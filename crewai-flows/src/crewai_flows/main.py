from crewai.flow.flow import Flow, start, listen
import time
class simpleflow(Flow):

    @start()
    def function1(self):
        print("Function 1 executed")
        time.sleep(3)
    @listen(function1)
    def function2(self):
        print("Function 2 executed")
        time.sleep(3)
    @listen(function2)
    def function3(self):
        print("Function 3 executed")
        time.sleep(3)

def kickoff():
    obj = simpleflow()
    obj.kickoff()