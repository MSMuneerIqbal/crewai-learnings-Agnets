from practice_1.crew import MarketAnalysisCrew  # Import the Market Analysis Crew class

def run():
    """Function to initialize and run the Market Analysis Crew."""
    crew_instance = MarketAnalysisCrew()  # Create an instance of the Market Analysis Crew
    crew_instance.run()  # Execute the Crew workflow

if __name__ == "__main__":
    run()  # Run normally if executed directly
