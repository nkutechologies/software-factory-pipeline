from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class Step08Evaluation():
    """Step 08 - Code Evaluation"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def evaluation_engine(self) -> Agent:
        return Agent(config=self.agents_config['evaluation_engine'], verbose=True)

    @task
    def evaluation_task(self) -> Task:
        return Task(
            config=self.tasks_config['evaluation_task'],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential, verbose=True)
