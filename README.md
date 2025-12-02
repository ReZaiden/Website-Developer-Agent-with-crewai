# 🤖 AI Python Developer Agent with CrewAI

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![CrewAI](https://img.shields.io/badge/CrewAI%5Btools%5D-1.6.0-brightgreen)
![Gradio](https://img.shields.io/badge/Gradio-Interactive%20UI-orange)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-purple)

An **AI-powered Python development agent** that generates complete Python applications based on your requirements.\
Powered by **CrewAI**, **OpenAI**, **Gradio**, and a fully **modular multi-agent architecture**.

> ⚠️ **Note:** This project is built for development and testing.\
> For production, ensure secure API keys, HTTPS, and proper rate limiting.

## 🚀 Features

-   🧠 **Multi-Agent System** with specialized roles (Engineering Lead, Backend Engineer, Frontend Engineer, Service Runner)\
-   📝 **Automated Design** generation from high-level requirements\
-   💻 **Python Code Generation** with clean, efficient implementation\
-   🎨 **Gradio UI Generation** for instant prototypes and demos\
-   ▶️ **Automatic Service Runner** to launch generated applications\
-   🔧 **Terminal Tool Integration** for command execution\
-   📚 **YAML-based Configuration** for agents and tasks

## 🧠 Tech Stack

| Technology       | Version  | Description                        |
|------------------|----------|------------------------------------|
| **Python**       | 3.10+    | Core language                      |
| **CrewAI**       | 1.6.0    | Multi-agent orchestration framework|
| **OpenAI API**   | GPT-4o   | LLM for code generation            |
| **Gradio**       | 6.0.1+   | Interactive UI framework           |
| **Hatchling**    | Latest   | Build system                       |

## ⚙️ Prerequisites

Before running the project, ensure you have:

-   🐍 **Python 3.10+**\
-   📦 **pip** or **uv** (recommended)\
-   🌐 **Git**\
-   🔑 **OpenAI API key**

## 🛠️ Installation

```bash
git clone https://github.com/ReZaiden/Python-Developer-Agent-with-crewai.git
cd Python-Developer-Agent-with-crewai
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e .
```

Or using **uv** (faster):

```bash
uv sync
```

## 🗝️ Edit .env file

1. Rename `.env.sample` file to `.env`
2. Add your OpenAI API key:

```env
MODEL=gpt-4o-mini
OPENAI_API_KEY=your_openai_api_key_here
```

## ▶️ Run the Project

### Using Gradio UI:

```bash
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
python src/project/app.py
```

Then go to http://localhost:11228/

### Using CLI:

```bash
python -m project
```

Or:

```bash
run_crew
```

## 📡 How It Works

1.  **User provides requirements** → Describe what Python application you need\
2.  **Engineering Lead** → Creates detailed design with classes and methods\
3.  **Backend Engineer** → Writes clean Python implementation code\
4.  **Frontend Engineer** → Builds a Gradio UI to demonstrate the backend\
5.  **Service Runner** → Launches the generated application\
6.  **Output saved** → All files saved in `output/{module_name}/`

## 🧩 Project Structure

```plaintext
src/
└── project/
    ├── __init__.py
    ├── app.py              # Gradio web interface
    ├── crew.py             # CrewAI agents and crew setup
    ├── main.py             # CLI entry point
    ├── config/
    │   ├── agents.yaml     # Agent configurations
    │   └── tasks.yaml      # Task definitions
    └── tools/
        ├── __init__.py
        └── run_terminal.py # Terminal execution tool
output/                     # Generated applications (created during execution)
pyproject.toml              # Project configuration
.env.sample                 # Environment variables template
```

## 🤖 Agents

| Agent              | Role                                    |
|--------------------|-----------------------------------------|
| Engineering Lead   | Designs the application architecture    |
| Backend Engineer   | Implements Python code                  |
| Frontend Engineer  | Creates Gradio UI                       |
| Service Runner     | Runs the generated application          |

## 🔒 Security Notes

-   Keep API keys inside `.env`\
-   Never commit `.env` to version control\
-   Use safe code execution mode for untrusted inputs

## 💡 Future Improvements

-   [ ] Add more specialized agents\
-   [ ] Support for multiple programming languages\
-   [ ] Database integration for project history\
-   [ ] Enhanced error handling and validation

## 🧑‍💻 Author

**Developed by:** ReZaiden\
💼 **GitHub:** [@ReZaiden](https://github.com/ReZaiden)\
📧 **Contact:** rezaidensalmani@gmail.com
