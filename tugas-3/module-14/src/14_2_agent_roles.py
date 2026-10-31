"""CrewAI roles and backstories with custom OpenAI-compatible 9Router LLM.
Reference: Python for Gen AI Complete Guide, Module 14, pages 153-154.
Execution: crew.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from crewai import Agent
from common import crew_llm
llm=crew_llm()
agents=[Agent(role='AI Research Analyst',goal='Collect accurate facts from provided context.',backstory='Careful technical analyst who distinguishes evidence from inference.',llm=llm,verbose=False,allow_delegation=False,max_iter=2),Agent(role='Technical Writer',goal='Write concise technical guides.',backstory='Writer who makes complex AI topics understandable.',llm=llm,verbose=False,allow_delegation=False,max_iter=2),Agent(role='Quality Reviewer',goal='Review completeness and factual support.',backstory='Editor who checks claims and suggests fixes.',llm=llm,verbose=False,allow_delegation=False,max_iter=2)]
for a in agents:print('Agent role:',a.role,'goal:',a.goal)
print('Agents constructed, no network call required for this example.')
