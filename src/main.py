import time
import sys
from node.node_manager import NodeManager
from node.node_brain import NodeBrain
from utils.logger import Logger

def main():
    Logger.log("Initializing Singulon Node...")
    manager = NodeManager(config_path="config/config.json")
    brain = NodeBrain(manager)

    # Start Node
    manager.start_node()
    Logger.log("Singulon Node is ACTIVE.")

    # Main loop
    while True:
        # Periodically gather data, run AI, and execute decisions
        brain.gather_data()
        brain.execute_ai_pipelines()
        brain.perform_governance_actions()
        time.sleep(10)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        Logger.log("Shutting down Singulon gracefully...")
        sys.exit(0)
