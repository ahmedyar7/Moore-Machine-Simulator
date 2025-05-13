"""This module is used to represent the state for moore and melay machine respectively"""


class State:
    """
    This class is used to define the actual states of the machine
    each state is represented by another states
    """

    def __init__(self, name, output=None):
        self.name = name
        self.output = output
        self.transitions = {}

    def add_transition(self, input_symbol, next_state, output=None):
        """
        This funcinon is used for adding the transtions to the states
        """
        self.transitions[input_symbol] = (
            next_state,
            output,
        )  # Change 'transition' to 'transitions'
