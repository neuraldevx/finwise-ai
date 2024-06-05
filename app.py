import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import requests
import pandas as pd

# Load the model and tokenizer
@st.cache(allow_output_mutation=True)
def load_model():
    model_name = "meta-llama/LLaMA-3"
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer

model, tokenizer = load_model()

# Fetch stock data
def fetch_stock_data(ticker):
    api_key = "YOUR_API_KEY"
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

# Fetch financial news
def fetch_news():
    url = "YOUR_NEWS_API_URL"
    response = requests.get(url)
    data = response.json()
    return data

# Generate financial insights
def generate_insights(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Streamlit interface
st.title("FinWise AI: Your AI-Powered Financial Advisor")

st.sidebar.header("Input Options")
ticker = st.sidebar.text_input("Stock Ticker", "AAPL")
news_data = fetch_news()

if st.sidebar.button("Get Stock Data"):
    stock_data = fetch_stock_data(ticker)
    st.write(stock_data)

if st.sidebar.button("Get Financial Insights"):
    prompt = st.text_area("Enter your query:", "What are the best stocks to invest in today?")
    insights = generate_insights(prompt)
    st.write(insights)

st.header("Latest Financial News")
for article in news_data["articles"]:
    st.subheader(article["title"])
    st.write(article["description"])
    st.write(f"[Read more]({article['url']})")
