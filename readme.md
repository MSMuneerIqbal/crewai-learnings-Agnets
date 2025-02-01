# [Crew AI](https://www.crewai.com/)

CrewAI is an open-source Python framework designed to facilitate the development and management of multi-agent AI systems. By enabling the orchestration of AI agents, CrewAI allows developers to build complex, collaborative workflows where agents assume specific roles and work together to achieve common objectives. This role-based architecture enhances the efficiency and effectiveness of AI-driven processes. 

A significant advancement in CrewAI's capabilities is the introduction of **Flows**. Flows provide a structured, event-driven framework for creating and managing AI workflows, allowing developers to seamlessly connect multiple tasks, manage state, and control execution flow within AI applications. This feature simplifies the development of sophisticated AI automations by enabling the chaining of tasks and the coordination of multiple agents, referred to as Crews. 

**Key Features of CrewAI Flows:**

- **Simplified Workflow Creation:** Flows enable the easy chaining of multiple Crews and tasks to create complex AI workflows. 

- **State Management:** Flows facilitate the management and sharing of state between different tasks within a workflow, ensuring consistency and coherence throughout the execution process. 

- **Event-Driven Architecture:** Built on an event-driven model, Flows allow for dynamic and responsive workflows that can adapt to changing conditions and inputs. 

- **Flexible Control Flow:** Developers can implement conditional logic, loops, and branching within workflows, providing the flexibility needed to handle complex decision-making processes. 

The introduction of Flows represents a significant evolution in CrewAI's architecture, offering a more organized and efficient approach to task management. By simulating traditional organizational hierarchies, Flows enable a manager agent to coordinate workflows, delegate tasks, and validate outcomes, leading to streamlined and effective execution. 

In summary, CrewAI, with the integration of Flows, provides a robust framework for building sophisticated AI workflows. Its event-driven architecture and state management capabilities make it an excellent choice for developing scalable, maintainable AI systems that can adapt to evolving requirements.  

## Should we start using workflows in CrewAI going forward?

Yes, it seems likely that Flows will become the preferred method for creating workflows in CrewAI over time, especially as they offer more flexibility, event-driven design, and scalability compared to the old way of doing things.

Why Flows Might Become the Standard way of doing things

	1.	Dynamic Capabilities: Flows allow tasks to be triggered by events or specific conditions, which is more adaptive than the linear or parallel structure of Pipelines.
	2.	State Management: Flows manage both structured and unstructured states efficiently, making them more robust for complex, interconnected workflows.
	3.	Future Updates: As CrewAI evolves, new features and optimizations are more likely to focus on Flows, gradually making them the standard tool.


Transition Period

For now, CrewAI supports both Flows and old way of doing things, so developers can transition gradually. You can use Pipelines for simpler tasks while adopting Flows for more complex, dynamic workflows. Over time, Flows are expected to become the go-to tool for CrewAI.

Recommendation

If you’re learning or planning projects with CrewAI, it’s wise to start focusing on Flows while keeping Pipelines in mind for legacy systems. This way, you’ll future-proof your skills and workflows!


