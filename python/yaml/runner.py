from context import Context
import key_names
from orchestrator import Orchestrator
import yaml_file_reader

context = Context()
context.set_value(key_names.KEY_MESSAGE_DEFINITION_FILE_PATH, '/log_data/stork_messages.csv')

list_of_task_groups = yaml_file_reader.get_task_group_list(key_names.KEY_YAML_FILE_PATH)

o = Orchestrator()
bool_result = o.run_tasks(list_of_task_groups=list_of_task_groups, context=context)

print('runner DONE. result', bool_result)
