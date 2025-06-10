# Capstone Project

This is a simple Python-based text completion app that uses the [Cohere API](https://cohere.com/) to generate creative responses to user prompts. Designed for experimentation with generative AI, it's perfect for generating stories, summaries, or kid-friendly explanations.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/text-completion-app.git
cd text-completion-app
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv ml_env
source ml_env/bin/activate  # Mac/Linux
# or
ml_env\Scripts\activate  # Windows
```

### 3. Install Dependencies

```bash
pip install cohere
```

### 4. Get a Cohere API Key
Sign up at https://cohere.com <br>
Generate an API key from your Cohere dashboard

### 5. Add Your API Key
Initialize the client with your key in the Python script:
```bash
import cohere
co = cohere.Client('your-api-key-here')
```

## Usage

Run the app in your terminal:
```bash
python text_completion_app.py
```
You’ll be prompted to enter your message:
```bash
Enter a prompt (or 'quit' to exit): Explain recursion like I’m five.
```
