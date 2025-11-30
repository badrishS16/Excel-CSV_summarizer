# Excel-CSV_summarizer
This project builds an intelligent AI Agent capable of analyzing structured data (Excel &amp; CSV) through natural language conversations. Unlike standard chatbots that hallucinate numbers, this agent acts as a Compound System.

📖 About The Project
This project builds an intelligent AI Agent capable of analyzing structured data (Excel & CSV) through natural language conversations. Unlike standard chatbots that hallucinate numbers, this agent acts as a Compound System: it uses a Large Language Model (Llama 3 via Groq) to understand questions and generate Python/Pandas code, which is then executed locally to perform accurate calculations.

It is specifically optimized for financial data analysis (e.g., bank statements, yearly reports), allowing users to ask complex questions like "Summarize my spending for Q1" or "Compare income vs. expenses for January."

✨ Key Features
⚡ Blazing Fast Inference: Powered by Groq's LPU™ engine using the llama-3.3-70b-versatile model.

📊 Multi-Format Support: Automatically detects and handles both .xlsx (Excel) and .csv files.

🧮 Accurate Math: Uses a Pandas Dataframe Agent to perform actual calculations (filtering, grouping, summing) rather than relying on LLM arithmetic.

🔒 Privacy-Centric: Your data file remains local. Only column headers and rows necessary for context are sent to the API.

🛠️ Agentic Workflow: The system reasons through problems, creates a plan, executes Python code, and reflects on the output.

🛠️ Tech Stack
Python 3.10+

LangChain (Orchestration & Agent Tooling)

Groq API (LLM Inference)

Pandas (Data Manipulation)

OpenPyXL & Tabulate (File Handling & Formatting)

🚀 Getting Started
1. Clone the Repo
Bash

git clone https://github.com/yourusername/groq-data-analyst.git
cd groq-data-analyst
2. Install Dependencies
Bash

pip install langchain-groq langchain-experimental pandas openpyxl tabulate
3. Set Up API Key
You will need a free API Key from Groq Console.

Bash

# Linux/Mac
export GROQ_API_KEY="your_api_key_here"

# Windows (Powershell)
$env:GROQ_API_KEY="your_api_key_here"
4. Run the Agent
Place your bank_statement.csv or .xlsx file in the project folder and run:

Bash

python excel_agent.py
💡 Usage Examples
Input File: A yearly bank statement.

User Prompt:

"Summarize my total income and total expenses for the first quarter of 2024."

Agent "Thought" Process (Under the hood):

Thought: I need to filter the dataframe for dates between 2024-01-01 and 2024-03-31.

Action: Executes df['Date'] = pd.to_datetime(df['Date'])

Action: Executes df_q1 = df[(df['Date'] >= '2024-01-01') & (df['Date'] <= '2024-03-31')]

Action: Sums positive values for Income and negative values for Expenses.

Final Answer: "In Q1 2024, your Total Income was $13,500.00 and Total Expenses were $4,200.50."
