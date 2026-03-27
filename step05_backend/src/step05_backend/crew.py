from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class Step05Backend():
    """Step 05 - Backend Development"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def backend_developer(self) -> Agent:
        return Agent(config=self.agents_config['backend_developer'], verbose=True)

    @task
    def backend_task(self) -> Task:
        return Task(
            config=self.tasks_config['backend_task'],
            output_file='../pipeline_data/05_backend.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential, verbose=True)
