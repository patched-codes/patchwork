import sys
import json
from PyQt6.QtWidgets import (QApplication, QMainWindow, QGraphicsView, QGraphicsScene, 
                             QGraphicsItem, QGraphicsRectItem, QGraphicsTextItem, 
                             QGraphicsLineItem, QWidget, QHBoxLayout, QVBoxLayout, 
                             QListWidget, QPushButton, QInputDialog, QMessageBox, QLabel,
                             QStatusBar, QScrollArea, QLineEdit, QFormLayout, QFileDialog)
from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtGui import QPen, QColor, QBrush, QPainter, QFont
import networkx as nx

class Step(QGraphicsRectItem):
    def __init__(self, name, id, inputs, outputs, x, y, color=QColor(200, 255, 200)):
        self.name = name
        self.id = id
        self.unique_name = f"{name}_{id}"
        self.inputs = inputs
        self.outputs = outputs
        self.user_assigned_inputs = {}  # New dictionary to store user-assigned input values

        # Create text item to measure its size
        self.text_item = QGraphicsTextItem(self.unique_name)
        self.text_item.setFont(QFont("Arial", 16))
        text_rect = self.text_item.boundingRect()

        # Set rectangle size based on text size with some padding
        width = max(100, text_rect.width() + 20)
        height = max(50, text_rect.height() + 20)

        super().__init__(0, 0, width, height)
        self.setPos(x, y)
        self.setBrush(QBrush(color))
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setZValue(1)

        # Position the text in the center of the rectangle
        self.text_item.setParentItem(self)
        self.text_item.setPos(10, 10)
        self.text_item.setDefaultTextColor(Qt.GlobalColor.black)

    def paint(self, painter, option, widget=None):
        super().paint(painter, option, widget)
        if self.isSelected():
            painter.setPen(QPen(Qt.GlobalColor.red, 2))
            painter.drawRect(self.boundingRect())

class Edge(QGraphicsLineItem):
    def __init__(self, source, target):
        super().__init__()
        self.source = source
        self.target = target
        self.setPen(QPen(Qt.GlobalColor.white, 2))
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.setZValue(0)
        self.update_position()

    def update_position(self):
        source_center = self.source.sceneBoundingRect().center()
        target_center = self.target.sceneBoundingRect().center()
        self.setLine(source_center.x(), source_center.y(), target_center.x(), target_center.y())

    def paint(self, painter, option, widget=None):
        if self.isSelected():
            painter.setPen(QPen(Qt.GlobalColor.red, 3))
        else:
            painter.setPen(QPen(Qt.GlobalColor.white, 2))
        painter.drawLine(self.line())

