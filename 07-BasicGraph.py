import streamlit as st 

st.set_page_config(
  page_title="This page runs a simple graph",
  page_icon="📉",
  layout="wide"
)

import path
import sys

cwd = path.Path(__file__).abspath()
sys.path.append(cwd.parent.parent)

# st.write(sys.path)
from UiStreamlit.ac_graph import AcGraph, AcNode, NamedAcNode

"Hi there. We're going to make a basic graph"

with st.echo():
  demo_g = AcGraph("demo")
  node1 = AcNode(demo_g)
  st.write(node1.id())
  node2 = AcNode(demo_g)
  node3 = AcNode(demo_g)

"So who's present in node2's list?"
for node in node2.node_list():
  st.write("- Node %s here!" % node.id())

"And who's present in node3's list?"
for node in node3.node_list():
  st.write("- Node %s here!" % node.id())

"Actually, the graph is also maintaining the node list too."
for node in demo_g.node_list():
  st.write("- Node %s here, bitches!" % node.id())

"# Statefulness"
"Unfortunately, we didn't save anything into state above. So the first block of code does nothing."
with st.echo():
  for node in node3.predecessors():
    st.write("- Node %s is a predecessor of node3." % node.id())

  node3.add_predecessor(node2)

"But after it's been added within this script..."
with st.echo():
  for node in node3.predecessors():
    st.write("- Node %s is a predecessor of node3." % node.id())