from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class Step04Database():
    """Step 04 - Database Engineering"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def database_engineer(self) -> Agent:
        return Agent(config=self.agents_config['database_engineer'], verbose=True)

    @task
    def database_task(self) -> Task:
        return Task(
            config=self.tasks_config['database_task'],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential, verbose=True)
