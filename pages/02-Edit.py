import streamlit as st 
import path
import sys

cwd = path.Path(__file__).abspath()
sys.path.append(cwd.parent.parent)
from graph_ui.ac_graph import AcGraph, AcNode, NamedAcNode
from graph_ui.integer_graph import InputNode, AddNode, ProductNode

# Get the graph from session
if 'graph' not in st.session_state:
    math_g = AcGraph("math")
    st.session_state['graph'] = math_g
else:
    math_g = st.session_state['graph']


st.selectbox("Node to edit", math_g.node_list())

"""What kind of edit?
Add prdecessor or add successor

**Predecessor**
Generate a list of all nodes that are currently available to add. (This might be non-trivial)"""