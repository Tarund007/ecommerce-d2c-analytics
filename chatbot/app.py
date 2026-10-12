# import streamlit as st
# from langchain_community.utilities.sql_database import SQLDatabase
# from langchain_community.agent_toolkits import create_sql_agent
# from langchain_google_genai import ChatGoogleGenerativeAI

# import os

# # --- Streamlit Page Configuration ---
# st.set_page_config(
#     page_title="Olist D2C AI Analytics Assistant",
#     page_icon="🤖",
#     layout="wide"
# )

# st.title("🤖 Olist D2C Natural Language-to-SQL Assistant")
# st.markdown("""
# Ask questions about your Brazilian E-Commerce data warehouse in plain English! 
# The AI agent will inspect your schema, write the BigQuery SQL, execute it, and return the insights.
# """)

# # --- Sidebar Configuration for API Keys ---
# with st.sidebar:
#     st.header("⚙️ Configuration")
#     google_api_key = st.text_input("Enter Google Gemini API Key:", type="password") 
    
#     st.markdown("---")
#     st.markdown("### Example Prompts:")
#     st.markdown("- *What are the top 5 product categories by total sales?*")
#     st.markdown("- *What is the average order delivery time?*")
#     st.markdown("- *How many unique customers made a purchase?*")

# # --- Database Connection Setup ---
# @st.cache_resource
# #py_func_cache = True
# def get_db_connection():
#     # Replace 'olist-d2c-analytics' with your actual GCP Project ID if it differs
#     db_uri = "bigquery://olist-d2c-analytics/olist_warehouse"
#     return SQLDatabase.from_uri(db_uri)

# if not google_api_key:
#     st.warning("⚠️ Please enter your Google Gemini API key in the sidebar to initialize the AI agent.")
# else:
#     try:
#         db = get_db_connection()
        
#         # Initialize the LLM
#         llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite", google_api_key=google_api_key, temperature=0)
        
#         # Create the LangChain SQL Agent toolkit
#         agent_executor = create_sql_agent(
#             llm=llm,
#             db=db,
#             verbose=True,
#             agent_type="zero-shot-react-description",# Standard zero-shot agent works best with Gemini
#             agent_executor_kwargs={"handle_parsing_errors": True}
            
#         )
        
#         # --- Chat Interface ---
#         if "messages" not in st.session_state:
#             st.session_state.messages = []

#         # Display historical messages
#         for message in st.session_state.messages:
#             with st.chat_message(message["role"]):
#                 st.markdown(message["content"])

#         # User input box
#         if prompt := st.chat_input("Ask a data question..."):
#             st.session_state.messages.append({"role": "user", "content": prompt})
#             with st.chat_message("user"):
#                 st.markdown(prompt)

#             with st.chat_message("assistant"):
#                 with st.spinner("Analyzing schema and querying BigQuery..."):
#                     try:
#                         # Invoke the LangChain agent with the user's prompt
#                         response = agent_executor.run(prompt)
#                         st.markdown(response)
#                         st.session_state.messages.append({"role": "assistant", "content": response})
#                     except Exception as e:
#                         error_msg = f"An error occurred while executing the query: {e}"
#                         st.error(error_msg)

#     except Exception as e:
#         st.error(f"Failed to connect to BigQuery database. Check your credentials: {e}")

 #its for openai api key
# import streamlit as st
# from langchain_community.utilities.sql_database import SQLDatabase
# from langchain_community.agent_toolkits import create_sql_agent
# from langchain_openai import ChatOpenAI
# import os

# # --- Google Cloud Credentials Setup ---

# # --- Streamlit Page Configuration ---
# st.set_page_config(
#     page_title="Olist D2C AI Analytics Assistant",
#     page_icon="🤖",
#     layout="wide"
# )

# st.title("🤖 Olist D2C Natural Language-to-SQL Assistant")
# st.markdown("""
# Ask questions about your Brazilian E-Commerce data warehouse in plain English! 
# The AI agent will inspect your schema, write the BigQuery SQL, execute it, and return the insights.
# """)

# # --- 1. Sidebar Configuration MUST come first so the variable exists ---
# with st.sidebar:
#     st.header("⚙️ Configuration")
#     openai_api_key = st.text_input("Enter OpenAI API Key:", type="password")
    
