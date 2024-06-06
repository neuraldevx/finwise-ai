import streamlit as st
from transformers import pipeline
import os

# Access Hugging Face token from secrets
hf_token = st.secrets["HF_TOKEN"]

# Function to load the model using pipeline
@st.cache(allow_output_mutation=True)
def load_pipeline():
    model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
    try:
        pipe = pipeline(
            "text-generation",
            model=model_id,
            model_kwargs={"torch_dtype": "auto"},
            device="cuda",
            use_auth_token=hf_token
        )
        return pipe
    except Exception as e:
        st.error(f"Error loading model pipeline: {e}")
        return None

# Load the pipeline
pipe = load_pipeline()

# Ensure the pipeline is loaded successfully
if pipe is None:
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
