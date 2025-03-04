from crewai import Agent, Task, Crew, Process

def create_research_crew():
    # 🚀 Crew 1: Research Team
    researcher = Agent(
        role="AI Research Analyst",
        goal="Find and analyze the latest AI trends and developments",
        backstory="""You are an experienced AI research analyst with a strong background in 
        machine learning and emerging technologies. You have spent years tracking AI developments
        and can identify significant trends and breakthroughs.""",
        verbose=True
    )
    
    research_task = Task(
        description="""Research and analyze the latest AI advancements, focusing on:
        1. Breakthrough technologies and innovations
        2. Industry adoption trends
        3. Major research developments
        4. Potential impact on various sectors""",
        agent=researcher,
        expected_output="A comprehensive summary of current AI trends and their implications."
    )

    return Crew(
        agents=[researcher],
        tasks=[research_task],
        process=Process.sequential
    )

def create_analysis_crew(research_results):
    # 🚀 Crew 2: Analysis Team
    analyst = Agent(
        role="Strategic AI Analyst",
        goal="Analyze AI trends and provide strategic insights",
        backstory="""You are a strategic analyst specializing in AI technology impact assessment.
        Your expertise lies in understanding how AI developments affect different industries and
        predicting future trends.""",
        verbose=True
    )
    
    analysis_task = Task(
        description=f"""Analyze the following research findings and provide strategic insights:
        {research_results}
        
        Focus on:
        1. Market impact assessment
        2. Industry-specific implications
        3. Future growth projections
        4. Potential challenges and opportunities""",
        agent=analyst,
        expected_output="A detailed strategic analysis of AI trends and their market impact."
    )

    return Crew(
        agents=[analyst],
        tasks=[analysis_task],
        process=Process.sequential
    )

def create_writing_crew(analysis_results):
    # 🚀 Crew 3: Writing Team
    writer = Agent(
        role="Technical Report Writer",
        goal="Create a professional and comprehensive AI trends report",
        backstory="""You are a skilled technical writer with expertise in creating clear,
        engaging reports about complex technological topics. You excel at making technical
        information accessible to diverse audiences.""",
        verbose=True
    )
    
    writing_task = Task(
        description=f"""Create a detailed, well-structured report based on the analysis:
        {analysis_results}
        
        The report should include:
        1. Executive Summary
        2. Current AI Landscape
        3. Key Trends and Developments
        4. Industry Impact Analysis
        5. Future Outlook
        6. Recommendations""",
        agent=writer,
        expected_output="A professional, comprehensive report on AI market trends and developments."
    )

    return Crew(
        agents=[writer],
        tasks=[writing_task],
        process=Process.sequential
    )

def main():
    # Execute research crew
    research_crew = create_research_crew()
    research_results = research_crew.kickoff()
    print("\n🔍 Research Phase Complete\n")

    # Execute analysis crew
    analysis_crew = create_analysis_crew(research_results)
    analysis_results = analysis_crew.kickoff()
    print("\n📊 Analysis Phase Complete\n")

    # Execute writing crew
    writing_crew = create_writing_crew(analysis_results)
    final_report = writing_crew.kickoff()
    
    print("\n📄 Final AI Trends Report:\n")
    print(final_report)

    # Save the final report to a file
    with open("ai_trends_report.md", "w", encoding='utf-8') as f:
        f.write(str(final_report))
    
    print("\n💾 Report saved to ai_trends_report.md\n")

if __name__ == "__main__":
    main()
