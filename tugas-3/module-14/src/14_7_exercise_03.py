"""Exercise 3: custom CrewAI WebSearchTool wrapping MOCK search, wired to Researcher.
Reference: Python for Gen AI Complete Guide, Module 14, pages 163.
Execution: crew.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from typing import Type
from pydantic import BaseModel,Field
from crewai.tools import BaseTool
from crewai import Agent,Task,Crew,Process
from common import crew_llm
class SearchInput(BaseModel):query:str=Field(description='Search topic')
class WebSearchTool(BaseTool):
    name:str='Mock Web Search';description:str='Look up fixed locally supplied workshop research facts. Not connected to live internet.'
    args_schema:Type[BaseModel]=SearchInput
    def _run(self,query:str)->str:
        return f'Mock search for {query}: RAG retrieves documents before response generation; embeddings convert text to vectors.'
tool=WebSearchTool();print('Tool direct check:',tool._run('RAG'))
researcher=Agent(role='Researcher',goal='Summarize mock search results with attribution.',backstory='Use Mock Web Search before giving answers.',llm=crew_llm(),tools=[tool],verbose=False,max_iter=3)
task=Task(description='Use Mock Web Search tool to investigate RAG and report exactly two facts. Cite as mock results.',expected_output='Two facts sourced to the mock tool.',agent=researcher)
crew=Crew(agents=[researcher],tasks=[task],process=Process.sequential,verbose=False,memory=False)
print('Research:',str(crew.kickoff())[:750]);print('Tool was supplied and explicitly requested; inspect logs to verify actual model tool invocation.')
