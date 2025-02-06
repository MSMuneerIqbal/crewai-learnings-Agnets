from crewai.flow.flow import Flow, listen, start, router
import random
class RoutFlow(Flow):
    @start()
    def greetings(self):
        print("Assalam-O-Alaikum")
    @router(greetings)
    def select_city(self):
        cities = ["karachi","islamabad", "lahore"]
        city = random.choice(cities)
        if city == "karachi":
            return "karachi"
        if city == "islamabad":
            return "islamabad"
        if city == "lahore":
            return "lahore"
    @listen(select_city)
    def fun_city(self,city):
        print(f"write some fun facts about the {city} city")

def kickoff():
    obj = RoutFlow()
    obj.kickoff()

def plot():
    obj = RoutFlow()
    obj.plot()