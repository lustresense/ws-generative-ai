"""Exercise 2: Developer, Security Reviewer, Performance Reviewer and Lead.
Reference: Python for Gen AI Complete Guide, Module 14, pages 163.
Execution: crew.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from crewai import Agent,Task,Crew,Process
from common import crew_llm
llm=crew_llm()
def ag(r,g):return Agent(role=r,goal=g,backstory='Python code reviewer. Return specific actionable findings.',llm=llm,max_iter=2,verbose=False)
roles=[('Developer','Explain code purpose'),('Security Reviewer','Find security risks'),('Performance Reviewer','Find bottlenecks'),('Lead','Consolidate review')]
agents=[ag(*r) for r in roles]
code="import requests\ndef fetch(url):\n    return requests.get(url).text\n"
tasks=[Task(description=f'Analyze this code for {title}:\n{code}',expected_output='2 concise findings.',agent=a) for title,a in zip(['correctness','security','performance'],agents[:3])]
lead=Task(description='Merge all reviews into an actionable report and give safe fixes.',expected_output='Merged review with priorities.',agent=agents[3],context=tasks)
result=Crew(agents=agents,tasks=tasks+[lead],process=Process.sequential,memory=False,verbose=False).kickoff()
print('Final review:',str(result)[:1300])
