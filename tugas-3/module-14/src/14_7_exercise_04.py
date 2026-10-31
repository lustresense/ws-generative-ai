"""Exercise 4: sequential versus hierarchical crew timing and qualitative comparison.
Reference: Python for Gen AI Complete Guide, Module 14, pages 163.
Execution: crew.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from crewai import Agent,Task,Crew,Process
from common import crew_llm
from time import perf_counter
llm=crew_llm()
def create(mode):
    a=Agent(role='Researcher',goal='Collect evidence',backstory='Careful analyst',llm=llm,max_iter=2)
    b=Agent(role='Writer',goal='Write concise text',backstory='Technical writer',llm=llm,max_iter=2)
    c=Agent(role='Reviewer',goal='Check claims',backstory='Accuracy reviewer',llm=llm,max_iter=2)
    manager=Agent(role='Manager',goal='Delegate tasks and check outputs',backstory='Production coordinator',llm=llm,allow_delegation=True,max_iter=2)
    t1=Task(description='Explain that RAG retrieves external documents.',expected_output='Two bullets.',agent=a)
    t2=Task(description='Write a short paragraph about the two bullets.',expected_output='One paragraph.',agent=b,context=[t1])
    t3=Task(description='Find any unsupported statement in the paragraph.',expected_output='Review status.',agent=c,context=[t2])
    args=dict(agents=[a,b,c],tasks=[t1,t2,t3],process=mode,memory=False,verbose=False)
    if mode==Process.hierarchical:args['manager_agent']=manager
    return Crew(**args)
for mode in (Process.sequential,Process.hierarchical):
    crew=create(mode);start=perf_counter();out=crew.kickoff();elapsed=perf_counter()-start
    print(mode.value,'seconds:',round(elapsed,2),'output:',str(out)[:450])
print('Comparison is one run per workflow; evaluate correctness against source before declaring quality winner.')
