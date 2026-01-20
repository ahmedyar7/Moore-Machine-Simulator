"""This module is responsible for making the graph using graphviz Digraph"""

# graph_generator.py
import os
from datetime import datetime
from graphviz import Digraph


class GraphGenerator:
    """This class is responsible for generating the graphs"""

    def __init__(self, moore_machine):
        self.moore_machine = moore_machine
        self.image_dir = "machine_images"
        os.makedirs(self.image_dir, exist_ok=True)  # Safe creation

    def generate_graph(self, filename=None):
        """This function would generate the graph and place it into right directory"""
        # Generate unique filename with timestamp if not provided
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"moore_machine_{timestamp}"
        
        # Full path including the directory
        full_path = os.path.join(self.image_dir, filename)

        dot = Digraph()

        # Add nodes
        for state_name, state in self.moore_machine.states.items():
            label = f"{state_name}\\nOutput: {state.output}"
            shape = (
                "doublecircle"
                if state == self.moore_machine.initial_state
                else "circle"
            )
            dot.node(state_name, label=label, shape=shape)

        # Add transitions
        for state in self.moore_machine.states.values():
            for input_symbol, (next_state, _) in state.transitions.items():
                dot.edge(state.name, next_state.name, label=f"{input_symbol}")

        dot.render(full_path, format="png", cleanup=True)
        return f"{full_path}.png"

    def graph_exists(self, path):
        "This would check if the graph already exists or not"
        return os.path.exists(path)