#     st.markdown("---")
#     st.markdown("### Example Prompts:")
#     st.markdown("- *How many rows are in the cleaned_customers table?*")
#     st.markdown("- *What are the top 5 product categories by total sales?*")

# # --- Database Connection Function ---
# @st.cache_resource
# def get_db_connection():
#     db_uri = "bigquery://olist-d2c-analytics/olist_warehouse"
#     return SQLDatabase.from_uri(db_uri)

# # --- 2. Now check the variable safely ---
# if not openai_api_key:
#     st.warning("⚠️ Please enter your OpenAI API key in the sidebar to initialize the AI agent.")
# else:
#     try:
#         db = get_db_connection()
        
#         # Initialize the OpenAI LLM
#         llm = ChatOpenAI(
#             model="gpt-4o-mini", 
#             openai_api_key=openai_api_key, 
#             temperature=0
#         )
        
#         # Create the LangChain SQL Agent toolkit
#         agent_executor = create_sql_agent(
#             llm=llm,
#             db=db,
#             verbose=True,
#             agent_type="zero-shot-react-description",
#             agent_executor_kwargs={"handle_parsing_errors": True}
#         )
        
#         # --- Chat Interface ---
#         if "messages" not in st.session_state:
#             st.session_state.messages = []

#         for message in st.session_state.messages:
#             with st.chat_message(message["role"]):
#                 st.markdown(message["content"])

#         if prompt := st.chat_input("Ask a data question..."):
#             st.session_state.messages.append({"role": "user", "content": prompt})
#             with st.chat_message("user"):
#                 st.markdown(prompt)

#             with st.chat_message("assistant"):
#                 with st.spinner("Analyzing schema and querying BigQuery..."):
#                     try:
#                         response = agent_executor.run(prompt)
#                         st.markdown(response)
#                         st.session_state.messages.append({"role": "assistant", "content": response})
#                     except Exception as e:
#                         st.error(f"An error occurred while executing the query: {e}")

#     except Exception as e:
#         st.error(f"Failed to connect to BigQuery database. Check your credentials: {e}")

# import streamlit as st
# from langchain_community.utilities.sql_database import SQLDatabase
# from langchain_community.agent_toolkits import create_sql_agent
# from langchain_groq import ChatGroq

# # --- Streamlit Page Configuration ---
# st.set_page_config(
#     page_title="Olist D2C AI Analytics Assistant",
#     page_icon="🤖",
#     layout="wide"
# )

# st.title("🤖 Olist D2C Natural Language-to-SQL Assistant")
# st.markdown("""
# Ask questions about your Brazilian E-Commerce data warehouse in plain English! 
# The AI agent will inspect your schema, write the BigQuery SQL, execute it, and return the insights.
# """)

# # --- Sidebar Configuration for API Key ---
# with st.sidebar:
#     st.header("⚙️ Configuration")
#     groq_api_key = st.text_input("Enter Groq API Key:", type="password")
    
#     st.markdown("---")
#     st.markdown("### Example Prompts:")
#     st.markdown("- *How many rows are in the cleaned_customers table?*")
#     st.markdown("- *What are the top 5 product categories by total sales?*")
#     st.markdown("- *What is the average order delivery time?*")
#     st.markdown("- *Top 5 product categories by revenue & order count*")
#     st.markdown("- *Top 5 customer states by revenue & unique customers*")
#     st.markdown("- *Payment type share breakdown (credit card, boleto, etc.)*")
#     st.markdown("- *Average delivery delay grouped by customer state*")
#     st.markdown("- *Monthly order volume and revenue trend for 2018*")

# # --- Database Connection Setup ---
# @st.cache_resource
# def get_db_connection():
#     # BigQuery connection URI via SQLAlchemy
#     db_uri = "bigquery://olist-d2c-analytics/olist_warehouse"
#     return SQLDatabase.from_uri(db_uri)

# # --- Check API Key and Initialize Agent ---
# if not groq_api_key:
#     st.warning("⚠️ Please enter your free Groq API key in the sidebar to initialize the AI agent.")
# else:
#     try:
#         db = get_db_connection()
        
