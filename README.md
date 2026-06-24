# AI Agent Toolkit

A modular Python repository designed to demonstrate the implementation of specialized, interactive automation tools. This project focuses on clean code structure and error handling, separating distinct functionalities into dedicated agents.

## Core Architecture

The toolkit is designed to be multi-agent, meaning each task has its own independent script. This approach ensures the code is easy to maintain and expand.

### 1. Math Tool Agent (`math_agent.py`)
The first component of the toolkit is an interactive command-line agent that processes math calculations safely and efficiently.

* **Basic Arithmetic:** Supports multi-number addition, subtraction, multiplication, and division.
* **Advanced Math:** Computes powers, square roots, and factorials.
* **Geometry Features:** Computes the total area of a circle using the radius.
* **Input Validation:** Features built-in safeguards to catch errors like division by zero or negative square roots without crashing the program.

### 2. Upcoming Agents
* **System Agent:** Will focus on local system tasks and file management automation.
* **Web Agent:** Will focus on fetching and processing data from online sources.

## Technology Stack
* **Language:** Python 3
* **Core Modules:** `math`

## How to Setup and Run

1. Clone or download this repository to your local computer.
2. Open your terminal or Anaconda Prompt.
3. Change your directory to the folder containing the scripts:
   ```bash
   cd AI_Agents
