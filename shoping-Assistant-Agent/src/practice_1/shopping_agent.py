from crewai import Agent, Task, Crew, Process

class ShoppingAgentSystem:
    def __init__(self):
        # Initialize all agents
        self.product_researcher = self.create_product_researcher()
        self.price_analyst = self.create_price_analyst()
        self.review_analyst = self.create_review_analyst()
        self.deal_finder = self.create_deal_finder()
        self.recommendation_writer = self.create_recommendation_writer()

    def create_product_researcher(self):
        return Agent(
            role="Product Researcher",
            goal="Research and gather detailed information about products",
            backstory="""You are an experienced product researcher with extensive knowledge 
            of consumer goods. You excel at finding and comparing product specifications, 
            features, and capabilities across different brands and models.""",
            verbose=True
        )

    def create_price_analyst(self):
        return Agent(
            role="Price Analyst",
            goal="Analyze pricing trends and find the best value options",
            backstory="""You are a skilled price analyst who specializes in tracking price 
            histories, identifying pricing patterns, and determining the best time to buy. 
            You understand market dynamics and can predict price changes.""",
            verbose=True
        )

    def create_review_analyst(self):
        return Agent(
            role="Review Analyst",
            goal="Analyze customer reviews and feedback to assess product quality and reliability",
            backstory="""You are an expert in analyzing customer reviews and feedback. 
            You can identify genuine reviews, spot common issues, and determine overall 
            customer satisfaction levels for products.""",
            verbose=True
        )

    def create_deal_finder(self):
        return Agent(
            role="Deal Finder",
            goal="Find the best deals, discounts, and promotions",
            backstory="""You are a professional deal finder who excels at discovering 
            discounts, promotions, and special offers. You know how to compare prices 
            across different retailers and find the best value for money.""",
            verbose=True
        )

    def create_recommendation_writer(self):
        return Agent(
            role="Recommendation Writer",
            goal="Create comprehensive shopping recommendations",
            backstory="""You are a skilled writer who specializes in creating clear, 
            detailed, and well-structured shopping recommendations. You excel at 
            presenting complex information in an easy-to-understand format.""",
            verbose=True
        )

    def create_research_task(self, product_query):
        return Task(
            description=f"""Research the following product category: {product_query}
            1. Identify top products in the category
            2. Gather detailed specifications
            3. Compare features across different brands
            4. Note any significant advantages or disadvantages""",
            agent=self.product_researcher,
            expected_output="Detailed product research report with specifications and comparisons"
        )

    def create_price_analysis_task(self, research_results):
        return Task(
            description=f"""Analyze pricing for the researched products:
            {research_results}
            1. Track historical price trends
            2. Identify typical price ranges
            3. Determine value for money
            4. Predict potential price changes""",
            agent=self.price_analyst,
            expected_output="Price analysis report with trends and predictions"
        )

    def create_review_analysis_task(self, research_results):
        return Task(
            description=f"""Analyze customer reviews for the researched products:
            {research_results}
            1. Assess overall customer satisfaction
            2. Identify common praise points
            3. Note recurring issues or complaints
            4. Evaluate long-term reliability""",
            agent=self.review_analyst,
            expected_output="Customer review analysis with key findings"
        )

    def create_deal_finding_task(self, price_analysis):
        return Task(
            description=f"""Find the best current deals based on the price analysis:
            {price_analysis}
            1. Search for active discounts and promotions
            2. Compare prices across retailers
            3. Identify best value options
            4. Note any upcoming sales or promotions""",
            agent=self.deal_finder,
            expected_output="List of best current deals and upcoming promotions"
        )

    def create_recommendation_task(self, research_results, price_analysis, review_analysis, deals):
        return Task(
            description=f"""Create a comprehensive shopping recommendation based on:
            Research: {research_results}
            Pricing: {price_analysis}
            Reviews: {review_analysis}
            Deals: {deals}
            
            Include:
            1. Top product recommendations
            2. Price comparisons
            3. Best deals available
            4. Pros and cons
            5. Buying timing recommendations""",
            agent=self.recommendation_writer,
            expected_output="Complete shopping recommendation report"
        )

    def run_shopping_analysis(self, product_query):
        try:
            print(f"\n🔍 Researching products for: {product_query}")
            
            # Research Crew
            research_crew = Crew(
                agents=[self.product_researcher, self.price_analyst, self.review_analyst],
                tasks=[
                    self.create_research_task(product_query),
                    self.create_price_analysis_task("{{research_results}}"),
                    self.create_review_analysis_task("{{research_results}}")
                ],
                process=Process.sequential
            )
            research_results = research_crew.kickoff()
            print("\n✅ Research phase complete")

            # Deal Finding Crew
            deal_crew = Crew(
                agents=[self.deal_finder],
                tasks=[self.create_deal_finding_task(research_results)],
                process=Process.sequential
            )
            deal_results = deal_crew.kickoff()
            print("\n✅ Deal finding phase complete")

            # Recommendation Crew
            recommendation_crew = Crew(
                agents=[self.recommendation_writer],
                tasks=[self.create_recommendation_task(
                    research_results, 
                    research_results,  # Price analysis is part of research results
                    research_results,  # Review analysis is part of research results
                    deal_results
                )],
                process=Process.sequential
            )
            final_recommendation = recommendation_crew.kickoff()
            print("\n✅ Recommendation phase complete")

            # Save the recommendation
            print("\n💾 Saving shopping recommendation...")
            with open("shopping_recommendation.md", "w", encoding='utf-8') as f:
                f.write(str(final_recommendation))
            
            print("\n📋 Shopping recommendation has been saved to 'shopping_recommendation.md'")
            print("\n=== Recommendation Preview ===\n")
            print(str(final_recommendation))

            return final_recommendation

        except Exception as e:
            print(f"\n❌ Error during shopping analysis: {str(e)}")
            raise

def main():
    # Example usage
    shopping_system = ShoppingAgentSystem()
    product_query = "4K Smart TV under $1000"  # Example query
    shopping_system.run_shopping_analysis(product_query)

if __name__ == "__main__":
    main() 