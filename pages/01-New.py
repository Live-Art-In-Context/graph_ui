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

with st.form("my_form"):
   node_type = st.selectbox("Node type", 
   ("Input", "Addition", "Product")
   )
   value = st.slider("Initial node value",0,25)
   submitted = st.form_submit_button("Create")
   if submitted:
        st.write("Creating %s node" % node_type)
        if node_type == "Input":
            InputNode(math_g, value)
        elif node_type == "Addition":
            AddNode(math_g)
        elif node_type == "Product":
            ProductNode(math_g)
