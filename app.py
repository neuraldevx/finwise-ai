import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

# Access Hugging Face token from secrets
hf_token = st.secrets["HF_TOKEN"]

# Function to load the model using pipeline
@st.cache(allow_output_mutation=True)
def load_pipeline():
    model_id = "meta-llama/Meta-Llama-3-8B"
    pipe = pipeline("text-generation", model=model_id, use_auth_token=hf_token)
    return pipe

# Load the pipeline
pipe = load_pipeline()

# Ensure the pipeline is loaded successfully
if pipe is None:
    st.error("Failed to load the model pipeline.")
    st.stop()

# Streamlit interface
st.title("FinWise AI: Your AI-Powered Financial Advisor")

prompt = st.text_area("Enter your query:", "What are the best stocks to invest in today?")
if st.button("Get Financial Insights"):
    try:
        insights = pipe(prompt)
        st.write(insights[0]['generated_text'])
    except Exception as e:
        st.error(f"Error generating insights: {e}")