class WorkflowScene(QGraphicsScene):
    def __init__(self, steps_data, main_window):
        super().__init__()
        self.steps_data = steps_data
        self.main_window = main_window
        self.steps = {}
        self.edges = []
        self.graph = nx.DiGraph()
        self.selected_step = None
        self.step_counter = {}
        self.setSceneRect(QRectF(0, 0, 800, 600))
        self.setBackgroundBrush(QColor(50, 50, 50))

    def add_step(self, name, data, x, y):
        if name not in self.step_counter:
            self.step_counter[name] = 0
        self.step_counter[name] += 1
        id = self.step_counter[name]
        step = Step(name, id, data['inputs'], data['outputs'], x, y)
        self.addItem(step)
        self.steps[step.unique_name] = step
        self.graph.add_node(step.unique_name)

    def mousePressEvent(self, event):
        clicked_item = self.itemAt(event.scenePos(), self.views()[0].transform())
        
        # Clear previous selections
        for scene_item in self.items():
            scene_item.setSelected(False)
        
        if clicked_item is None:
            self.selected_step = None
            self.main_window.clear_io_display()
            self.main_window.update_status("No item selected")
            return

        # Find the top-level item (Step or Edge)
        while clicked_item and not isinstance(clicked_item, (Step, Edge)):
            clicked_item = clicked_item.parentItem()

        if clicked_item is None:
            self.main_window.update_status("Clicked on an unknown area")
            return

        clicked_item.setSelected(True)
        
        if isinstance(clicked_item, Step):
            if self.selected_step is None:
                self.selected_step = clicked_item
                self.main_window.update_io_display()
                self.main_window.update_status(f"Step '{clicked_item.unique_name}' selected")
            elif self.selected_step == clicked_item:
                self.selected_step = None
                self.main_window.clear_io_display()
                self.main_window.update_status(f"Step '{clicked_item.unique_name}' unselected")
            else:
                if self.validate_connection(self.selected_step, clicked_item):
                    edge = Edge(self.selected_step, clicked_item)
                    self.addItem(edge)
                    self.edges.append(edge)
                    self.graph.add_edge(self.selected_step.unique_name, clicked_item.unique_name)
                    self.main_window.update_status(f"Edge created: {self.selected_step.unique_name} -> {clicked_item.unique_name}")
                else:
                    self.main_window.update_status("Invalid connection: Output types don't match input types")
                
                self.selected_step = None
                self.main_window.clear_io_display()
        elif isinstance(clicked_item, Edge):
            self.main_window.clear_io_display()
            self.selected_step = None
            self.main_window.update_status("Edge selected")
        else:
            self.selected_step = None
            self.main_window.clear_io_display()
            self.main_window.update_status("Unknown item selected")

        self.update()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        for edge in self.edges:
            edge.update_position()

    def keyPressEvent(self, event):
        print(f"Key pressed: {event.key()}")
        if event.key() in [Qt.Key.Key_Delete, Qt.Key.Key_Backspace]:
            print("Delete key pressed")
            items_to_remove = list(self.selectedItems())
            print(f"Selected items: {items_to_remove}")
            for item in items_to_remove:
                if isinstance(item, Edge):
                    self.remove_edge(item)
                elif isinstance(item, Step):
                    self.remove_step(item)
            self.main_window.clear_io_display()
            self.update()
        super().keyPressEvent(event)

    def remove_edge(self, edge):
        print(f"Removing edge: {edge}")
        self.removeItem(edge)
        self.edges.remove(edge)
        self.graph.remove_edge(edge.source.unique_name, edge.target.unique_name)

    def remove_step(self, step):
        print(f"Removing step: {step.unique_name}")
        edges_to_remove = [edge for edge in self.edges if edge.source == step or edge.target == step]
        for edge in edges_to_remove:
            self.remove_edge(edge)
        
        self.removeItem(step)
        del self.steps[step.unique_name]
        self.graph.remove_node(step.unique_name)

    def validate_connection(self, source, target):
        source_outputs = {output['name']: output['type'] for output in source.outputs}
        target_inputs = {input['name']: input['type'] for input in target.inputs}
        
        for input_name, input_type in target_inputs.items():
            if input_name in source_outputs and source_outputs[input_name] == input_type:
                return True
        return False
    
    def get_workflow_order(self):
        return list(nx.topological_sort(self.graph))

class WorkflowView(QGraphicsView):
    def __init__(self, scene):
        super().__init__(scene)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)

    def wheelEvent(self, event):
        if event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            factor = 1.1
            if event.angleDelta().y() < 0:
                factor = 0.9
            self.scale(factor, factor)
        else:
            super().wheelEvent(event)

