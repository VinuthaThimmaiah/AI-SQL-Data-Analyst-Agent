import streamlit as st
import pandas as pd
import sqlite3
import re
import plotly.express as px
from langchain_groq import ChatGroq
import os

st.set_page_config(page_title="AI SQL Data Analyst", layout="wide")

st.title("🤖 AI SQL Data Analyst Agent")

# Upload CSV
uploaded_file = st.file_uploader("📂 Upload your CSV file")

if uploaded_file:
    # Load data
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    st.subheader("📊 Data Preview")
    st.dataframe(df.head())

    # Save to SQLite
    conn = sqlite3.connect("data.db")
    df.to_sql("airbnb_data", conn, if_exists="replace", index=False)

    # LLM Setup
    import os

    groq_api_key = os.getenv("GROQ_API_KEY")

    llm = ChatGroq(
        groq_api_key=groq_api_key,
        model_name="llama-3.1-8b-instant"
    )

    # User Input
    user_question = st.text_input("💬 Ask your question")

    if user_question:
        with st.spinner("Thinking... 🤔"):
            try:
                # Step 1: Generate SQL
                raw_output = llm.invoke(
                    f"Write ONLY a SQL query for: {user_question}. Use table airbnb_data. No explanation."
                ).content

                # Step 2: Extract SQL
                match = re.search(r"SELECT.*?;", raw_output, re.DOTALL | re.IGNORECASE)

                if not match:
                    st.error("❌ Could not generate valid SQL query")
                else:
                    query = match.group(0)

                    st.subheader("🧾 Generated SQL")
                    st.code(query, language="sql")

                    # Step 3: Execute SQL
                    cursor = conn.cursor()
                    cursor.execute(query)

                    rows = cursor.fetchall()
                    columns = [desc[0] for desc in cursor.description]

                    result_df = pd.DataFrame(rows, columns=columns)

                    st.subheader("✅ Answer")
                    st.dataframe(result_df)

                    # Step 4: Visualization
                    if len(result_df.columns) >= 2:
                        try:
                            fig = px.bar(
                                result_df,
                                x=result_df.columns[0],
                                y=result_df.columns[1],
                                title="📈 Query Result Visualization"
                            )
                            st.plotly_chart(fig, use_container_width=True)
                        except:
                            st.info("ℹ️ Visualization not applicable for this query")

            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")