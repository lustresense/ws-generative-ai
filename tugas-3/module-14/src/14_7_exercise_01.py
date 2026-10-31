"""Exercise 1: three-agent blog content pipeline on fine-tuning versus RAG.
Reference: Python for Gen AI Complete Guide, Module 14, pages 163.
Execution: crew.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from crewai import Agent,Task,Crew,Process
from common import crew_llm
llm=crew_llm()
def make(r,g):return Agent(role=r,goal=g,backstory='An accurate technical writer, using only provided knowledge.',llm=llm,max_iter=2,verbose=False)
r,o,w=[make('Researcher','Extract facts'),make('Outline Writer','Create structure'),make('Full Writer','Create article')]
t1=Task(description='Extract facts about RAG vs fine-tuning. Facts: RAG retrieves external context; fine-tuning updates weights; both have different costs.',expected_output='Four concise fact bullets.',agent=r)
t2=Task(description='Outline a practical guide based on research, with 3 headings.',expected_output='Markdown outline.',agent=o,context=[t1])
t3=Task(description='Write a 180-word article using the outline, no unsupported claims.',expected_output='Final Markdown blog post.',agent=w,context=[t2])
print(str(Crew(agents=[r,o,w],tasks=[t1,t2,t3],process=Process.sequential,memory=False,verbose=False).kickoff())[:1600])
