import os
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool

def check_serper_api_key():
    """Check if SERPER_API_KEY is set in environment variables."""
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key:
        raise ValueError(
            "SERPER_API_KEY not found in environment variables. "
            "Please set it using:\n"
            "Windows (PowerShell): $env:SERPER_API_KEY='your_api_key'\n"
            "Windows (CMD): set SERPER_API_KEY=your_api_key\n"
            "Linux/Mac: export SERPER_API_KEY=your_api_key"
        )
    return api_key

def main():
    try:
        # Check for API key first
        check_serper_api_key()

        # Initialize a search tool
        search_tool = SerperDevTool()

        # Initialize the agent with advanced options
        agent = Agent(
            role='Research Analyst',
            goal='Provide up-to-date market analysis',
            backstory='An expert analyst with a keen eye for market trends.',
            tools=[search_tool],
            memory=True,
            verbose=True,
            max_rpm=None,
            max_iter=25,
        )

        # Create a task
        task = Task(
            description="Research and analyze the latest news on AI",
            agent=agent,
            expected_output="A comprehensive summary of the latest AI news, including key developments, trends, and their potential impact on the industry."
        )

        # Create a crew
        crew = Crew(
            agents=[agent],
            tasks=[task],
            verbose=True
        )

        # Execute the crew
        result = crew.kickoff()
        
        # Print the result
        print(result)

    except Exception as e:
        print(f"Error: {str(e)}")
        print("\nTo use this script, you need to:")
        print("1. Sign up at https://serper.dev/")
        print("2. Get your API key from the dashboard")
        print("3. Set the SERPER_API_KEY environment variable")
        print("4. Run the script again")

if __name__ == "__main__":
    main()