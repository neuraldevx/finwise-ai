# FinWise AI 🏆

FinWise AI is an AI-powered financial advisor built using the LLaMA 3 model from Meta and the Streamlit framework. This application provides users with financial insights and stock recommendations based on natural language queries.

## Overview

FinWise AI leverages the powerful capabilities of the LLaMA 3 model, a state-of-the-art language model optimized for dialogue use cases. The application allows users to input queries about stock market investments and receive detailed, AI-generated insights.

## Features

- **Natural Language Processing**: Understands and responds to user queries about stock market investments.
- **Real-Time Insights**: Provides up-to-date financial advice and stock recommendations.
- **Streamlit Integration**: Offers an interactive web-based interface for user queries and displaying results.
- **Secure Handling of API Keys**: Uses Hugging Face's secrets management for secure handling of API tokens.

## How to Use

1. **Input Your Query**: Enter a natural language query in the text area provided. For example, "What are the best stocks to invest in today?"
2. **Get Insights**: Click on the "Get Financial Insights" button to receive detailed, AI-generated advice and stock recommendations.

## Installation

To run this application locally, follow these steps:

1. **Clone the Repository**:

    ```bash
    git clone https://huggingface.co/spaces/neuraldevx/FinWise-AI
    cd FinWise-AI
    ```

2. **Set Up Environment Variables**:
   Add your Hugging Face token in the Hugging Face Spaces settings under the "Secrets" section with the name `HF_TOKEN`.

3. **Install Dependencies**:

    Ensure you have the necessary dependencies listed in `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**:

    ```bash
    streamlit run app.py
    ```

## Configuration

The application is configured using the following settings:

- **Title**: FinWise AI
- **Emoji**: 🏆
- **Color From**: Pink
- **Color To**: Pink
- **SDK**: Streamlit
- **SDK Version**: 1.35.0
- **App File**: app.py
- **Pinned**: False
- **License**: MIT

Check out the configuration reference at [Hugging Face Spaces Config Reference](https://huggingface.co/docs/hub/spaces-config-reference).

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Contact

For questions or comments about the model, please reach out through the model's repository on Hugging Face.

---

This project demonstrates the capabilities of the LLaMA 3 model from Meta and provides a foundation for building advanced financial advisory tools using AI.
