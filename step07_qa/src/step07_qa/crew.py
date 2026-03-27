from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class Step07Qa():
    """Step 07 - QA Engineering"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def qa_engineer(self) -> Agent:
        return Agent(config=self.agents_config['qa_engineer'], verbose=True)

    @task
    def qa_task(self) -> Task:
        return Task(
            config=self.tasks_config['qa_task'],
            output_file='../pipeline_data/07_tests.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential, verbose=True)