#         # Initialize the free, lightning-fast Groq model
#         llm = ChatGroq(
#             model="meta-llama/llama-prompt-guard-2-86m", 
#             groq_api_key=groq_api_key, 
#             temperature=0
#         )
        
#         # Create the LangChain SQL Agent toolkit with error handling enabled
#         agent_executor = create_sql_agent(
#             llm=llm,
#             db=db,
#             verbose=True,
#             agent_type="zero-shot-react-description",
#             agent_executor_kwargs={"handle_parsing_errors": True}
#         )
        
#         # --- Chat Interface State ---
#         if "messages" not in st.session_state:
#             st.session_state.messages = []

#         # Display historical messages
#         for message in st.session_state.messages:
#             with st.chat_message(message["role"]):
#                 st.markdown(message["content"])

#         # User input box
#         if prompt := st.chat_input("Ask a data question..."):
#             st.session_state.messages.append({"role": "user", "content": prompt})
#             with st.chat_message("user"):
#                 st.markdown(prompt)

#             with st.chat_message("assistant"):
#                 with st.spinner("Analyzing schema and querying BigQuery..."):
#                     try:
#                         # Invoke the LangChain agent with the user's prompt
#                         response = agent_executor.run(prompt)
#                         st.markdown(response)
#                         st.session_state.messages.append({"role": "assistant", "content": response})
#                     except Exception as e:
#                         error_msg = f"An error occurred while executing the query: {e}"
#                         st.error(error_msg)

#     except Exception as e:
#         st.error(f"Failed to connect to BigQuery database. Check your credentials: {e}")



# import os
# import streamlit as st
# from langchain_community.utilities.sql_database import SQLDatabase
# from langchain_community.agent_toolkits import create_sql_agent
# from langchain_groq import ChatGroq

# # --- Google Cloud Credentials Setup ---
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"D:\Data Analytics\Chat D2C\Chatbot\olist-ai-assistant\credentials.json"

# # --- Streamlit Page Configuration ---
# st.set_page_config(
#     page_title="Olist D2C AI Analytics Assistant",
#     page_icon="🤖",
#     layout="wide"
# )

# # --- Custom CSS Styling for a Sleek Enterprise Look ---
# st.markdown("""
#     <style>
#         /* Main background & font styling */
#         .main {
#             background-color: #0e1117;
#         }
#         /* Custom header styling */
#         h1 {
#             color: #ffffff;
#             font-family: 'Segoe UI', sans-serif;
#             font-weight: 700;
#         }
#         /* Style input fields and chat containers */
#         .stTextInput input {
#             border-radius: 8px;
#             border: 1px solid #30363d;
#             background-color: #161b22;
#             color: #ffffff;
#         }
#         /* Custom info cards */
#         .metric-card {
#             background-color: #161b22;
#             border: 1px solid #30363d;
#             padding: 15px;
#             border-radius: 10px;
#             margin-bottom: 10px;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # --- Title Header & Description ---
# st.title("🤖 Olist D2C Natural Language-to-SQL Assistant")
# st.markdown("Query your Brazilian E-Commerce BigQuery data warehouse instantly using natural language.")
# st.markdown("---")

# # --- Sidebar Configuration & Interactive Prompts ---
# with st.sidebar:
#     st.header("⚙️ Configuration")
#     groq_api_key = st.text_input("Enter Groq API Key:", type="password")
    
#     st.markdown("---")
#     st.markdown("### 💡 Quick Portfolio Prompts")
#     st.markdown("*(Click an idea to copy or test)*")
    
#     # Session state helper to store selected prompt
#     if "selected_prompt" not in st.session_state:
#         st.session_state.selected_prompt = ""

#     prompts = [
#         "What are the top 5 product categories by total sales?",
#         "Top 5 customer states by revenue & unique customers",
#         "What is the average order delivery time?",
#         "Payment type share breakdown (credit card, boleto, etc.)",
#         "Monthly order volume and revenue trend for 2018"
#     ]
    
#     for p in prompts:
#         if st.button(p, use_container_width=True):
#             st.session_state.selected_prompt = p

