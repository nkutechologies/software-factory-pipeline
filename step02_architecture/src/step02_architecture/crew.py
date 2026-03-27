from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class Step02Architecture():
    """Step 02 - Architecture Design"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def architecture_agent(self) -> Agent:
        return Agent(config=self.agents_config['architecture_agent'], verbose=True)

    @task
    def architecture_task(self) -> Task:
        return Task(
            config=self.tasks_config['architecture_task'],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential, verbose=True)
