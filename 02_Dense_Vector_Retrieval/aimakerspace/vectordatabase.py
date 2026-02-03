import numpy as np
from collections import defaultdict
from typing import List, Tuple, Callable
from aimakerspace.openai_utils.embedding import EmbeddingModel
import asyncio
from enum import Enum


class DistanceMetric(Enum):
    """
    Enumeration of supported distance metrics.

    Metrics marked as 'similarity' are higher-is-better (descending sort).
    Metrics marked as 'distance' are lower-is-better (ascending sort).
    """
    COSINE = "cosine"  # similarity
    EUCLIDEAN = "euclidean"  # distance
    MANHATTAN = "manhattan"  # distance
    DOT_PRODUCT = "dot_product"  # similarity
    CHEBYSHEV = "chebyshev"  # distance


def cosine_similarity(vector_a: np.array, vector_b: np.array) -> float:
    """
    Computes the cosine similarity between two vectors.

    Returns a value between -1 and 1, where 1 means identical direction.
    Higher values indicate more similarity.
    """
    dot_product = np.dot(vector_a, vector_b)
    norm_a = np.linalg.norm(vector_a)
    norm_b = np.linalg.norm(vector_b)
    return dot_product / (norm_a * norm_b)


def euclidean_distance(vector_a: np.array, vector_b: np.array) -> float:
    """
    Computes the Euclidean (L2) distance between two vectors.

    This is the straight-line distance between two points.
    Lower values indicate more similarity.
    """
    return np.linalg.norm(vector_a - vector_b)


def manhattan_distance(vector_a: np.array, vector_b: np.array) -> float:
    """
    Computes the Manhattan (L1) distance between two vectors.

    This is the sum of absolute differences between coordinates.
    Lower values indicate more similarity.
    """
    return np.sum(np.abs(vector_a - vector_b))


def dot_product(vector_a: np.array, vector_b: np.array) -> float:
    """
    Computes the dot product between two vectors.

    Higher values indicate more similarity.
    Note: Unlike cosine similarity, this is not normalized.
    """
    return np.dot(vector_a, vector_b)


def chebyshev_distance(vector_a: np.array, vector_b: np.array) -> float:
    """
    Computes the Chebyshev (L-infinity) distance between two vectors.

    This is the maximum absolute difference along any dimension.
    Lower values indicate more similarity.
    """
    return np.max(np.abs(vector_a - vector_b))


class VectorDatabase:
    """
    A simple vector database for storing and retrieving text embeddings.

    Supports multiple distance metrics for similarity search:
    - cosine: Cosine similarity (default, normalized dot product)
    - euclidean: L2 distance
    - manhattan: L1 distance
    - dot_product: Raw dot product (unnormalized)
    - chebyshev: L-infinity distance (max absolute difference)
    """

    # Mapping from metric name to function
    METRIC_FUNCTIONS = {
        DistanceMetric.COSINE: cosine_similarity,
        DistanceMetric.EUCLIDEAN: euclidean_distance,
        DistanceMetric.MANHATTAN: manhattan_distance,
        DistanceMetric.DOT_PRODUCT: dot_product,
        DistanceMetric.CHEBYSHEV: chebyshev_distance,
    }

    # Metrics where higher scores are better (similarities)
    SIMILARITY_METRICS = {DistanceMetric.COSINE, DistanceMetric.DOT_PRODUCT}

    def __init__(
        self,
        embedding_model: EmbeddingModel = None,
        distance_metric: DistanceMetric = DistanceMetric.COSINE
    ):
        """
        Initialize the vector database.

        Args:
            embedding_model: The model to use for generating embeddings
            distance_metric: The distance metric to use for similarity search
        """
        self.vectors = defaultdict(np.array)
        self.embedding_model = embedding_model or EmbeddingModel()
        self.distance_metric = distance_metric
        self.distance_function = self.METRIC_FUNCTIONS[distance_metric]

    def insert(self, key: str, vector: np.array) -> None:
        self.vectors[key] = vector

    def search(
        self,
        query_vector: np.array,
        k: int,
        distance_measure: Callable = None,
    ) -> List[Tuple[str, float]]:
        """
        Search for the k most similar vectors.

        Args:
            query_vector: The query vector to search for
            k: Number of results to return
            distance_measure: Optional custom distance function (overrides default)

        Returns:
            List of (text, score) tuples, sorted by relevance
        """
        # Use provided distance measure or fall back to the instance default
        measure_func = distance_measure or self.distance_function

        scores = [
            (key, measure_func(query_vector, vector))
            for key, vector in self.vectors.items()
        ]

        # Determine sort order based on metric type
        # For similarities (cosine, dot product), higher is better (reverse=True)
        # For distances (euclidean, manhattan, etc.), lower is better (reverse=False)
        if distance_measure is None:
            # Using instance default metric
            reverse_sort = self.distance_metric in self.SIMILARITY_METRICS
        else:
            # Using custom distance measure - default to similarity behavior
            # (reverse=True for backward compatibility)
            reverse_sort = True

        return sorted(scores, key=lambda x: x[1], reverse=reverse_sort)[:k]

    def search_by_text(
        self,
        query_text: str,
        k: int,
        distance_measure: Callable = None,
        return_as_text: bool = False,
    ) -> List[Tuple[str, float]]:
        """
        Search for the k most similar texts using a text query.

        Args:
            query_text: The text to search for
            k: Number of results to return
            distance_measure: Optional custom distance function (overrides default)
            return_as_text: If True, return only text; if False, return (text, score) tuples

        Returns:
            List of texts or (text, score) tuples, sorted by relevance
        """
        query_vector = self.embedding_model.get_embedding(query_text)
        results = self.search(query_vector, k, distance_measure)
        return [result[0] for result in results] if return_as_text else results

    def get_metric_info(self) -> dict:
        """
        Get information about the currently configured distance metric.

        Returns:
            Dictionary with metric name, type, and description
        """
        metric_type = "similarity" if self.distance_metric in self.SIMILARITY_METRICS else "distance"
        return {
            "metric": self.distance_metric.value,
            "type": metric_type,
            "description": self.distance_function.__doc__.strip() if self.distance_function.__doc__ else ""
        }

    def retrieve_from_key(self, key: str) -> np.array:
        return self.vectors.get(key, None)

    async def abuild_from_list(self, list_of_text: List[str]) -> "VectorDatabase":
        embeddings = await self.embedding_model.async_get_embeddings(list_of_text)
        for text, embedding in zip(list_of_text, embeddings):
            self.insert(text, np.array(embedding))
        return self


if __name__ == "__main__":
    list_of_text = [
        "I like to eat broccoli and bananas.",
        "I ate a banana and spinach smoothie for breakfast.",
        "Chinchillas and kittens are cute.",
        "My sister adopted a kitten yesterday.",
        "Look at this cute hamster munching on a piece of broccoli.",
    ]

    vector_db = VectorDatabase()
    vector_db = asyncio.run(vector_db.abuild_from_list(list_of_text))
    k = 2

    searched_vector = vector_db.search_by_text("I think fruit is awesome!", k=k)
    print(f"Closest {k} vector(s):", searched_vector)

    retrieved_vector = vector_db.retrieve_from_key(
        "I like to eat broccoli and bananas."
    )
    print("Retrieved vector:", retrieved_vector)

    relevant_texts = vector_db.search_by_text(
        "I think fruit is awesome!", k=k, return_as_text=True
    )
    print(f"Closest {k} text(s):", relevant_texts)