#     st.markdown("---")
#     st.markdown("### 📊 Warehouse Status")
#     st.markdown("🟢 **BigQuery**: Connected (`olist_warehouse`)")
#     st.markdown("⚡ **LLM**: Groq (`qwen/qwen3.8-27b`)")

# # --- Database Connection Setup ---
# @st.cache_resource
# def get_db_connection():
#     db_uri = "bigquery://olist-d2c-analytics/olist_warehouse"
#     return SQLDatabase.from_uri(db_uri)

# # --- Check API Key and Initialize Agent ---
# if not groq_api_key:
#     st.warning("⚠️ Please enter your free Groq API key in the sidebar to initialize the AI agent.")
# else:
#     try:
#         db = get_db_connection()
        
#         # Initialize Groq LLM
#         llm = ChatGroq(
#             model="qwen/qwen3.8-27b", 
#             groq_api_key=groq_api_key, 
#             temperature=0
#         )
        
#         # Create LangChain SQL Agent with error handling
#         agent_executor = create_sql_agent(
#             llm=llm,
#             db=db,
#             verbose=True,
#             agent_type="zero-shot-react-description",
#             agent_executor_kwargs={"handle_parsing_errors": True}
#         )
        
#         # --- Chat Interface State ---
#         if "messages" not in st.session_state:
#             st.session_state.messages = []

#         # Display historical messages
#         for message in st.session_state.messages:
#             with st.chat_message(message["role"]):
#                 st.markdown(message["content"])

#         # Handle user prompt (either from chat input box or sidebar quick button)
#         chat_placeholder = "Ask a data question..."
#         prompt = st.chat_input(chat_placeholder)
        
#         # If a sidebar quick button was clicked, use it as the prompt
#         if st.session_state.selected_prompt:
#             prompt = st.session_state.selected_prompt
#             st.session_state.selected_prompt = ""  # reset after capturing

#         if prompt:
#             st.session_state.messages.append({"role": "user", "content": prompt})
#             with st.chat_message("user"):
#                 st.markdown(prompt)

#             with st.chat_message("assistant"):
#                 with st.spinner("🔍 Inspecting schema, writing BigQuery SQL, and executing..."):
#                     try:
#                         response = agent_executor.run(prompt)
#                         st.markdown(response)
#                         st.session_state.messages.append({"role": "assistant", "content": response})
#                     except Exception as e:
#                         error_msg = f"An error occurred while executing the query: {e}"
#                         st.error(error_msg)

#     except Exception as e:
#         st.error(f"Failed to connect to BigQuery database. Check your credentials: {e}")



import os
import json
import tempfile
import streamlit as st
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_groq import ChatGroq

# --- Database & Credentials Connection Setup ---
@st.cache_resource
def get_db_connection():
    try:
        if "gcp_service_account" in st.secrets:
            service_account_info = dict(st.secrets["gcp_service_account"])
            with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".json") as temp:
                json.dump(service_account_info, temp)
                temp_path = temp.name
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = temp_path
    except Exception:
        local_creds = r"D:\Data Analytics\Chat D2C\Chatbot\olist-ai-assistant\credentials.json"
        if os.path.exists(local_creds):
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = local_creds

    db_uri = "bigquery://olist-d2c-analytics/olist_warehouse"
    return SQLDatabase.from_uri(db_uri)

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="Olist D2C AI Analytics Assistant",
    page_icon="🤖",
    layout="wide"
)

