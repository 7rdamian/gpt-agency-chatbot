# AI-Powered Internal Documentation Assistant

This is a web application that helps GPT Agency employees ask questions about company documents. It uses AI to read documents and answer questions.

## What it does

- Reads all .txt files from a documents folder when you start the app
- Stores the document information in a database 
- Lets users ask questions on a web page
- Uses AI to give answers based on the documents

## How to use it

### Step 1: Get the code
```bash
git clone https://github.com/7rdamian/gpt-agency-chatbot.git
cd gpt-agency-chatbot
```

### Step 2: Install Python packages
```bash
pip install -r requirements.txt
```

### Step 3: Add your documents
Put your .txt files in the docs/ folder. The app will read all of them automatically.

### Step 4: Create a together.ai free account
- Go to https://www.together.ai and create a free account
- Go to their list of models and pick "Llama-3.3-70B-Instruct-Turbo-Free"
- Copy your api key and paste it into a .env file inside the project folder like this: TOGETHER_API_KEY=[your-api-key-here]

### Step 5: Run the app
```bash
python main.py
```

### Step 6: Use it
- Open your web browser
- Go to http://127.0.0.1:5000
- Type your question in the box
- Click Submit

## What you need
- Python 3.7 or newer
- Internet connection (for downloading AI models)
- Text files with your company documents

## Technology used
- Python, Flask - for the web server
- LangChain - for connecting everything together
- ChromaDB - for storing document information
- Together.ai - for the AI that answers questions
- HuggingFace - for understanding the documents
