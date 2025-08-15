from domain.plugins import Plugin
from domain.nodes import Node
from typing import Dict


class AProperOnePlugin(Plugin):
    title = "A Proper One Plugin"

    def nodes(self):
        return [AProperOneNode()]


class AProperOneNode(Node):
    name = "a_proper_one-node"
    title = "A Proper One Node"
    description = "A node for a_proper_one"

    def call(self, input_text: str) -> Dict:
        # Plugin logic here
        return {"result": input_text}

class AnEvenMoreProperOneNode(Node):
    name = "an_even_more_proper_one-node"
    title = "Does something interesting with two numbers"
    description = "Another node for a_proper_one"

    def call(self, input_a: int, input_b: int) -> Dict:
        # Plugin logic here
        if input_a % 2 == 0:  # input_a is even
            result = input_a * input_b
        else:  # input_a is odd
            result = input_a + input_b

        return {"result": result}
