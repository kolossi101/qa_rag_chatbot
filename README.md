# RAG-Enabled Q&A Chatbot

This project is a Retrieval-Augmented Generation (RAG) powered chatbot that provides accurate, contextually relevant answers based on a private knowledge base. Instead of relying solely on pretrained knowledge, the chatbot retrieves information from a custom textbook on biochemistry and cell biology genetics, making it a powerful study tool for students and researchers in these fields.

The system uses cutting-edge AI tools and libraries including LangChain, Pinecone, Hugging Face models, and Streamlit to deliver authoritative, domain-specific responses through a simple and intuitive web interface.

## Features

- Domain-Specific Q&A: Answers are based on a private collection of scientific documents, not just general LLM knowledge.

- RAG Pipeline: Combines retrieval from an external vector database with generative AI for enhanced accuracy and relevance.

- Streamlit Frontend: Clean, interactive interface for submitting queries and viewing detailed responses and source references.

- Modular Design: Separate components for document processing, embedding generation, vector storage, retrieval, and response generation.

- Efficient Information Retrieval: Quick similarity search powered by Pinecone's cloud-native vector database.

## How It Works

1. Document Processing:
   A textbook PDF is loaded, segmented into coherent chunks (~500 characters each), and slightly overlapped for better context preservation.

2. Embedding Creation:
   Each chunk is transformed into a dense vector representation using Hugging Face's all-MiniLM-L6-v2 model.

3. Vector Storage:
   The embeddings are stored in a Pinecone index, enabling fast similarity searches.

4. Query Handling:

   - When a user submits a question, it is embedded into a vector.
   - The system retrieves the most semantically similar chunks from Pinecone.
   - Retrieved context is combined with the user’s question.

5. Response Generation:
   - A system prompt and the retrieved context guide the LLM (Microsoft's Phi-4 model via Hugging Face API) to generate a targeted answer.
   - The chatbot outputs the answer along with the source documents used.

## Tech Stack

- LangChain: Build the RAG pipeline and retrieval chains
- Pinecon: Vector database for fast document retrieval
- Hugging Face (Phi-4, all-MiniLM-L6-v2): Embedding generation and language model responses
- Streamlit: Frontend for user interaction
- Python: Core application logic
- Jupyter Notebook: For experimentation and prototyping

## Setup Instructions

1.  **Create a Virtual Environment:**

    Open your terminal or command prompt and navigate to the project directory. Run the following command to create a virtual environment named `chatbot`:

    ```bash
    python -m venv chatbot
    ```

2.  **Select Python Interpreter in VS Code:**

    - Open the project in VS Code.
    - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS) to open the command palette.
    - Type "Python: Select Interpreter" and press Enter.
    - Select the Python interpreter from the `chatbot` virtual environment. It will typically be located at `.\chatbot\Scripts\python.exe` (Windows) or `./chatbot/bin/python` (macOS/Linux).

3.  **Bypass Execution Policy (Windows Only):**

    If you are using Windows, you might need to bypass the execution policy to run the activation script. Open PowerShell as an administrator and run:

    ```powershell
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
    ```

    **Note:** This command temporarily bypasses the execution policy for the current process. It is generally safe for setting up virtual environments.

4.  **Activate the Virtual Environment:**

    - **Windows:**

      ```bash
      .\chatbot\Scripts\activate
      ```

    - **macOS/Linux:**

      ```bash
      source chatbot/bin/activate
      ```

    Your terminal prompt should now indicate that the virtual environment is active (e.g., `(chatbot) C:\path\to\project>`).

5.  **Install Dependencies:**

    Install the required Python packages using `pip` from the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

6.  **(Optional) Recreate Pinecone Index:**

    If you want to create new Pinecone index (it is already created), run the following command:

    ```bash
    python store_index.py
    ```

    **Important:** This step requires that you have your Pinecone API key and environment variables properly set up. Also, make sure to change the name of the variable "index_name" for your new index.

7.  **Run the Application:**

    Start the Streamlit application by running:

    ```bash
    streamlit run app.py
    ```

    This will open the application in your default web browser.

## Acknowledgments

- Textbook sourced from the [Open Textbook Library](https://open.umn.edu/opentextbooks/textbooks/967).
- This project was developed as part of a software development course project exploring modern AI technologies and RAG architectures. The goal was to demonstrate practical skills in building intelligent, modular, and production-ready AI applications using Python ecosystems. Please see the report in the assets folder for more details.

---

**Author**: Nadiia Geras  
**Date**: March 26, 2025  
**Link**: [Live Application](https://appragchatbot-rwedmfwycmrvsun8yz4eiv.streamlit.app/)
