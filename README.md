# 🤖 Olist D2C Natural Language-to-SQL AI Analytics Assistant

An enterprise-grade, portfolio-ready Natural Language-to-SQL analytics application built on the **Olist Brazilian E-Commerce dataset**. This tool empowers business stakeholders and data analysts to query a cloud data warehouse instantly using plain English, complete with automated executive insights and technical metadata transparency.

![Python](https://img.shields.io/badge/Python-3.10%25%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Cloud-red)
![LangChain](https://img.shields.io/badge/LangChain-SQL%20Agent-green)
![BigQuery](https://img.shields.io/badge/Google-BigQuery-orange)
![Groq](https://img.shields.io/badge/Groq-Qwen%203.8%2027B-purple)

---

## 🌟 Key Features

* **Natural Language to BigQuery SQL:** Translates complex business questions (e.g., cohort retention, state-wise revenue share, delivery delays) into optimized SQL queries executed directly against Google BigQuery.
* **Dynamic Strategic Recommendations:** Automatically evaluates query results using LLM reasoning to output tailored, actionable e-commerce operational insights.
* **Transparent Data Lineage:** Provides a dedicated technical expansion drawer detailing the source tables queried, warehouse provider, and execution type for every query.
* **Robust Hybrid Security:** Seamlessly handles authentication across local development (`credentials.json`) and cloud deployment (Streamlit Cloud `st.secrets` with temporary file mapping).
* **Token-Optimized ReAct Agent:** Constrained table scoping and iteration limits to maximize cost-efficiency and inference speed on the Groq API.
* **Interactive Portfolio Sidebar:** Includes quick-prompt buttons for complex multi-table analytics to showcase end-to-end data capability to recruiters.

---

## 🏗️ System Architecture

```text
 [ User / Recruiter ] 
         │ (Natural Language Prompt / Quick Button)
         ▼
 [ Streamlit Frontend App ] 
         │
         ├──> [ LangChain SQL Agent (ReAct Framework) ]
         │         │
         │         ├──> [ Groq LLM (qwen/qwen3.8-27b) ] ──> Dynamic Business Insights & Summaries
         │         │
         │         └──> [ SQLAlchemy BigQuery Dialect ]
         │                   │
         │                   ▼
         └──────────> [ Google BigQuery Data Warehouse (olist_warehouse) ]
