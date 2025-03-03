# CrewAI Project

A demonstration of CrewAI framework for orchestrating AI agents to work together as a crew.

## Overview

This project demonstrates how to use the CrewAI framework to create a team of AI agents that collaborate to research and produce content about artificial intelligence and AI agents. The crew consists of three agents:

1. **Researcher** - Conducts thorough research on AI topics
2. **Writer** - Creates compelling content based on research
3. **Project Manager** - Oversees the crew and ensures high-quality completion of tasks

## Installation

```bash
# Clone the repository
git clone https://github.com/MSMuneerIqbal/crewai-learnings-Agnets/tree/main/manager_agent.git
cd crewai-project

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install the required packages
pip install crewai
```

## Usage

The main script creates a crew with a hierarchical process flow where the Project Manager coordinates the efforts of the Researcher and Writer to complete the assigned task.

```bash
# Run the script
python main.py
```

## Project Structure

- `main.py` - The main script that defines the agents, tasks, and crew
- `README.md` - This file

## How It Works

1. The script defines three agents: a Researcher, a Writer, and a Project Manager.
2. A task is created to generate a list of article ideas about AI and AI agents.
3. The crew is instantiated with a hierarchical process, with the Project Manager overseeing the Researcher and Writer.
4. When the script runs, the Manager delegates work to the Researcher and Writer as needed to complete the task.
5. The final output is a list of 5 article ideas, each with a sample paragraph and notes.

## Example Output

The output will include 5 numbered bullet points, each with a captivating paragraph about an AI-related topic and accompanying notes for potential full articles.

## Customization

You can customize this project by:
- Modifying the agent roles and goals
- Changing the task description
- Adding more agents to the crew
- Creating more complex workflows with additional tasks

## Dependencies

- CrewAI library

## License

[Your chosen license]