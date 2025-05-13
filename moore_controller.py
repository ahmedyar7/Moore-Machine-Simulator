"""
This module contain class that would be used for, simulation of the Moore Machine
"""


class MooreMachineController:
    """This class handles the mmoore machine simulations"""

    def __init__(self, moore_machine):
        self.moore_machine = moore_machine

    def add_state(self, name, output, is_initial=False):
        """This add the different states regarding the machine"""
        self.moore_machine.add_state(name, output, is_initial)
        return f"State added: {name}, Output: {output}, Initial: {is_initial}"

    def add_transition(self, from_state, symbol, to_state):
        "This add the transtion towards the states"
        self.moore_machine.add_transition(from_state, symbol, to_state)
        return f"Transition added: {from_state} --{symbol}--> {to_state}"

    def simulate(self, input_str):
        """This handles the simulation part towards the state"""
        result = self.moore_machine.simulate(input_str)
        return f"Simulation result for '{input_str}': {' '.join(result)}"
