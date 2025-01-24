import pytest
from src.node.node_communication import NodeCommunication

def test_broadcast_update():
    success = NodeCommunication.broadcast_update({"test": "data"})
    assert success is True

def test_receive_updates():
    updates = NodeCommunication.receive_updates()
    assert isinstance(updates, dict)
