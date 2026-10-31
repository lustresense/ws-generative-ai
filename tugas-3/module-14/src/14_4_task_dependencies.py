"""CrewAI Task with description, expected_output and context dependencies.
Reference: Python for Gen AI Complete Guide, Module 14, pages 157-159.
Execution: crew.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from crewai import Agent,Task
from common import crew_llm
llm=crew_llm()
researcher=Agent(role='Research Analyst',goal='Summarize provided background.',backstory='Accurate technical analyst.',llm=llm,max_iter=2,verbose=False)
writer=Agent(role='Technical Writer',goal='Explain a technical concept clearly.',backstory='Software documentation specialist.',llm=llm,max_iter=2,verbose=False)
reviewer=Agent(role='Reviewer',goal='Identify unclear claims.',backstory='Professional technical editor.',llm=llm,max_iter=2,verbose=False)
research=Task(description='Summarize this supplied fact: RAG retrieves relevant documents to support an LLM response.',expected_output='Two factual bullet points.',agent=researcher)
writing=Task(description='Turn the provided facts into a short beginner guide.',expected_output='A 100-word explanation.',agent=writer,context=[research])
review=Task(description='Review the guide and list one improvement.',expected_output='One concrete correction.',agent=reviewer,context=[writing])
for t in [research,writing,review]:
    ctx = t.context
    if ctx is None or (hasattr(ctx, '__class__') and ctx.__class__.__name__ == '_NotSpecified'):
        cnt = 0
    else:
        cnt = len(ctx)
    print(t.agent.role,'context_count=',cnt,'expected:',t.expected_output)
print('Task objects created. Run Module 14.5 to execute a crew.')
