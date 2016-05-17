"""
A utility module that reads the yaml file and returns a list of TaskGroup objects.

Each TaskGroup represents a set of python modules to be executed in parallel.
Each group on the list of TaskGroups is executed sequentially.
"""

import yaml
from TaskGroup import TaskGroup
from TaskConfig import TaskConfig
# import json

# fixed key names used in the yaml file
KEY_TASKS = 'tasks'
KEY_FILE_PATH = 'file_path'
KEY_BINARY_MISSION_LOG_DATA = 'binary_mission_log_data'
KEY_BINARY_FLIGHT_LOG_DATA = 'binary_flight_log_data'
KEY_PROTOBUF_MISSION_LOG_DATA = 'protobuf_mission_log_data'
KEY_PROTOBUF_FLIGHT_LOG_DATA = 'protobuf_flight_log_data'


def get_task_group_list(yaml_file_name):
    """Reads the given yaml config file and returns a list of TaskGroup objects."""

    # the list to be populated and returned
    list_of_task_groups = []

    f = open(yaml_file_name)
    task_list = yaml.load(f)
    f.close()

    # print('modules', type(task_list))
    # print('yaml contents', task_list)
    #
    # print('-------------------------')
    # print('LEVEL 1: modules', type(task_list))
    # print('modules', task_list)
    # print('modules size', len(task_list))

    # iterate thru the task_list
    for dict_of_tasks in task_list:

        #create the nested structure used to return the data
        list_of_task_config = []
        task_group = TaskGroup(list_of_task_config)
        list_of_task_groups.append(task_group)

        # print('-------------MODULE GROUP-------------')
        # print('LEVEL 2: dict_of_tasks', type(dict_of_tasks))
        # print('dict_of_tasks', dict_of_tasks)

        # now pull the tasks out of the dictionary as a list
        # each item in the list is a dictionary keyed by 'tasks'
        list_of_tasks = dict_of_tasks[KEY_TASKS]

        # print('LEVEL 3: list_of_tasks type', type(list_of_tasks))
        # print('list_of_tasks', list_of_tasks)

        for task_dict in list_of_tasks:
            # print('LEVEL 4: task_dict type', type(task_dict))
            # print('task_dict', task_dict)

            for task_name in task_dict:
                # print('LEVEL 5: task_name type', type(task_name))
                # print('task_name', task_name)
                params_dict = task_dict[task_name]
                list_of_task_config.append(TaskConfig(task_name, params_dict))

                # for testing only
                # for param_name in params_dict:
                #     param_value = params_dict[param_name]
                #     print(param_name, param_value)

    return list_of_task_groups


###############################################
# testing logic
###############################################
yaml_file_name = 'task_list.yaml'
list_of_task_groups = get_task_group_list(yaml_file_name)

for task_group in list_of_task_groups:
    print("-------task group-------")
    for task_config in task_group.list_of_task_config:
        print(task_config.module_name)
        for key in task_config.params_dictionary:
            print(key, task_config.params_dictionary[key])


###############################################
# playing around with yaml to json conversiohn
###############################################
# modules = yaml.load(open(yaml_file_name))
# print('=========')
# json_str = str(modules)
#
# # valid json requires double quotes rather than single quotes
# json_str = json_str.replace("'", "\"")
# print(json_str)
# print('=========')
# print('modules type', type(modules))
#
# # load json from a string representation
# d = json.loads(json_str)
#
# print('json type')
# print(type(d))
# print('json')
# print(d)
