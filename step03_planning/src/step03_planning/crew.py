from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class Step03Planning():
    """Step 03 - Task Planning"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def planning_agent(self) -> Agent:
        return Agent(config=self.agents_config['planning_agent'], verbose=True)

    @task
    def planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['planning_task'],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential, verbose=True)
