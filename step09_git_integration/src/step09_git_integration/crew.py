from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class Step09GitIntegration():
    """Step 09 - Git Integration"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def git_integration_agent(self) -> Agent:
        return Agent(config=self.agents_config['git_integration_agent'], verbose=True)

    @task
    def git_integration_task(self) -> Task:
        return Task(
            config=self.tasks_config['git_integration_task'],
            output_file='../pipeline_data/09_pull_request.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential, verbose=True)
