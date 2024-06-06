import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import os

# Access Hugging Face token from secrets
hf_token = st.secrets["HF_TOKEN"]

# Function to load the model
@st.cache(allow_output_mutation=True)
def load_model():
    model_id = "meta-llama/Meta-Llama-3-8B"
    model = AutoModelForCausalLM.from_pretrained(model_id, use_auth_token=hf_token)
    tokenizer = AutoTokenizer.from_pretrained(model_id, use_auth_token=hf_token)
    return model, tokenizer

model, tokenizer = load_model()

# Function to generate financial insights
def generate_insights(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Streamlit interface
st.title("FinWise AI: Your AI-Powered Financial Advisor")

prompt = st.text_area("Enter your query:", "What are the best stocks to invest in today?")
if st.button("Get Financial Insights"):
    insights = generate_insights(prompt)
    st.write(insights)
