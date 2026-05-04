 🤖 AI SQL Data Analyst Agent

An end-to-end AI-powered data analysis application that converts CSV data into SQL, understands natural language queries, and returns insights along with visualizations.

 🚀 Features

* 📂 Upload CSV files dynamically
* 🧠 Convert natural language → SQL queries using LLM
* 🗄️ Automatic SQLite database creation
* 📊 Execute queries and return results instantly
* 📈 Generate visualizations (charts)
* 💬 Interactive UI using Streamlit


 🧠 How It Works

CSV File → Pandas → SQLite Database  
        ↓  
User Question (Natural Language)  
        ↓  
LLM (Groq - Llama 3)  
        ↓  
SQL Query Generation  
        ↓  
Execute Query  
        ↓  
Return Answer + Visualization


 🛠️ Tech Stack

* Frontend:Streamlit
* Backend: Python
* LLM: Groq (Llama 3.1)
* Framework: LangChain
* Database:SQLite
* Data Processing: Pandas
* Visualization: Plotly / Matplotlib


 ⚙️ Installation

1. Clone the repository

bash
git clone https://github.com/your-username/AI-SQL-Data-Analyst-Agent.git
cd AI-SQL-Data-Analyst-Agent


 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows


 3. Install dependencies
pip install -r requirements.txt

🔑 Environment Variables
Create a `.env` file and add:
GROQ_API_KEY=your_api_key_here


 ▶️ Run the App
streamlit run app_streamlit.py

 💡 Example Queries

* What is the average price?
* Top 5 neighbourhoods with highest listings
* Show distribution of prices
* Which room type is most common?


 🔐 Security Note

* API keys are stored using environment variables
* No sensitive data is exposed in the repository

 📌 Future Improvements

* Add support for multiple tables
* Improve query accuracy with schema awareness
* Add downloadable reports
* Deploy on cloud (Streamlit Cloud / AWS)

 👩‍💻 Author

Vinutha Thimmaiah

 ⭐ If you like this project

Give it a ⭐ on GitHub!
