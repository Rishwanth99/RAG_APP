# AI-Powered RAG Question Answering Application

This project is a Retrieval-Augmented Generation (RAG) application that uses a Large Language Model (LLM) to answer questions about the Social Studies curriculum for 10th standard students. The application is built using Python, Streamlit, LangChain, and Google's Gemini Pro.

## Features

*   **Question Answering:** Ask questions about the Social Studies 10th standard curriculum and get answers from the LLM.
*   **Retrieval-Augmented Generation:** The application retrieves relevant information from a PDF document (`TM_Social_EM.pdf`) to provide more accurate and context-aware answers.
*   **Web Interface:** The application provides a simple and intuitive web interface built with Streamlit.
*   **Powered by Gemini Pro:** The application uses Google's Gemini Pro model for question answering.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.7 or higher
*   Pip (Python package installer)

### Installation

1.  Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/RAG_APP.git
    ```

2.  Navigate to the project directory:

    ```bash
    cd RAG_APP
    ```

3.  Install the required Python packages:

    ```bash
    pip install -r rag_poc/req.txt
    ```

### Configuration

1.  Create a `.env` file in the root directory of the project.

2.  Add your Google Generative AI API key to the `.env` file:

    ```
    GEMINI_API_KEY="YOUR_API_KEY"
    MODEL_GEMINI="gemini-pro-latest"
    ```

### Running the Application

1.  Run the Streamlit application:

    ```bash
    streamlit run rag_poc/data.py
    ```

2.  Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

## Usage

1.  Once the application is running, you will see a chat interface.
2.  Type your question in the chat input box and press Enter.
3.  The application will generate a response based on the information in the PDF document.

## Project Structure

```
RAG_APP/
├── .env
├── .git/
├── rag_poc/
│   ├── data.py
│   ├── list_models.py
│   ├── req.txt
│   └── TM_Social_EM.pdf
└── README.md
```

*   **`.env`**: This file contains the environment variables for the project, such as the Google Generative AI API key.
*   **`rag_poc/data.py`**: This is the main application file that contains the Streamlit code and the RAG pipeline.
*   **`rag_poc/list_models.py`**: This is a utility script that lists the available Google Generative AI models.
*   **`rag_poc/req.txt`**: This file contains the list of Python packages required for the project.
*   **`rag_poc/TM_Social_EM.pdf`**: This is the PDF document that contains the information used by the RAG pipeline.
*   **`README.md`**: This file contains the documentation for the project.
