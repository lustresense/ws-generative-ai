"""CrewAI hierarchical manager delegates to researcher and writer.
Reference: Python for Gen AI Complete Guide, Module 14, pages 161-163.
Execution: crew.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from crewai import Agent,Task,Crew,Process
from common import crew_llm
llm=crew_llm()
manager=Agent(role='Production Manager',goal='Delegate and check accuracy.',backstory='Experienced manager of short technical reports.',llm=llm,allow_delegation=True,verbose=False,max_iter=3)
researcher=Agent(role='Researcher',goal='Extract key facts.',backstory='Detail-oriented fact analyst.',llm=llm,verbose=False,max_iter=2)
writer=Agent(role='Writer',goal='Write simple AI explanations.',backstory='Technical documentation writer.',llm=llm,verbose=False,max_iter=2)
tasks=[Task(description='Summarize provided statement: embeddings represent text as numeric vectors.',expected_output='Two accurate key points.',agent=researcher),Task(description='Write a short readable explanation of embeddings, using only facts supplied.',expected_output='80-word paragraph.',agent=writer)]
crew=Crew(agents=[researcher,writer],tasks=tasks,manager_agent=manager,process=Process.hierarchical,verbose=False,memory=False)
print('Hierarchical result:',str(crew.kickoff())[:1000])
