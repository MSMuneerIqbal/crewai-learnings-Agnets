from crewai import Agent, Task, Crew, Process, LLM
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
import os

# Get the GEMINI API key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Create a knowledge source
content = "Hello! I'm Muneer Iqbal, a graduate in Artificial Intelligence from The Islamia University of Bahawalpur (GPA: 3.48/4), Class of July 2024. My academic journey and hands-on projects have provided me with a strong foundation in Machine Learning (ML), Deep Learning (DL), Generative AI, and Exploratory Data Analysis (EDA)."
string_source = StringKnowledgeSource(
    content=content,
)

# Create an LLM with a temperature of 0 to ensure deterministic outputs
gemini_llm = LLM(
    model="gemini/gemini-2.0-flash",
    api_key=GEMINI_API_KEY,
    temperature=0,
)

# Configure embedder once to reuse
embedder_config = {
    "provider": "google",
    "config": {
        "model": "models/text-embedding-004",
        "api_key": GEMINI_API_KEY,
    }
}

# Create an agent with the knowledge store
agent = Agent(
    role="About User",
    goal="You know everything about the user.",
    backstory="""You are a master at understanding people and their preferences. when user ask any thing then you will assume he asking aobut the user that data you have in you knowledge souce""",
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm,
    knowledge_sources=[string_source],  # Explicitly assign the knowledge source to the agent
    embedder=embedder_config
)

task = Task(
    description="Answer the following questions about the user: {question}. Use the provided knowledge sources to answer questions about Muneer Iqbal.",
    expected_output="An answer to the question based on the provided context.",
    agent=agent,
    # Removed the incorrect context parameter
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True,
    process=Process.sequential,
    knowledge_sources=[string_source],  # Keep this for crew-level access
    embedder=embedder_config
)

def run():  
    result = crew.kickoff(inputs={"question": "in which year he completed his graduation"})
    print(result)

if __name__ == "__main__":
    run()