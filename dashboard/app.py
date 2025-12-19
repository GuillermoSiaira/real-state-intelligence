import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import time

# Page Config
st.set_page_config(page_title="Vape/Real Estate Intelligence", layout="wide")

# DB Connection
db_connection_str = 'postgresql://n8n_user:n8n_password@postgres:5432/n8n_db'
db_connection = create_engine(db_connection_str)

# --- SIDEBAR: AI CHATBOT SIMULATION ---
with st.sidebar:
    st.header("🤖 AI Analyst Agent")
    st.caption("Ask questions about your pipeline...")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hello! I've analyzed the CoStar and Clay data. How can I help you close a deal today?"}]

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # User Input
    if prompt := st.chat_input("Ex: 'Best opportunity?'"):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # SIMULATED AI RESPONSE (Safe for Demo)
        with st.chat_message("assistant"):
            with st.spinner("Analyzing vacancy rates and revenue models..."):
                time.sleep(1.5) # Fake thinking time for dramatic effect
                
                # Logic to get the best lead from DB
                try:
                    df_chat = pd.read_sql("SELECT * FROM leads ORDER BY lost_revenue DESC LIMIT 1", db_connection)
                    if not df_chat.empty:
                        top_lead = df_chat.iloc[0]
                        response = f"Based on the analysis, you should contact **{top_lead['owner_name']}** immediately. \n\n Their property at **{top_lead['address']}** is losing **** annually due to vacancy. I have their email ({top_lead['owner_email']}) ready for outreach."
                    else:
                        response = "I need more data ingested to provide recommendations."
                except:
                    response = "System is syncing. Please check the dashboard."
                
                st.write(response) 
                st.session_state.messages.append({"role": "assistant", "content": response})

# --- MAIN DASHBOARD ---
st.title("🏢 Commercial Real Estate Intelligence")
st.markdown("### Automated Lead Enrichment Pipeline (CoStar + Clay)")

try:
    # Load Data
    df = pd.read_sql("SELECT * FROM leads", db_connection)
    
    # KPI Section
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Qualified Leads", len(df))
        
    with col2:
        total_lost = df['lost_revenue'].sum()
        st.metric("Total Pipeline Value (Est.)", f"")
        
    with col3:
        avg_vacancy = df['vacancy_rate'].mean()
        st.metric("Avg. Vacancy Rate", f"{avg_vacancy:.1f}%")

    st.divider()

    # Layout: Charts and Data
    col_chart, col_data = st.columns([1, 2])

    with col_chart:
        st.subheader("🔥 Top High-Value Targets")
        top_opportunities = df.sort_values(by='lost_revenue', ascending=False).head(5)
        st.bar_chart(top_opportunities, x='address', y='lost_revenue')

    with col_data:
        st.subheader("Live Data Feed (Enriched)")
        display_df = df.rename(columns={
            'property_id': 'ID',
            'address': 'Property Address',
            'owner_name': 'Owner',
            'owner_email': 'Contact Email',
            'lost_revenue': 'Opportunity ($)'
        })
        st.dataframe(display_df[['Property Address', 'Owner', 'Contact Email', 'Opportunity ($)']], use_container_width=True)

except Exception as e:
    st.error(f"Connection Error: {e}")

