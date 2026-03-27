from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class Step06Frontend():
    """Step 06 - Frontend Development"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def frontend_developer(self) -> Agent:
        return Agent(config=self.agents_config['frontend_developer'], verbose=True)

    @task
    def frontend_task(self) -> Task:
        return Task(
            config=self.tasks_config['frontend_task'],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential, verbose=True)
