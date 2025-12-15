import os
import pandas as pd
from langchain_groq import ChatGroq
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv

load_dotenv()
# Now fetch the key securely
api_key = os.getenv("GROQ_API_KEY")

# Optional: Check if key loaded correctly
if not api_key:
    raise ValueError("GROQ_API_KEY not found. Please check your .env file.")

def analyze_excel(file_path, user_query):
    """
    Creates an AI agent to analyze Excel OR CSV files using Groq.
    """
    
    #Smart detection of file type
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(file_path)
        else:
            return " Error: Unsupported file format. Please use .csv or .xlsx"
            
        print(f" Successfully loaded '{file_path}' with {len(df)} rows.")
    except Exception as e:
        return f"Error loading file: {e}"

    #INITIALIZE MODEL
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    #CREATE AGENT
    agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=True,
        allow_dangerous_code=True
    )

    #RUN QUERY
    print(f"\n Agent is analyzing: '{user_query}'...\n")
    try:
        response = agent.invoke(user_query)
        return response['output']
    except Exception as e:
        return f"Error during analysis: {e}"

# MAIN EXECUTION
if __name__ == "__main__":
    # Replace with the path to your actual bank statement
    excel_file = "bankstatements.csv" 
    
    #Dummy file if user's file doen not exist
    if not os.path.exists(excel_file):
        data = {
            'Date': ['2024-01-15', '2024-02-20', '2024-03-10', '2024-01-25'],
            'Description': ['Salary', 'Grocery Store', 'Electric Bill', 'Freelance Work'],
            'Amount': [5000, -150, -120, 1200],
            'Category': ['Income', 'Expense', 'Expense', 'Income']
        }
        pd.DataFrame(data).to_excel(excel_file, index=False)
        print("created dummy file")

    #Prompt
    prompt = "Tell me the amount spent on 17th of august, 2023."
    
    result = analyze_excel(excel_file, prompt)
    print("\n SUMMARY:\n", result)