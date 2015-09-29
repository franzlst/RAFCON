# core elements
from rafcon.statemachine.execution.statemachine_execution_engine import StatemachineExecutionEngine
from rafcon.statemachine.states.execution_state import ExecutionState
from rafcon.statemachine.states.hierarchy_state import HierarchyState

# singleton elements
import rafcon.statemachine.singleton

# test environment elements
import test_utils


def test_error_propagation():

    rafcon.statemachine.singleton.state_machine_manager.delete_all_state_machines()
    test_utils.test_multithrading_lock.acquire()

    sm = StatemachineExecutionEngine.execute_state_machine_from_path(rafcon.__path__[0] + "/../test_scripts/error_propagation_test")
    rafcon.statemachine.singleton.state_machine_manager.remove_state_machine(sm.state_machine_id)
    assert sm.root_state.output_data["error_check"] == "successfull"

    test_utils.test_multithrading_lock.release()


if __name__ == '__main__':
    test_error_propagation()
