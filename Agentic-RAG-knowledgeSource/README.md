# CrewAI User Information Agent

This project demonstrates how to create a simple AI agent using CrewAI that can answer questions about a user based on provided information. The agent uses the Gemini 2.0 Flash model from Google and retrieves information using a string knowledge source.

## Overview

The application creates an agent that:
1. Stores information about a user (Muneer Iqbal)
2. Utilizes RAG (Retrieval-Augmented Generation) capabilities to answer questions about the user
3. Accesses this information through CrewAI's knowledge source mechanism

## Prerequisites

- Python 3.8+
- Google Gemini API key

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/username/crewai-user-info.git
   cd crewai-user-info
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install crewai google-generativeai
   ```

## Configuration

Set your Google Gemini API key as an environment variable:

```bash
# On Windows
set GEMINI_API_KEY=your_api_key_here

# On macOS/Linux
export GEMINI_API_KEY=your_api_key_here
```

## Usage

Run the script:

```bash
python main.py
```

The script will:
1. Initialize a knowledge source with information about Muneer Iqbal
2. Create an agent with access to this knowledge
3. Set up a task to answer questions about the user
4. Run the agent and display the results

## Customization

You can modify the user information by changing the `content` variable:

```python
content = "Your custom user information here..."
```

Change the question by modifying the input to the `kickoff` method:

```python
result = crew.kickoff(inputs={"question": "your custom question here"})
```

## How It Works

1. The script creates a StringKnowledgeSource containing information about the user
2. An agent is created with this knowledge source attached
3. A task is defined that prompts the agent to answer questions about the user
4. The CrewAI crew executes the task using the sequential process
5. The agent retrieves relevant information from the knowledge source to answer the question

## Troubleshooting

If you encounter errors:

- Ensure your Gemini API key is correctly set as an environment variable
- Check that you have the latest versions of the required packages
- Verify that the embedder configuration matches the requirements of your Google API key

## License

[MIT License](LICENSE)