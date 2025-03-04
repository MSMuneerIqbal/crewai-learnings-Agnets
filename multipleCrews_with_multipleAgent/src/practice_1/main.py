from crewai import Agent, Task, Crew, Process

#  Crew 1: Research Team (Collects Market Data)
researcher = Agent(
    role="Web Researcher",
    goal="Gather market data from news sources and reports.",
    backstory="You are a web researcher who is responsible for gathering market data from news sources and reports.",
    verbose=True
)

social_analyst = Agent(
    role="Social Media Analyst",
    goal="Analyze market trends on social media.",
    backstory="You are a social media analyst who is responsible for analyzing market trends on social media.",
    verbose=True
)

research_task1 = Task(
    description="Collect the latest market trends from news and financial reports.",
    expected_output="A summary of the latest market trends.",
    agent=researcher
)

research_task2 = Task(
    description="Analyze trending topics on social media related to market changes.",
    expected_output="A report on social media trends impacting the market.",
    agent=social_analyst
)

research_crew = Crew(
    agents=[researcher, social_analyst],
    tasks=[research_task1, research_task2],
    process=Process.sequential  # ✅ Both agents collect data at the same time
)


#  Crew 2: Analysis Team (Uses Research Crew Output)
data_scientist = Agent(
    role="Data Scientist",
    goal="Analyze market trends and extract key insights.",
    backstory="You are a data scientist who is responsible for analyzing market trends and extracting key insights.",
    verbose=True
)

market_strategist = Agent(
    role="Market Strategist",
    goal="Develop strategies based on market trends.",
    backstory="You are a market strategist who is responsible for developing strategies based on market trends.",
    verbose=True
)

def analyze_market(research_results):
    """Generate a task that uses the research results as input."""
    return Task(
        description=f"Analyze the following research findings and identify key insights: {research_results}",
        expected_output="A structured analysis report with key insights.",
        agent=data_scientist
    )

def strategy_development(analysis_results):
    """Generate a task that builds strategies based on analysis."""
    return Task(
        description=f"Based on the analysis: {analysis_results}, create a market strategy.",
        expected_output="A market strategy document.",
        agent=market_strategist
    )


#  Crew 3: Report Writing Team (Uses Analysis Crew Output)
financial_writer = Agent(
    role="Financial Writer",
    goal="Create a professional market report based on analysis.",
    backstory="You are a financial writer who is responsible for creating a professional market report based on analysis.",
    verbose=True
)

editor = Agent(
    role="Editor",
    goal="Proofread and refine the final report.",
    backstory="You are an editor who is responsible for proofreading and refining the final report.",
    verbose=True
)

def write_market_report(strategy_results):
    """Generate a writing task using the market strategy as input."""
    return Task(
        description=f"Write a detailed market report based on the strategy document: {strategy_results}",
        expected_output="A well-structured financial report on market trends.",
        agent=financial_writer
    )

def edit_market_report(report_results):
    """Generate an editing task to finalize the report."""
    return Task(
        description=f"Proofread and edit the following market report: {report_results}",
        expected_output="A polished, publication-ready market analysis report.",
        agent=editor
    )

def main():
    try:
        # Run Research Crew
        print("\n🔎 Running Research Crew...")
        research_results = research_crew.kickoff()
        print("\n✅ Research Phase Complete")

        # Run Analysis Crew
        print("\n📊 Running Analysis Crew with Research Data...")
        analysis_crew = Crew(
            agents=[data_scientist, market_strategist],
            tasks=[analyze_market(research_results), strategy_development(research_results)],
            process=Process.sequential  # ✅ First analyze, then develop strategy
        )
        analysis_results = analysis_crew.kickoff()
        print("\n✅ Analysis Phase Complete")

        # Run Report Writing Crew
        print("\n📝 Running Report Writing Crew with Analysis Data...")
        writing_crew = Crew(
            agents=[financial_writer, editor],
            tasks=[write_market_report(analysis_results), edit_market_report(analysis_results)],
            process=Process.sequential  # ✅ First writing, then editing
        )
        final_report = writing_crew.kickoff()
        print("\n✅ Writing Phase Complete")

        # Save the report
        print("\n💾 Saving Final Report...")
        with open("market_analysis_report.md", "w", encoding='utf-8') as f:
            f.write(str(final_report))
        
        print("\n📄 Final Market Analysis Report has been saved to 'market_analysis_report.md'")
        print("\n=== Report Preview ===\n")
        print(str(final_report))
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        raise

if __name__ == "__main__":
    main()
