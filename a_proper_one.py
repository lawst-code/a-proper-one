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
