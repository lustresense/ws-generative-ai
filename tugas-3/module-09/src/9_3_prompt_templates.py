"""ChatPromptTemplate and MessagesPlaceholder with history.
Reference: Python for Gen AI Complete Guide, Module 09, pages 103-104.
Execution: offline.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
prompt=ChatPromptTemplate.from_messages([('system','You are a {role}. Answer in {language}.'),('human','{question}')])
print(prompt.format_messages(role='Python tutor',language='English',question='What is a decorator?'))
hist=ChatPromptTemplate.from_messages([('system','Context: {context}'),MessagesPlaceholder('history'),('human','{input}')])
print(hist.format_messages(context='User studies RAG',history=[HumanMessage(content='What is retrieval?'), AIMessage(content='Finding relevant content.')],input='How is it used in RAG?'))
