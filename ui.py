"""This module would take care of all the UI Components"""

import sys

from PyQt5.QtGui import QPixmap, QColor, QPalette
from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QRadioButton,
    QTextEdit,
    QApplication,
)
from graph_generation import GraphGenerator
from moore_controller import MooreMachineController
from moore_machine import MooreMachine


class FSMGui(QMainWindow):
    """This class is the finite state machine GUI"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Moore Machine Simulator")
        self.setGeometry(300, 100, 800, 600)
        self.set_dark_theme()
        self.moore_machine = MooreMachine()
        self.init_ui()
        self.graph_generator = GraphGenerator(self.moore_machine)
        self.controller = MooreMachineController(self.moore_machine)

    def set_dark_theme(self):
        """This would set the application mode to the dark theme"""
        # Set the application to dark mode
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(33, 33, 33))  # Dark background
        palette.setColor(QPalette.WindowText, QColor(255, 255, 255))  # White text
        palette.setColor(QPalette.Base, QColor(50, 50, 50))  # Dark base for text input
        palette.setColor(QPalette.AlternateBase, QColor(33, 33, 33))
        palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        palette.setColor(QPalette.Button, QColor(60, 60, 60))  # Button background
        palette.setColor(
            QPalette.ButtonText, QColor(255, 255, 255)
        )  # Button text color
        palette.setColor(QPalette.Highlight, QColor(78, 154, 255))  # Highlighted items
        palette.setColor(
            QPalette.HighlightedText, QColor(255, 255, 255)
        )  # Highlighted text color

        self.setPalette(palette)

    def init_ui(self):
        """This would be the initialization function for the UI components"""
        main_layout = QVBoxLayout()

        # State Input
        state_layout = QHBoxLayout()
        self.state_name_input = QLineEdit()
        self.state_output_input = QLineEdit()
        self.initial_state_radio = QRadioButton("Initial")
        self.add_state_btn = QPushButton("Add State")
        self.add_state_btn.clicked.connect(self.add_state)

        # Add some padding and minimal design
        self.state_name_input.setStyleSheet(
            "background-color: #333333; color: white; padding: 5px;"
        )
        self.state_output_input.setStyleSheet(
            "background-color: #333333; color: white; padding: 5px;"
        )
        self.add_state_btn.setStyleSheet(
            "background-color: #555555; color: white; border-radius: 5px; padding: 10px; border: none;"
        )

        state_layout.addWidget(QLabel("State Name:"))
        state_layout.addWidget(self.state_name_input)
        state_layout.addWidget(QLabel("Output:"))
        state_layout.addWidget(self.state_output_input)
        state_layout.addWidget(self.initial_state_radio)
        state_layout.addWidget(self.add_state_btn)

        # Transition Input
        transition_layout = QHBoxLayout()
        self.from_state_input = QLineEdit()
        self.input_symbol_input = QLineEdit()
        self.to_state_input = QLineEdit()
        self.add_transition_btn = QPushButton("Add Transition")
        self.add_transition_btn.clicked.connect(self.add_transition)

        self.from_state_input.setStyleSheet(
            "background-color: #333333; color: white; padding: 5px;"
        )
        self.input_symbol_input.setStyleSheet(
            "background-color: #333333; color: white; padding: 5px;"
        )
        self.to_state_input.setStyleSheet(
            "background-color: #333333; color: white; padding: 5px;"
        )
        self.add_transition_btn.setStyleSheet(
            "background-color: #555555; color: white; border-radius: 5px; padding: 10px; border: none;"
        )

        transition_layout.addWidget(QLabel("From:"))
        transition_layout.addWidget(self.from_state_input)
        transition_layout.addWidget(QLabel("Input Symbol:"))
        transition_layout.addWidget(self.input_symbol_input)
        transition_layout.addWidget(QLabel("To:"))
        transition_layout.addWidget(self.to_state_input)
        transition_layout.addWidget(self.add_transition_btn)

        # Input String Simulation
        input_layout = QHBoxLayout()
        self.input_string = QLineEdit()
        self.simulate_btn = QPushButton("Simulate")
        self.simulate_btn.clicked.connect(self.simulate)

        self.input_string.setStyleSheet(
            "background-color: #333333; color: white; padding: 5px;"
        )
        self.simulate_btn.setStyleSheet(
            "background-color: #555555; color: white; border-radius: 5px; padding: 10px; border: none;"
        )

        input_layout.addWidget(QLabel("Input String:"))
        input_layout.addWidget(self.input_string)
        input_layout.addWidget(self.simulate_btn)

        # Graph Generation Button
        self.graph_btn = QPushButton("Generate Graph")
        self.graph_btn.clicked.connect(self.generate_graph_and_show)
        self.graph_btn.setStyleSheet(
            "background-color: #555555; color: white; border-radius: 5px; padding: 10px; border: none;"
        )
        main_layout.addWidget(self.graph_btn)

        # Output Display
        self.output_display = QTextEdit()
        self.output_display.setReadOnly(True)
        self.output_display.setStyleSheet(
            "background-color: #333333; color: white; padding: 10px;"
        )

        main_layout.addLayout(state_layout)
        main_layout.addLayout(transition_layout)
        main_layout.addLayout(input_layout)
        main_layout.addWidget(QLabel("Output Sequence:"))
        main_layout.addWidget(self.output_display)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def add_state(self):
        """This would be used  to add the state to the Finite Machine"""
        name = self.state_name_input.text().strip()
        output = self.state_output_input.text().strip()
        is_initial = self.initial_state_radio.isChecked()
        if name and output:
            msg = self.controller.add_state(name, output, is_initial)
            self.output_display.append(msg)
            self.state_name_input.clear()
            self.state_output_input.clear()
            self.initial_state_radio.setChecked(False)

    def add_transition(self):
        """This would be used to add transitions to the Finite Machine"""
        from_state = self.from_state_input.text().strip()
        symbol = self.input_symbol_input.text().strip()
        to_state = self.to_state_input.text().strip()
        if from_state and symbol and to_state:
            msg = self.controller.add_transition(from_state, symbol, to_state)
            self.output_display.append(msg)
            self.from_state_input.clear()
            self.input_symbol_input.clear()
            self.to_state_input.clear()

    def simulate(self):
        """This would be used for the simulations of the machine"""
        input_str = self.input_string.text()
        try:
            msg = self.controller.simulate(input_str)
            self.output_display.append(msg)
        except Exception as e:
            self.output_display.append(f"Error: {str(e)}")

    def generate_graph_and_show(self):
        "This function  would generate the Graph of Finite Machine and the"
        try:
            image_path = self.graph_generator.generate_graph()
            if self.graph_generator.graph_exists(image_path):
                pixmap = QPixmap(image_path)
                label = QLabel()
                label.setPixmap(pixmap)
                label.setWindowTitle("Moore Machine Graph")
                label.resize(pixmap.width(), pixmap.height())
                label.setAttribute(Qt.WA_DeleteOnClose)  # type: ignore
                label.show()
                self.output_display.append("Graph generated and displayed.")
            else:
                self.output_display.append("Graph image not found.")
        except Exception as e:
            self.output_display.append(f"Error generating graph: {e}")


def main():
    app = QApplication(sys.argv)
    window = FSMGui()
    window.show()
    sys.exit(app.exec_())
