from pathlib import Path

import streamlit as st
import yaml
from code_editor import code_editor
from streamlit_flow import streamlit_flow
from streamlit_flow.interfaces import StreamlitFlowEdge, StreamlitFlowNode

_DEFAULT_STEPS_FILE = Path(__file__).parent / "steps" / "steps_collection.yml"

steps_collection = yaml.safe_load(_DEFAULT_STEPS_FILE.read_text())
step_names = list(steps_collection.keys())

st.set_page_config(layout="wide")

def add_popup(element):
    if element not in st.session_state.step_details:
        st.session_state.step_details.append(element)

def generate_code(nodes, edges):
    code = '''
from patchwork.logger import logger
from patchwork.step import Step
from patchwork.steps import (
'''

    for node in nodes:
        if node.id != "0":
            code += node.data["label"]
            code += "\n"
    
    code += ")\n"
    code += '''
class MyPatchFlow(Step):
    def __init__(self, inputs: dict):
        self.inputs = inputs
'''
    node_id_codelist = []
    init_inputs = set()
    for node in step_nodes:
        node_code = f'''
        outputs_{node.id} = '''
        node_code += node.data["label"] + "(self.inputs).run()\n" 
        if node.id != "0":
            # print(node.id)
            node_id_codelist.append({"id": node.id, "code": node_code})
        init_inputs.update(node.data["inputs"])
        init_inputs -= set(node.data["outputs"])
    
    for input in init_inputs:
        code += f'''
        # Uncomment and initialize if needed
        # self.inputs["{input}"] = 
'''
    code += '''
    def run(self) -> dict:
'''

    edges_done = []
    
    source = "0"
    
    while(len(edges) != len(edges_done)):
        for edge in edges:
            # print(edge.id)
            if edge.source is source and edge.id not in edges_done:
                node_code = [node["code"] for node in node_id_codelist if node["id"] == edge.source]
                if node_code:
                    code += node_code[0]
                    code += f'''
        self.inputs.update(outputs_{edge.source})'''
        
                source = edge.target
                edges_done.append(edge.id)
                
                if len(edges) == len(edges_done):
                    node_code = [node["code"] for node in node_id_codelist if node["id"] == edge.target]
                    if node_code:
                        code += node_code[0]
                        code += f'''
        self.inputs.update(outputs_{edge.target})'''        

    code += '''
        return self.inputs
'''
    return code

options = st.multiselect("Choose the steps to create your patchflow", step_names)

c1, c2, c3 = st.columns(3)
with c1:
    create = st.button("Generate Patchflow", use_container_width=True)
with c2:
    clear = st.button("Reset Patchflow", use_container_width=True)
with c3:
    run = st.button("Run Patchflow", use_container_width=True)

col1, col2 = st.columns([1, 3])

if "step_details" not in st.session_state:
    st.session_state.step_details = []

if "step_edges" not in st.session_state:
    st.session_state.step_edges = []

with col1:
    for element in st.session_state.step_details:
        step_json = {
            "type": element["elementType"] + element["id"] + " - " + element["data"]["label"],
            "inputs": element["data"]["inputs"],
            "outputs": element["data"]["outputs"],
        }
        st.json(step_json)

with col2:
    step_nodes = []
    i = 0
    x = 200
    y = 100

    start_node = StreamlitFlowNode(
        id=str(i),
        pos=(x, y),
        data={
            "label": "Start",
            "inputs": [],
            "outputs": [],
        },
        style = {
        "backgroundColor": "red",
        "color": "white",
        "fontWeight": "bold",
        }
    )
   
    step_nodes.append(start_node)
    
    for step in options:
        i += 1

        node = StreamlitFlowNode(
            id=str(i),
            pos=(x, y),
            data={
                "label": step,
                "inputs": steps_collection.get(step).get("inputs"),
                "outputs": steps_collection.get(step).get("outputs") or [],
            },
            style = {
            "backgroundColor": "#1d976c",
            "color": "white",
            "fontWeight": "bold",
            }
        )
        step_nodes.append(node)
        y += 100

    element = streamlit_flow(
        nodes=step_nodes,
        edges=[],
        animate_new_edges=True,
        fit_view=True,
        get_node_on_click=True,
        get_edge_on_click=True,
        direction="right",
    )

if clear:
    st.session_state.step_details = []
    st.session_state.step_edges = []
    
elif create:
    # streamlit_flow(nodes=step_nodes, edges=st.session_state.step_edges, show_controls=False, fit_view=True)
    code_editor(code=generate_code(step_nodes, st.session_state.step_edges))

elif element:
    if element["elementType"] == "node":
        # print(element)
        add_popup(element)
    else:
        outputs = []
        inputs = []

        for node in step_nodes:
            if node.id == element["source"]:
                outputs = node.data["outputs"]
            if node.id == element["target"]:
                inputs = node.data["inputs"]

        intersection = [option for option in outputs if option in inputs]
        if len(intersection) > 0 or element["source"] == '0':
            st.success("Connected")
            edge = StreamlitFlowEdge(
                id=element["source"] + "-" + element["target"], source=element["source"], target=element["target"]
            )
            e = [e for e in st.session_state.step_edges if e.id == edge.id]
            if not e:
                st.session_state.step_edges.append(edge)
        else:
            st.error("outputs of source step don't overlap with inputs of target step")
        # print(element)