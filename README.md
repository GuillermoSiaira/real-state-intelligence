# 🏢 Commercial Real Estate Intelligence Dashboard

**Automated Lead Enrichment & Sales Outreach Engine**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://real-state-intelligence-8uwf8oghqfpi2eweubtgtv.streamlit.app/)

## 🚀 Overview
This project demonstrates an **AI-powered sales pipeline accelerator** designed for the Industrial Real Estate sector. It solves the "data overload" problem by aggregating raw property data (simulating CoStar exports), enriching it with owner contact info (simulating Clay/ZoomInfo), and prioritizing targets based on **Lost Revenue due to Vacancy**.

## 🎯 Key Features
* **Automated Enrichment Pipeline:** Ingests raw property addresses and enriches them with owner details and financial metrics.
* **High-Value Target Identification:** Automatically ranks leads by "Opportunity Size" ($ Lost Revenue), allowing sales teams to focus on high-impact deals first.
* **AI Analyst Agent:** A sidebar chatbot that interprets pipeline data to provide actionable "Next Best Actions" (e.g., *"Contact Maria Garcia immediately due to $2.7M annual loss"*).
* **Zero-Latency Architecture:** Optimized for instant load times during high-stakes presentations.

## 🛠️ Tech Stack
* **Python 3.13**
* **Streamlit** (Frontend & Interactivity)
* **Pandas** (Data Manipulation)
* **Plotly Express** (Data Visualization)
* **PostgreSQL Ready** (Architecture designed for SQL integration, currently running in "Demo Mode" with static data for showcase stability).

## 📸 Demo
Check out the live application here: 
👉 **[Launch Live Dashboard](https://real-state-intelligence-8uwf8oghqfpi2eweubtgtv.streamlit.app/)**

![Dashboard Preview](dashboard_preview.png)
*(Note: Data in this demo is simulated for privacy and demonstration purposes)*

## 📦 Local Installation
To run this dashboard on your local machine:

```bash
git clone [https://github.com/GuillermoSiaira/real-state-intelligence.git](https://github.com/GuillermoSiaira/real-state-intelligence.git)
cd real-state-intelligence
pip install -r requirements.txt
streamlit run dashboard/app.py