# --- Custom CSS Styling for a Sleek Enterprise Look ---
st.markdown("""
    <style>
        .main {
            background-color: #0e1117;
        }
        h1 {
            color: #ffffff;
            font-family: 'Segoe UI', sans-serif;
            font-weight: 700;
        }
        .stTextInput input {
            border-radius: 8px;
            border: 1px solid #30363d;
            background-color: #161b22;
            color: #ffffff;
        }
        .metric-card {
            background-color: #161b22;
            border: 1px solid #30363d;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title Header & Description ---
st.title("🤖 Olist D2C Natural Language-to-SQL Assistant")
st.markdown("Query your Brazilian E-Commerce BigQuery data warehouse instantly using natural language.")
st.markdown("---")

# --- Sidebar Configuration & Interactive Prompts ---
with st.sidebar:
    st.header("⚙️ Configuration")
    groq_api_key = st.text_input("Enter Groq API Key:", type="password")
    
    st.markdown("---")
    st.markdown("### 💡 Quick Portfolio Prompts")
    st.markdown("*(Click an idea to copy or test)*")
    
    if "selected_prompt" not in st.session_state:
        st.session_state.selected_prompt = ""

    prompts = [
        "What are the top 5 product categories by total sales?",
        "Top 5 customer states by revenue & unique customers",
        "What is the average order delivery time?",
        "Payment type share breakdown (credit card, boleto, etc.)",
        "Monthly order volume and revenue trend for 2018"
    ]
    
    for p in prompts:
        if st.button(p, use_container_width=True):
            st.session_state.selected_prompt = p

    st.markdown("---")
    st.markdown("### 📊 Warehouse Status")
    st.markdown("🟢 **BigQuery**: Connected (`olist_warehouse`)")
    st.markdown("⚡ **LLM**: Groq (`qwen/qwen3.8-27b`)")

# --- Check API Key and Initialize Agent ---
if not groq_api_key:
    st.warning("⚠️ Please enter your free Groq API key in the sidebar to initialize the AI agent.")
else:
    try:
        db = get_db_connection()
        
        llm = ChatGroq(
            model="qwen/qwen3.8-27b", 
            groq_api_key=groq_api_key, 
            temperature=0
        )
        
        agent_executor = create_sql_agent(
            llm=llm,
            db=db,
            verbose=True,
            agent_type="zero-shot-react-description",
            agent_executor_kwargs={"handle_parsing_errors": True}
        )
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # --- Display Historical Messages & Persistent Expanders ---
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                if message["role"] == "assistant":
                    if "recommendations" in message:
                        with st.expander("💡 Strategic Business Recommendations"):
                            st.markdown(message["recommendations"])
                    if "summary" in message:
                        with st.expander("📊 View Data Extraction Summary"):
                            st.markdown(message["summary"])

        chat_placeholder = "Ask a data question..."
        prompt = st.chat_input(chat_placeholder)
        
        if st.session_state.selected_prompt:
            prompt = st.session_state.selected_prompt
            st.session_state.selected_prompt = ""

        if prompt:
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                with st.spinner("🔍 Inspecting schema, writing BigQuery SQL, and executing..."):
                    try:
                        response = agent_executor.run(prompt)
                        st.markdown(response)
                        
                        # Dynamically generate tailored strategic recommendations
                        with st.spinner("Generating strategic business insights..."):
                            recommendation_prompt = f"""
                            Based on this data query result: "{response}"
                            Provide 2 short, highly tailored strategic business or operational recommendations for an e-commerce platform like Olist. Keep it concise, specific, and actionable.
                            """
                            dynamic_recommendations = llm.invoke(recommendation_prompt).content

                        with st.expander("💡 Strategic Business Recommendations"):
                            st.markdown(dynamic_recommendations)

                        # Dynamically generate the Data Extraction Summary using the LLM
                        with st.spinner("Extracting query metadata..."):
                            summary_prompt = f"""
                            Based on the user's question "{prompt}" and the query result "{response}", provide a concise technical summary in bullet points covering:
                            - **Source Tables Queried:** (e.g. cleaned_orders, cleaned_customers, cleaned_order_items, etc. based on the data)
                            - **Warehouse Provider:** Google BigQuery (olist_warehouse)
                            - **Execution Type:** (e.g. Real-time multi-table relational join, time-series aggregation, grouping, etc.)
                            Keep it clean and formatted in markdown bullet points.
                            """
                            dynamic_summary = llm.invoke(summary_prompt).content

                        with st.expander("📊 View Data Extraction Summary"):
                            st.markdown(dynamic_summary)

                        # --- SAVE TO SESSION STATE ONCE (No duplication) ---
                        st.session_state.messages.append({
                            "role": "assistant", 
                            "content": response,
                            "recommendations": dynamic_recommendations,
                            "summary": dynamic_summary
                        })
                        
                    except Exception as e:
                        error_msg = f"An error occurred while executing the query: {e}"
                        st.error(error_msg)

    except Exception as e:
        st.error(f"Failed to connect to BigQuery database. Check your credentials: {e}")