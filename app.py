import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Configuración de página
st.set_page_config(page_title="Real Estate Intelligence", layout="wide")

# --- MODO DEMO: DATOS ESTÁTICOS (Sin SQL) ---
# Estos son los datos exactos de tu captura de pantalla
data = {
    "Property Address": ["9349 Main St, Miami, FL", "4389 Main St, Miami, FL", "2252 Main St, Miami, FL", "3081 Main St, Miami, FL", "7103 Main St, Miami, FL", "972 Main St, Miami, FL"],
    "Owner": ["John Smith", "Ahmed Al-Fayed", "Maria Garcia", "Robert Johnson", "Robert Johnson", "Robert Johnson"],
    "Contact Email": ["None", "None", "None", "None", "None", "None"],
    "Opportunity ($)": [287103.7, 1431109.68, 2720071.2, 39297.1, 158657.28, 269960.14],
    "lost_revenue": [287103, 1431109, 2720071, 39297, 158657, 269960] 
}
df = pd.DataFrame(data)

# --- SIDEBAR: AI AGENT (Simulado para velocidad o Real si hay Key) ---
with st.sidebar:
    st.header("🤖 AI Analyst Agent")
    st.write("Ask questions about your pipeline...")
    
    # Simulación de chat para la demo (Seguridad total)
    user_input = st.text_input("Ex: 'Best opportunity?'")
    
    if user_input:
        st.info("🤖 Based on the analysis, you should contact **Maria Garcia** immediately.")
        st.write("Her property at **2252 Main St, Miami, FL** is losing **$2.7M annually** due to vacancy.")
        st.write("I have her email ready for outreach.")

# --- MAIN DASHBOARD ---
st.title("🏢 Commercial Real Estate Intelligence")
st.subheader("Automated Lead Enrichment Pipeline (CoStar + Clay)")

# KPIs Top
col1, col2, col3 = st.columns(3)
col1.metric("Qualified Leads", "6")
col2.metric("Total Pipeline Value (Est.)", "$4.2M")
col3.metric("Avg. Vacancy Rate", "20.5%")

st.divider()

# Gráfico y Tabla
c1, c2 = st.columns([1, 2])

with c1:
    st.subheader("🔥 Top High-Value Targets")
    fig = px.bar(df, x='Property Address', y='lost_revenue')
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.subheader("Live Data Feed (Enriched)")
    st.dataframe(df, use_container_width=True)

