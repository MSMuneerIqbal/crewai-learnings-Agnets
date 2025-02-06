from crewai.flow.flow import Flow, listen, start, router
import random
from litellm import completion
api_key = "api-key"

class RoutFlow(Flow):
    @start()
    def greetings(self):
        print("Assalam-O-Alaikum")
    @router(greetings)
    def select_city(self):
        cities = ["karachi","rawalpindi", "lahore"]
        city = random.choice(cities)
        if city == "karachi":
            return "karachi"
        if city == "rawalpindi":
            return "rawalpindi"
        if city == "lahore":
            return "lahore"
    @listen(select_city)
    def fun_city(self,city_select):
        result = completion(model="gemini/gemini-1.5-flash",
                            api_key=api_key,
                            messages=[{"content":f"write some fun fact about{city_select} city",
                                       "role": "user"}])
        fun_fact = (result['choices'][0]['message']['content'])
        print(fun_fact)
        #self.state['fun_fact'] = fun_fact       

def run3():
    obj = RoutFlow()
    obj.kickoff()

def plot3():
    obj = RoutFlow()
    obj.plot()