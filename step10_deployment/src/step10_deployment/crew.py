from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from step10_deployment.tools.deployment_tools import FileWriterTool, ShellCommandTool


@CrewBase
class Step10Deployment():
    """Step 10 - Deployment"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def deployment_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['deployment_agent'],
            verbose=True,
            tools=[FileWriterTool(), ShellCommandTool()]
        )

    @task
    def deployment_task(self) -> Task:
        return Task(
            config=self.tasks_config['deployment_task'],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential, verbose=True)
