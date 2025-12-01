from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

import subprocess


class RunTerminalToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    command: str = Field(..., description="The command to run(such as python app.py")

class RunTerminalTool(BaseTool):
    name: str = "Run Terminal Tool"
    description: str = (
        "This tool for run a command in terminal. such as run python script"
    )
    args_schema: Type[BaseModel] = RunTerminalToolInput

    def _run(self, command: str) -> str:
        subprocess.Popen(f'start cmd /k {command}"', shell=True)
        return "Terminal ran successfully"