class MainWindow(QMainWindow):
    def __init__(self, steps_data):
        super().__init__()
        self.steps_data = steps_data
        self.current_step = None
        self.temp_input_values = {}
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Workflow Builder")
        self.setGeometry(100, 100, 1200, 600)

        main_widget = QWidget()
        main_layout = QVBoxLayout()

        content_layout = QHBoxLayout()

        left_widget = QWidget()
        left_layout = QVBoxLayout()
        self.step_list = QListWidget()
        self.step_list.addItems(self.steps_data.keys())
        self.step_list.itemClicked.connect(self.add_step_to_canvas)
        left_layout.addWidget(self.step_list)
        left_widget.setLayout(left_layout)

        middle_widget = QWidget()
        middle_layout = QVBoxLayout()
        self.scene = WorkflowScene(self.steps_data, self)
        self.view = WorkflowView(self.scene)
        
        button_layout = QHBoxLayout()
        zoom_in_button = QPushButton("+")
        zoom_out_button = QPushButton("-")
        save_workflow_button = QPushButton("Save Workflow")
        load_workflow_button = QPushButton("Load Workflow")
        export_button = QPushButton("Export")
        zoom_in_button.clicked.connect(lambda: self.view.scale(1.2, 1.2))
        zoom_out_button.clicked.connect(lambda: self.view.scale(0.8, 0.8))
        save_workflow_button.clicked.connect(self.save_workflow)
        load_workflow_button.clicked.connect(self.load_workflow)
        export_button.clicked.connect(self.export_workflow)
        
        button_layout.addWidget(zoom_in_button)
        button_layout.addWidget(zoom_out_button)
        button_layout.addWidget(save_workflow_button)
        button_layout.addWidget(load_workflow_button)
        button_layout.addWidget(export_button)
        
        middle_layout.addLayout(button_layout)
        
        middle_layout.addWidget(self.view)
        middle_widget.setLayout(middle_layout)
        
        right_widget = QWidget()
        right_layout = QVBoxLayout()
        self.io_display = QScrollArea()
        self.io_display.setWidgetResizable(True)
        self.io_form = QWidget()
        self.io_form_layout = QFormLayout()
        self.io_form.setLayout(self.io_form_layout)
        self.io_display.setWidget(self.io_form)
        right_layout.addWidget(QLabel("Node I/O:"))
        right_layout.addWidget(self.io_display)
        
        # Add save button
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_input_values)
        self.save_button.setEnabled(False)
        right_layout.addWidget(self.save_button)
        
        right_widget.setLayout(right_layout)

        content_layout.addWidget(left_widget, 1)
        content_layout.addWidget(middle_widget, 3)
        content_layout.addWidget(right_widget, 1)

        main_layout.addLayout(content_layout)

        self.status_bar = QStatusBar()
        main_layout.addWidget(self.status_bar)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.scene.selectionChanged.connect(self.update_io_display)

    def update_status(self, message):
        self.status_bar.showMessage(message)

    def add_step_to_canvas(self, item):
        step_name = item.text()
        step_data = self.steps_data[step_name]
        x = 200 + (len(self.scene.steps) % 3) * 200
        y = 100 + (len(self.scene.steps) // 3) * 150
        self.scene.add_step(step_name, step_data, x, y)

    def update_io_display(self):
        # Clear previous form layout
        while self.io_form_layout.rowCount() > 0:
            self.io_form_layout.removeRow(0)

        selected_items = self.scene.selectedItems()
        if len(selected_items) == 1 and isinstance(selected_items[0], Step):
            step = selected_items[0]
            self.current_step = step
            self.temp_input_values = {}  # Reset temporary values
            
            self.io_form_layout.addRow(QLabel(f"Node: {step.unique_name}"))
            self.io_form_layout.addRow(QLabel("Inputs:"))

            for input_data in step.inputs:
                input_name = input_data['name']
                input_type = input_data['type']
                input_value = self.get_input_value(step, input_name)
                
                input_field = QLineEdit(input_value)
                input_field.setPlaceholderText(f"Type: {input_type}")
                input_field.textChanged.connect(lambda text, n=input_name: self.update_temp_input_value(n, text))
                
                self.io_form_layout.addRow(f"{input_name}:", input_field)

            self.io_form_layout.addRow(QLabel("Outputs:"))
            for output in step.outputs:
                self.io_form_layout.addRow(f"{output['name']} ({output['type']})", QLabel(""))

            self.save_button.setEnabled(True)
        else:
            self.current_step = None
            self.save_button.setEnabled(False)

        self.io_form.adjustSize()

    def get_input_value(self, step, input_name):
        # First, check if there's a user-assigned value
        if input_name in step.user_assigned_inputs:
            return step.user_assigned_inputs[input_name]
        
        # If not, check for connected inputs
        incoming_edges = self.scene.graph.in_edges(step.unique_name)
        for source, target in incoming_edges:
            source_step = self.scene.steps[source]
            for output in source_step.outputs:
                if output['name'] == input_name:
                    return f"From: {source_step.unique_name}.{output['name']}"
        return ""

    def update_temp_input_value(self, input_name, value):
        self.temp_input_values[input_name] = value

    def save_input_values(self):
        if self.current_step:
            for input_name, value in self.temp_input_values.items():
                if value.startswith("From: "):
                    # This input is connected to another node's output, so we don't store a user-assigned value
                    if input_name in self.current_step.user_assigned_inputs:
                        del self.current_step.user_assigned_inputs[input_name]
                else:
                    # Store the user-assigned value
                    self.current_step.user_assigned_inputs[input_name] = value
            
            # Update the graph to reflect this change
            self.scene.graph.nodes[self.current_step.unique_name]['user_assigned_inputs'] = self.current_step.user_assigned_inputs

            self.update_io_display()  # Refresh the display
            self.update_status(f"Input values saved for {self.current_step.unique_name}")

    def clear_io_display(self):
        # Clear previous form layout
        while self.io_form_layout.rowCount() > 0:
            self.io_form_layout.removeRow(0)
        
        # Reset the form widget
        self.io_form.setLayout(self.io_form_layout)
        self.io_display.setWidget(self.io_form)

    def update_input_value(self, step, input_name, value):
        if value.startswith("From: "):
            # This input is connected to another node's output, so we don't store a user-assigned value
            if input_name in step.user_assigned_inputs:
                del step.user_assigned_inputs[input_name]
        else:
            # Store the user-assigned value
            step.user_assigned_inputs[input_name] = value
        
        # Update the graph to reflect this change
        self.scene.graph.nodes[step.unique_name]['user_assigned_inputs'] = step.user_assigned_inputs

        # Print for debugging (you can remove this later)
        print(f"Updated {step.unique_name}.{input_name} to: {value}")
        print(f"Current user-assigned inputs for {step.unique_name}: {step.user_assigned_inputs}")
    
    def save_workflow(self):
        workflow_name, ok = QInputDialog.getText(self, 'Save Workflow', 'Enter workflow name:')
        if ok and workflow_name:
            filename = f"{workflow_name}_workflow.json"
            workflow_data = self.serialize_workflow()
            
            try:
                with open(filename, 'w') as f:
                    json.dump(workflow_data, f, indent=2)
                QMessageBox.information(self, "Save Successful", f"Workflow saved to {filename}")
            except Exception as e:
                QMessageBox.critical(self, "Save Failed", f"Failed to save workflow: {str(e)}")

    def load_workflow(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Load Workflow", "", "JSON Files (*.json)")
        if filename:
            try:
                with open(filename, 'r') as f:
                    workflow_data = json.load(f)
                self.deserialize_workflow(workflow_data)
                QMessageBox.information(self, "Load Successful", f"Workflow loaded from {filename}")
            except Exception as e:
                QMessageBox.critical(self, "Load Failed", f"Failed to load workflow: {str(e)}")

    def serialize_workflow(self):
        workflow_data = {
            'steps': {},
            'edges': []
        }

        for step_name, step in self.scene.steps.items():
            workflow_data['steps'][step_name] = {
                'name': step.name,
                'id': step.id,
                'x': step.x(),
                'y': step.y(),
                'inputs': step.inputs,
                'outputs': step.outputs,
                'user_assigned_inputs': step.user_assigned_inputs
            }

        for edge in self.scene.edges:
            workflow_data['edges'].append({
                'source': edge.source.unique_name,
                'target': edge.target.unique_name
            })

        return workflow_data

    def deserialize_workflow(self, workflow_data):
        self.scene.clear()
        self.scene.steps = {}
        self.scene.edges = []
        self.scene.graph.clear()

        for step_name, step_data in workflow_data['steps'].items():
            step = Step(step_data['name'], step_data['id'], step_data['inputs'], step_data['outputs'], 
                        step_data['x'], step_data['y'])
            step.user_assigned_inputs = step_data['user_assigned_inputs']
            self.scene.addItem(step)
            self.scene.steps[step_name] = step
            self.scene.graph.add_node(step_name)

        for edge_data in workflow_data['edges']:
            source_step = self.scene.steps[edge_data['source']]
            target_step = self.scene.steps[edge_data['target']]
            edge = Edge(source_step, target_step)
            self.scene.addItem(edge)
            self.scene.edges.append(edge)
            self.scene.graph.add_edge(edge_data['source'], edge_data['target'])

        self.scene.update()
        self.view.update()
        
    def export_workflow(self):
        workflow_name, ok = QInputDialog.getText(self, 'Export Workflow', 'Enter workflow name:')
        if ok and workflow_name:
            filename = f"{workflow_name}.py"
            workflow_order = self.scene.get_workflow_order()
            
            try:
                with open(filename, 'w') as f:
                    f.write("import yaml\n")
                    f.write("from pathlib import Path\n")
                    f.write("from patchwork.step import Step\n")
                    f.write(f"from patchwork.steps import {', '.join(set(step.split('_')[0] for step in workflow_order))}\n\n\n")
                    f.write(f"_DEFAULT_INPUT_FILE = Path(__file__).parent / 'defaults.yml'\n\n")
                
                    f.write(f"class {workflow_name}(Step):\n")
                    f.write("    def __init__(self, inputs):\n")
                    f.write("        super().__init__(inputs)\n")
                    f.write("        initial_inputs = yaml.safe_load(_DEFAULT_INPUT_FILE.read_text())\n")
                    f.write("        self.inputs = {**initial_inputs, **inputs}\n\n")
                    
                    # Add user-assigned input values
                    f.write("        # User-assigned input values\n")
                    for step in workflow_order:
                        step_obj = self.scene.steps[step]
                        if step_obj.user_assigned_inputs:
                            f.write(f"        # {step_obj.unique_name} inputs\n")
                            for input_name, input_value in step_obj.user_assigned_inputs.items():
                                f.write(f"        self.inputs['{input_name}'] = {repr(input_value)}\n")
                    f.write("\n")

                    f.write("    def validate_inputs(self):\n")
                    f.write("        missing_inputs = []\n")
                    
                    missing_required_inputs = set()
                    for step in workflow_order:
                        step_obj = self.scene.steps[step]
                        required_inputs = [inp['name'] for inp in step_obj.inputs if inp.get('required', True)]
                        incoming_edges = list(self.scene.graph.in_edges(step))
                        
                        # Get the actual input names that are assigned from incoming edges
                        assigned_inputs = set()
                        for source, target in incoming_edges:
                            source_obj = self.scene.steps[source]
                            for output in source_obj.outputs:
                                assigned_inputs.add(output['name'])
                        
                        # Include user-assigned inputs
                        assigned_inputs.update(step_obj.user_assigned_inputs.keys())
                        
                        for req_input in required_inputs:
                            if req_input not in assigned_inputs:
                                f.write(f"        if '{req_input}' not in self.inputs:\n")
                                f.write(f"            missing_inputs.append('{req_input}')\n")
                                missing_required_inputs.add(req_input)

                    f.write("        if missing_inputs:\n")
                    f.write("            raise ValueError(f'Missing required inputs: {missing_inputs}. Please add them to the defaults.yml file.')\n\n")

                    f.write("    def run(self) -> dict:\n")
                    f.write("        self.validate_inputs()\n")
                    f.write("        inputs = self.inputs.copy()\n")
                    
                    for step in workflow_order:
                        step_name, step_id = step.rsplit('_', 1)
                        incoming_edges = list(self.scene.graph.in_edges(step))
                        
                        if not incoming_edges:
                            # No incoming edges, use self.inputs
                            f.write(f"        outputs_{step} = {step_name}(inputs).run()\n")
                        else:
                            # Construct input dictionary from incoming edges
                            input_dict = {}
                            for source, _ in incoming_edges:
                                source_obj = self.scene.steps[source]
                                for output in source_obj.outputs:
                                    input_dict[output['name']] = f"outputs_{source}['{output['name']}']"
                            
                            input_str = ", ".join(f"'{k}': {v}" for k, v in input_dict.items())
                            f.write(f"        step_inputs = {{**inputs, {input_str}}}\n")
                            f.write(f"        outputs_{step} = {step_name}(step_inputs).run()\n")
                    
                    # Determine the final outputs
                    final_steps = [step for step in workflow_order if not list(self.scene.graph.out_edges(step))]
                    final_outputs = {}
                    for step in final_steps:
                        for output in self.scene.steps[step].outputs:
                            final_outputs[output['name']] = f"outputs_{step}['{output['name']}']"
                    
                    final_outputs_str = ", ".join(f"'{k}': {v}" for k, v in final_outputs.items())
                    f.write(f"        final_outputs = {{**inputs, {final_outputs_str}}}\n")
                    f.write("        return final_outputs\n")
                
                if missing_required_inputs:
                    message = f"Workflow exported to {filename}\n\nThe following required inputs are missing and should be added to the defaults.yml file:\n{', '.join(missing_required_inputs)}"
                    QMessageBox.warning(self, "Export Successful - Action Required", message)
                else:
                    QMessageBox.information(self, "Export Successful", f"Workflow exported to {filename}")
            except Exception as e:
                QMessageBox.critical(self, "Export Failed", f"Failed to export workflow: {str(e)}")


if __name__ == "__main__":
    with open("steps.artifact.json", "r") as f:
        steps_data = json.load(f)

    app = QApplication(sys.argv)
    window = MainWindow(steps_data)
    window.show()
    sys.exit(app.exec())