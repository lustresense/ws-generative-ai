"""CrewAI sequential pipeline: researcher, writer, reviewer, with visible task output.
Reference: Python for Gen AI Complete Guide, Module 14, pages 159-161.
Execution: crew.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from crewai import Agent,Task,Crew,Process
from common import crew_llm
llm=crew_llm()
def agent(role,goal):return Agent(role=role,goal=goal,backstory='Precise technical specialist. Use only supplied context.',llm=llm,verbose=False,max_iter=2,allow_delegation=False)
a,b,c=[agent(*x) for x in [('Researcher','Extract factual points'),('Writer','Explain clearly'),('Reviewer','Find unsupported claims')]]
t1=Task(description='From these facts, summarize 2 takeaways: RAG retrieves documents before generation; embeddings represent meaning as vectors.',expected_output='2 factual points.',agent=a)
t2=Task(description='Write a 120 word developer explanation of the provided facts.',expected_output='Short Markdown guide.',agent=b,context=[t1])
t3=Task(description='Review technical accuracy without adding external facts.',expected_output='Short list of corrections or READY.',agent=c,context=[t2])
crew=Crew(agents=[a,b,c],tasks=[t1,t2,t3],process=Process.sequential,verbose=False,memory=False)
result=crew.kickoff();print('CREW RESULT:',str(result)[:900]);
for task in crew.tasks:print('Task:',task.agent.role,'Output:',str(task.output)[:250])
