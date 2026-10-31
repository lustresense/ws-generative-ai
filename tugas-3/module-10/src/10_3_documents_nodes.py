"""LlamaIndex Document, Node, SentenceSplitter and metadata.
Reference: Python for Gen AI Complete Guide, Module 10, pages 116-118.
Execution: offline.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from llama_index.core import Document
from llama_index.core.node_parser import SentenceSplitter
docs=[Document(text='LlamaIndex reads documents and converts content into nodes for search. '*3,metadata={'source':'intro'}),Document(text='Retrieval finds the most relevant nodes; synthesis composes an answer. '*3,metadata={'source':'retrieval'})]
parser=SentenceSplitter(chunk_size=64,chunk_overlap=10)
nodes=parser.get_nodes_from_documents(docs)
print('Documents:',len(docs),'Nodes:',len(nodes))
for node in nodes:print(node.node_id[:9],node.metadata,repr(node.text[:95]))
