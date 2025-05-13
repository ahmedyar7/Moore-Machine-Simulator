"""Moore machine simulator module."""

from state import State


class MooreMachine:
    """A class to represent a Moore machine."""

    def __init__(self):
        """Initialize the Moore machine with states and an initial state."""
        self.states = {}
        self.initial_state = None

    def add_state(self, name, output, is_initial=False):
        """
        Add a state to the Moore machine.
        """
        state = State(name, output)
        self.states[name] = state

        if is_initial:
            self.initial_state = state

    def add_transition(self, from_state, input_symbol, to_state):
        """
        Add a transition between states.
        """
        self.states[from_state].add_transition(input_symbol, self.states[to_state])

    def simulate(self, input_string):
        """
        Simulate the Moore machine on the given input string.
        """
        state = self.initial_state
        output_sequence = [state.output]

        for symbol in input_string:
            state = state.transitions[symbol][0]  # Follow the transition
            output_sequence.append(state.output)

        return output_sequence
