# Dynamic AI Agent with Web Search 🤖

This project implements an AI agent using LangGraph, designed to interact with users, leverage web search, and provide intelligent responses. It features a frontend built with Streamlit, a backend powered by FastAPI, and utilizes both Groq and OpenAI language models. The agent can be configured with a system prompt, and users can select their preferred model and provider.

## 🚀 Key Features

- **Interactive UI:** A user-friendly interface built with Streamlit for easy interaction with the AI agent.
- **Model Selection:** Choose between Groq and OpenAI models based on your needs.
- **Web Search Integration:** Option to enable web search using the Tavily API for up-to-date information.
- **Customizable System Prompt:** Define the behavior of the AI agent with a custom system prompt.
- **Backend API:** A FastAPI backend handles requests, validates data, and interacts with the AI agent.
- **LangGraph Agent:** Utilizes LangGraph to create a robust and configurable AI agent workflow.
- **Asynchronous operation:** Uses asynchronous calls to the LLMs to improve performance.

## 🛠️ Tech Stack

- **Frontend:**
    - Streamlit: UI framework
    - requests: For making HTTP requests to the backend
- **Backend:**
    - FastAPI: Web framework for creating the API
    - Pydantic: Data validation and settings management
    - Uvicorn: ASGI server for running the FastAPI application
- **AI Agent:**
    - LangGraph: Framework for building conversational agents
    - Groq: Language model provider
    - OpenAI: Language model provider
    - Tavily: Search API
    - Langchain: LLM integration and tooling
- **General:**
    - Python: Programming language
    - dotenv: For managing environment variables

## 📦 Getting Started

### Prerequisites

- Python 3.7+
- API keys for Groq, OpenAI, and Tavily (if you want to use web search)

### Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  Create a virtual environment (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Set up environment variables:

    - Create a `.env` file in the root directory.
    - Add your API keys to the `.env` file:

    ```
    GROQ_API_KEY=your_groq_api_key
    OPENAI_API_KEY=your_openai_api_key
    TAVILY_API_KEY=your_tavily_api_key
    ```

    *(Note: While the code includes `dotenv`, it's commented out. Ensure you properly configure environment variables in your deployment environment.)*

### Running Locally

1.  Start the backend:

    ```bash
    python backend.py
    ```

    This will start the FastAPI server on `http://127.0.0.1:9999`.

2.  Start the frontend:

    ```bash
    streamlit run frontend.py
    ```

    This will open the Streamlit UI in your browser.

## 💻 Usage

1.  Open the Streamlit UI in your browser.
2.  Enter a system prompt to define the behavior of the AI agent.
3.  Select the desired model provider (Groq or OpenAI).
4.  Choose a specific model from the dropdown.
5.  Enable web search if needed.
6.  Enter your query in the text input field.
7.  Click the "Ask Agent!" button to get the AI agent's response.

## 📂 Project Structure

```
├── ai_agent.py      # Defines the AI agent logic using LangGraph
├── backend.py       # FastAPI backend for handling API requests
├── frontend.py      # Streamlit frontend for user interaction
├── .env             # Environment variables (API keys)
├── README.md        # This file
└── requirements.txt # Project dependencies
```

## 📸 Screenshots
 
 

 
## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Submit a pull request.

## 📝 License

This project is licensed under the [MIT License](LICENSE).

## 📬 Contact

If you have any questions or suggestions, feel free to contact me at [tusharkamthe23@gmail.com](mailto: tusharkamthe23@gmail.com).

## 💖 Thanks Message

Thanks for checking out this LangGraph AI Agent project! I hope it's helpful and inspires you to build amazing things.