[Amazing NEW CrewAI Feature for AI Agents...FLOW Explained](https://www.youtube.com/watch?v=EEzpeJqvb_w)

[Official Documentation](https://docs.crewai.com/introduction)

[Flows Documentation](https://docs.crewai.com/concepts/flows)

# UV, litellm and  CrewAi  Setup
Welcome to the repository for GloProg (GloVersity) Class 08, held on -- / -- / ----. ion.  

## 📌 Table of Contents
1. [PowerShell Setup](#powershell-setup)  
2. [UV Basics](#uv-basics)  
3. [Creating and Managing Projects](#creating-and-managing-projects)  
4. [Adding Dependencies](#adding-dependencies)  
5. [Working with LiteLLM](#working-with-litellm)  
6. [Understanding Python Decorators](#understanding-python-decorators)  
7. [CrewAI Installation & Setup](#crewai-installation--setup)  
8. [Running CrewAI Workflow](#running-crewai-workflow)  

---

## ⚡ PowerShell Setup  
To begin, run the following command to install UV:  
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
Check if UV is installed correctly:  
```sh
uv version
uv help
```

---

## 🎯 UV Basics
Initialize a new project:  
```sh
uv init my-project
code .
```
Open the terminal and navigate into the project folder:  
```sh
cd .\my-project\
uv run hello.py
```
Modify `hello.py`, rerun the script, and observe changes:  
```sh
uv run hello.py
```

---

## 📦 Adding Dependencies  
Install additional packages:  
```sh
uv add numpy pandas
```
Verify the dependencies in the `pyproject.toml` file.  

---

## 🚀 Creating and Managing Projects  
Create another project:  
```sh
uv init --package another-project
```
Return to VS Code and check the `pyproject.toml` file.  
Navigate to `src/` and create `hello.py`:
```python
def my_function():
    print("Hello from my_function()")
```
Now, add a new command in `pyproject.toml`:  
```toml
gloprog = "another_project.hello:my_function"
```
Run the command from the terminal:  
```sh
uv run gloprog
```
Install the package in editable mode:  
```sh
pip install -e .
```

---

## 🔥 Working with LiteLLM  
Initialize a new project:  
```sh
uv init --package litellm-project
cd litellm-project
```
Add the LiteLLM dependency:  
```sh
uv add litellm
uv venv
```
Activate the virtual environment:  
```sh
.venv\Scripts\activate   # Windows
source .venv/bin/activate   # macOS/Linux
```
Now make hello.py in SRC folder. 

```python
from litellm import completion
import os

os.environ["OPENAI_API_KEY"] = "ADD YOUR API KEY"
os.environ["GEMINI_API_KEY"] = "ADD YOUR API KEY"

def openai():
    response = completion(
        model="openai/gpt-4o",
        messages=[{"content": "Hello, how are you?", "role": "user"}]
    )
    print(response)

def gemini():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{"content": "Hello, how are you?", "role": "user"}]
    )
    print(response)

def gemini2():
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        messages=[{"content": "Hello, how are you?", "role": "user"}]
    )
    print(response)
```
Add your API key and run:  
```sh
uv run gemini
```

---

## 🧠 Understanding Python Decorators  
**Python decorators** are functions that modify the behavior of another function without changing its structure.  
Example:  
```python
def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, world!")

say_hello()
```
Try running this in **Google Colab** to experiment with decorators.

---

## 🤖 CrewAI Installation & Setup  
To install CrewAI, follow these steps:

### Step 1: Install Microsoft C++ Build Tools  
Download from [Visual Studio Official Site](https://visualstudio.microsoft.com/visual-cpp-build-tools/).  

### Step 2: During Installation, Select:  
✅ MSVC v142 or later  
✅ Windows 10 SDK  
✅ C++ CMake tools for Windows  

Restart your system after installation.

### Step 3: Upgrade Pip & Install CrewAI  
```sh
pip install --upgrade pip setuptools wheel
pip install crewai
```
If using a virtual environment:  
```sh
.venv\Scripts\activate   # Windows
source .venv/bin/activate   # macOS/Linux
```
If installation issues occur:  
```sh
pip install hnswlib
pip install crewai
```
Verify installation:  
```sh
crewai version
```

---

## ⚙️ Running CrewAI Workflow  
Create a new CrewAI workflow:  
```sh
crewai create flow crew_flow
dir
```
Open the project in **VS Code** and edit `.env`:  
```env
OPENAI_API_KEY= (Replace with GEMINI_API_KEY)
MODEL=gemini/gemini-1.5-flash
```
Run the CrewAI script:  
```sh
uv run kickoff
```

---

## 🎯 Conclusion  
This revision guide covered:
- Setting up **UV**, **LiteLLM**, and **CrewAI**  
- Running Python scripts and managing dependencies  
- Understanding **Python decorators**  
- Configuring API keys and virtual environments  

🚀 **Keep practicing, and happy coding!** 🚀

---





