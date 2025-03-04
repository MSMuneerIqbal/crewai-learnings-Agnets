from crewai import Agent, Crew, Task, Process
from crewai_tools import SerperDevTool

class MarketAnalysisCrew:
    def __init__(self):
        self.serper_tool = SerperDevTool()
        self.market_analyst = self.create_market_analyst()
        self.research_analyst = self.create_research_analyst()
        self.data_collection_task = self.create_data_collection_task()
        self.analysis_task = self.create_analysis_task()

    def create_market_analyst(self) -> Agent:
        return Agent(
            role="Market Analyst",
            goal="Research and analyze projected market trends for 2025",
            backstory="""You are an experienced market analyst with 10+ years of experience in financial markets.
            You have a strong background in technical analysis and market psychology. Your expertise lies in 
            identifying market patterns and predicting future market movements. You are particularly skilled at
            analyzing long-term market trends and making forward-looking projections.""",
            verbose=True,
            tools=[self.serper_tool]
        )

    def create_research_analyst(self) -> Agent:
        return Agent(
            role="Research Analyst",
            goal="Conduct comprehensive research on future market drivers and opportunities for 2025",
            backstory="""You are a seasoned research analyst specializing in fundamental analysis and market research.
            You have extensive experience in analyzing economic indicators, company financials, and industry trends.
            Your research has helped numerous investors make informed decisions. You excel at identifying emerging
            trends and potential future market disruptions.""",
            verbose=True,
            tools=[self.serper_tool]
        )

    def create_data_collection_task(self) -> Task:
        return Task(
            description="""1. Research and collect data about projected market trends for 2025, including:
            - Emerging technologies and their potential market impact
            - Industry-specific growth projections
            - Demographic and consumer behavior changes
            - Regulatory and policy changes that might affect markets
            
            2. Identify key market drivers and potential disruptions
            
            3. Document significant predictions and forecasts from reliable sources
            
            4. Focus on long-term trends that could shape the market in 2025""",
            expected_output="""A detailed report containing:
            - Projected market trends for 2025
            - Key emerging technologies and their impact
            - Industry growth projections
            - Potential market disruptions
            - Sources and references for all data""",
            agent=self.market_analyst
        )

    def create_analysis_task(self) -> Task:
        return Task(
            description="""1. Analyze the market research data provided by the Market Analyst
            
            2. Research and evaluate:
            - Future economic indicators and their potential impact
            - Industry-specific growth opportunities
            - Emerging market segments
            - Potential risks and challenges
            
            3. Identify investment opportunities for 2025
            
            4. Provide strategic recommendations for long-term positioning
            
            5. Include specific sectors and technologies that show the most promise""",
            expected_output="""A comprehensive analysis report including:
            - Future market drivers and their impact
            - Risk assessment for 2025
            - Opportunity identification
            - Strategic recommendations for long-term investment
            - Specific sector and technology recommendations""",
            agent=self.research_analyst
        )

    def create_crew(self) -> Crew:
        return Crew(
            agents=[self.market_analyst, self.research_analyst],
            tasks=[self.data_collection_task, self.analysis_task],
            process=Process.sequential,
            verbose=True
        )

    def run(self):
        crew = self.create_crew()
        result = crew.kickoff()
        print("\n=== 2025 Market Analysis Report ===\n")
        print(result)
        # Save the result to a markdown file
        with open("market_analysis_2025.md", "w", encoding='utf-8') as f:
            f.write(str(result))
