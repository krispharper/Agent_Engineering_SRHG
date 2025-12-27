# **🧑‍💻 What is Agent Engineering?**

AI Engineering refers to the industry-relevant skills that data science and engineering teams need to successfully **build, deploy, operate, and improve Large Language Model (LLM) applications in production environments**.

In 2026, AI Engineers are responsible for building agents.

[Agent Engineering](https://blog.langchain.com/agent-engineering-a-new-discipline/), an emerging discipline, is defined as the iterative process of refining non-deterministic LLM systems into reliable production experiences.

# 📅 Structure & Format

Weekly content releases & tag-ups on Tuesdays from 5-6 PM ET

2 assignments per week

24-hour async Slack channel to be staffed to get responses *within the workday*

## 📚 Learning Outcomes

**Week 1: Building & Vibe Checking Simple RAG Apps**

- *✨ Building LLM Apps with Simple Evals*: Check the vibes on the LLM app you built during The AI Engineer Challenge and see how even naive context updates can have a big impact.
- *🗃️ Dense Vector Retrieval*: Understand RAG from first principles, both conceptually and in code.


**Week 2: Building Simple Agents**

- *🔁 The Agent Loop*: Understand what an “agent” is and how to use the latest abstractions to build production-grade agents quickly.
- *🕴️ Agentic RAG*: Look under the hood of agentic RAG and the `create_agent` abstraction.


**Week 3: Building More Complex Agents**

- *🔄 Multi-Agent Applications*: Learn when to add additional agents to optimize context and how to construct agent teams using common patterns.
- *🧠 Agent Memory*: Learn how to build agents that manage both short- and long-term memory.


**Week 4: Systematic Evals for Agentic RAG Apps**

- *🧪 Synthetic Data Generation for Evals*: Learn how to automatically generate test data for agentic RAG applications when no eval datasets exist.
- *📊 Agentic RAG Evaluation*: Set up and implement effective evals for agents and RAG applications.


**Week 5: Deeper on Agents & RAG**

- *🐕 Advanced Retrievers*: Learn retrieval best practices and a systematic approach to choosing the right retriever for your AI applications.
- *🔌 MCP Connectors*: Learn how to leverage collections of tools to enhance retrieval on the client side of MCP servers.
- *📶 Deep Agents*: Build complex agents that operate over longer time horizons.
- *🕵️ Deep Research*: Understand how deep research systems work under the hood and how to build them.


**Week 6: Agent Servers & Production Upgrades**

- *🚢 Agent Servers*: Learn to deploy complex agent applications to production endpoints you can use elsewhere.
- *🔀 MCP Servers*: Learn how to set up MCP servers and enable public communication between agents.
- *🛤️ Guardrails & Caching*: Learn practical upgrades for performance, security, and trustworthiness.


# **🧰 Tooling**

We will work within the AWS ecosystem and within the Deployment Process used by your organization; e.g.,

<details>
<summary><strong>SRHG Deployment Process</strong></summary>

1. GitHub
2. Write code in a feature branch
3. PR with CODEOWNERS approval to merge into `main`
4. GitHub Actions on ephemeral ARC CI/CD runners to build, test, and deploy Docker images to AWS ECR
5. Terraform manages declarative infrastructure in AWS
6. ArgoCD watches the `main` branch  
   - Auto-sync enabled for low-risk changes  
   - Manual sync required for higher-risk changes
7. Datadog for metrics, monitoring, APM, and logging

</details>

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
