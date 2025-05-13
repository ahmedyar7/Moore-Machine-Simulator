"""Mealy machine simulator module."""

from state import State


class MealyMachine:
    """A class to represent a Mealy machine."""

    def __init__(self):
        """Initialize the Mealy machine with states and an initial state."""
        self.states: dict = {}
        self.initial_state = None

    def add_state(self, name: str, is_initial=False):
        """
        Add a state to the machine.
        """
        state: State = State(name)
        self.states[name] = state
        if is_initial:
            self.initial_state = state

    def add_transition(
        self, from_state: str, input_symbol: str, to_state: str, output: str
    ):
        """
        Add a transition between states.
        """
        self.states[from_state].add_transition(
            input_symbol, self.states[to_state], output
        )

    def simulate(self, input_string: str):
        """
        Simulate the Mealy machine on the given input string.
        """
        state = self.initial_state
        output_sequence = []

        for symbol in input_string:
            state, output = state.transitions[symbol]
            output_sequence.append(output)

        return output_sequence
