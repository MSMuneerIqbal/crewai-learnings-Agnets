from crewai.flow.flow import Flow, start, listen
from litellm import completion

api_key = "api-key"
class CityFunFact(Flow):
    @start()
    def generate_random_city(self):
        result = completion(
            model="gemini/gemini-1.5-flash",
            api_key=api_key,
            messages=[{"content":"Return any random city name from pakistan except lahore.","role":"user"}])
        city=(result['choices'][0]['message']['content'])

        print(city)
        return city
    @listen(generate_random_city)
    def generate_fun_fact(self, city_name):
        result = completion(model="gemini/gemini-1.5-flash",
                            api_key=api_key,
                            messages=[{"content":f"write some fun fact about{city_name}",
                                       "role": "user"}])
        fun_fact = (result['choices'][0]['message']['content'])
        print(fun_fact)
        self.state['fun_fact'] = fun_fact
    @listen(generate_fun_fact)
    def save_fun_fact(self):
        with open("fun_fact.md", "w") as f:
            f.write(self.state['fun_fact'])
            return self.state['fun_fact']
        
def kickoff():
    obj = CityFunFact()
    result=obj.kickoff()
    print(result)
