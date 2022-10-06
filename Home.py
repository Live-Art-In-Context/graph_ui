import streamlit as st 
from ac_graph import AcGraph, AcNode, NamedAcNode
from integer_graph import InputNode, AddNode, ProductNode

# This is the entrypoint file > the first page Streamlit shows.

st.set_page_config(
  page_title="Live art in context",
  page_icon="🎨",
  layout="wide"
)

welcome_msg = "Welcome, the first thing you will want to do is create a node. Use the *New* page in the sidebar."

if 'graph' not in st.session_state:
    math_g = AcGraph("math")
    st.session_state['graph'] = math_g
    welcome_msg
else:
    math_g = st.session_state['graph']
    if len(math_g.node_list()) > 0:
        st.write("Your graph currently has %s following nodes:" % len(math_g.node_list()))
        for node in math_g.node_list():
            st.write("- Node %s is %s" %(node.id(), type(node)))
            for p in node.predecessors():
                st.write("    - %s is a prdecessor", p.id())
            for s in node.successors():
                st.write("    - %s is a successor", p.id())
    else:
        welcome_msg
