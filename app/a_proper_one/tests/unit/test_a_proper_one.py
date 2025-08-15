import pytest
from a_proper_one import AProperOneNode, AProperOnePlugin


class TestAProperOnePlugin:
    def test_plugin_creation(self):
        """Test that the plugin can be instantiated"""
        plugin = AProperOnePlugin()
        assert plugin.title == "A Proper One Plugin"
        assert len(plugin.nodes()) == 1

    def test_plugin_has_node(self):
        """Test that the plugin has the expected node"""
        plugin = AProperOnePlugin()
        nodes = plugin.nodes()
        assert len(nodes) == 2
        assert isinstance(nodes[0], AProperOneNode)


class TestAProperOneNode:
    def test_node_creation(self):
        """Test that the node can be instantiated"""
        node = AProperOneNode()
        assert node.name == "a_proper_one-node"
        assert node.title == "A Proper One Node"
        assert node.description == "A node for a_proper_one"

    def test_node_call_with_string(self):
        """Test that the node processes string input correctly"""
        node = AProperOneNode()
        result = node.call("Hello, World!")
        assert result == {"result": "Hello, World!"}

    def test_node_call_with_empty_string(self):
        """Test that the node handles empty strings"""
        node = AProperOneNode()
        result = node.call("")
        assert result == {"result": ""}

    def test_node_call_with_special_characters(self):
        """Test that the node handles special characters"""
        node = AProperOneNode()
        test_input = "Test with special chars: !@#$%^&*()"
        result = node.call(test_input)
        assert result == {"result": test_input}
