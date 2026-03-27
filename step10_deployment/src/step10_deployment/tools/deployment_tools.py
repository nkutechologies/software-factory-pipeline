import os
import subprocess
from typing import Type
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from pathlib import Path


class FileWriterInput(BaseModel):
    """Input for FileWriterTool."""
    file_path: str = Field(..., description="Relative path for the file to create (e.g., 'deploy/Dockerfile')")
    content: str = Field(..., description="The full content to write to the file")


class FileWriterTool(BaseTool):
    name: str = "file_writer"
    description: str = (
        "Writes content to a file on disk. Creates parent directories automatically. "
        "Use this to create deployment config files like Dockerfile, render.yaml, "
        "vercel.json, .env files, and shell scripts."
    )
    args_schema: Type[BaseModel] = FileWriterInput

    def _run(self, file_path: str, content: str) -> str:
        try:
            full_path = Path("output/deploy") / file_path
            full_path.parent.mkdir(parents=True, exist_ok=True)
            full_path.write_text(content, encoding="utf-8")
            if file_path.endswith('.sh'):
                full_path.chmod(0o755)
            return f"Successfully wrote file: {full_path}"
        except Exception as e:
            return f"Error writing file: {e}"


class ShellCommandInput(BaseModel):
    """Input for ShellCommandTool."""
    command: str = Field(..., description="The shell command to execute")
    working_dir: str = Field(
        default="output/deploy",
        description="Working directory for the command (relative to project root)"
    )


class ShellCommandTool(BaseTool):
    name: str = "shell_command"
    description: str = (
        "Executes a shell command and returns the output. Use this to run deployment "
        "commands like 'npx vercel deploy', 'npm install', 'git init', etc."
    )
    args_schema: Type[BaseModel] = ShellCommandInput

    def _run(self, command: str, working_dir: str = "output/deploy") -> str:
        blocked = ['rm -rf /', 'mkfs', 'dd if=', ':(){', 'fork bomb']
        for b in blocked:
            if b in command.lower():
                return f"Blocked: dangerous command detected"

        try:
            full_dir = Path(working_dir)
            full_dir.mkdir(parents=True, exist_ok=True)

            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=120,
                cwd=str(full_dir)
            )

            output = ""
            if result.stdout:
                output += f"STDOUT:\n{result.stdout}\n"
            if result.stderr:
                output += f"STDERR:\n{result.stderr}\n"
            output += f"Return code: {result.returncode}"
            return output if output.strip() else "Command completed (no output)"
        except subprocess.TimeoutExpired:
            return "Error: Command timed out after 120 seconds"
        except Exception as e:
            return f"Error: {e}"
