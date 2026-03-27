from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class Step01Requirements():
    """Step 01 - Requirements Analysis"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def requirement_analyst(self) -> Agent:
        return Agent(config=self.agents_config['requirement_analyst'], verbose=True)

    @task
    def requirement_task(self) -> Task:
        return Task(
            config=self.tasks_config['requirement_task'],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential, verbose=True)
