# **🧑‍💻 What is Agent Engineering?**

AI Engineering refers to the industry-relevant skills that data science and engineering teams need to successfully **build, deploy, operate, and improve Large Language Model (LLM) applications in production environments**.

In 2026, AI Engineers are responsible for building agents.

[Agent Engineering](https://blog.langchain.com/agent-engineering-a-new-discipline/), an emerging discipline, is defined as the iterative process of refining non-deterministic LLM systems into reliable production experiences.

# 📅 Structure & Format

Weekly content releases & tag-ups on Tuesdays from 5-6 PM ET

2 assignments per week

24-hour async Slack channel to be staffed to get responses *within the workday*

## 📚 Learning Outcomes

- **Week 1: Building & Vibe Checking Simple RAG Apps**
    - ✨Building LLM Apps with Simple Evals**:** Check the vibes on the LLM app you built during The AI Engineer Challenge and how even naive updating of context can have a big impact!
    - ****🗃️ Dense Vector Retrieval**:** Understand RAG from first principles, in concepts and in code
- **Week 2: Building Simple Agents**
    - ****🔁 The Agent Loop**:** Understand what an “agent” is and how to use the latest abstractions for building production-grade agents fast
    - 🕴️ Agentic RAG**:** Look under the hood of agentic RAG and the create_agent abstraction
- **Week 3: Building More Complex Agents**
    - 🔄 Multi-Agent Applications**:** Understand when to add additional agents to optimize context and how to construct agent teams using typical patterns.
    - 🧠 Agent Memory**:** Understand how to build agents capable of managing both short and long-term memory stores
- **Week 4: Systematic Evals for Agentic RAG Apps**
    - 🧪 Synthetic Data Generation for Evals**:** Understand how to generate test data automatically to test agentic RAG applications when you don’t have any eval datasets.
    - 📊 Agentic RAG Evaluation**:** Learn to set up and implement effective evals for agents and RAG applications.
- **Week 5: Deeper on Agents & RAG**
    - 🐕 Advanced Retrievers**:** Learn best practices for retrieval and a systematic approach for deciding on the best retriever for your AI applications.
    - **🔌 MCP Connectors:** Learn how to leverage collections of tools to enhance retrieval by sitting on the client side of MCP servers.
    - 📶 Deep Agents**:** Understand how to build complex agents that operate over longer time horizons.
    - 🕵️ Deep Research**:** Understand how to deep research systems work under the hood and how to build them.
- **Week 6: Agent Servers & Production Upgrades**
    - 🚢 Agent Servers**:** Learn to deploy complex agent applications to production endpoints that you can use elsewhe
    - 🔀 MCP Servers**:** Learn to set up MCP servers and enable public communication between agents.
    - 🛤️ Guardrails & Caching**:** 🎯 Learn a few upgrades: for performance and security/trustworthiness.

# **🧰 Tooling**

We will work within the AWS ecosystem and within the Deployment Process used by your organization; e.g.,

- **SRHG Deployment Process**
    1. GitHub
    2. Write code in branch
    3. PR / CODEOWNERS approval to merge to main
    4. GitHub Actions on ephemeral ARC CI/CD runners to build, test and deploy docker images to AWS ECR
    5. Terraform to manage declarative infrastructure in AWS
    6. ArgoCD watching `main` branch, sometimes auto-sync on, sometimes requiring manual sync, depending risk
    7. DataDog for metrics, monitoring, APM, logging

Specifically, we will leverage the following tooling in the curriculum and assignments:

- **Hardware Requirements**: Apple Macbook Pro, M-Chip Series
- **Cloud Service Provider**: AWS
- **LLM & Embedding Model Serving & Inference**: Anthropic Models through AWS Bedrock
- **Version Control**: GitHub
- **Coding Agent:** Claude Code (running locally)
- **MCP Servers**: Office365 ChatGPT connector, AWS Knowledgebase for Confluence (specific spaces)
- **Agent Orchestration**: LangGraph
- **Monitoring, Observability, and Deployment**: LangSmith

# 🧑‍🤝‍🧑 Your Support Team

- [Dr. Greg Loughnane, Ph.D](https://www.linkedin.com/in/gregloughnane/), CEO & Co-Founder @ AI Makerspace
- [Chris Alexiuk](https://www.linkedin.com/in/csalexiuk/), CTO & Co-Founder @ AI Makerspace
- [Dr. Katerina Gawthorpe, Ph.D.](https://www.linkedin.com/in/katerina-gawthorpe/), Co-Founder @ [eve.ai](http://eve.ai), AI Makerspace-Certified Consultant
- [Mani Sarkar](https://www.linkedin.com/in/mani-sarkar/), Freelance Consultant, 4X Kaggle Grandmaster
- [Laura Funderburk](https://www.linkedin.com/in/laurafunderburk/), Community & Developer Relations Lead @ AI Makerspace
- [Jacob Kilpatrick](https://www.linkedin.com/in/jacobkilpatrickai/), Course Operations Lead @ AI Makerspace

# **🏆 Grading**

Each week, you will receive personalized feedback from your support team on assignments submitted

# **📚 About**

This GitHub repository is your gateway to mastering the art of AI Engineering. ***All assignments for the course will be released here for your building, shipping, and sharing adventures!***