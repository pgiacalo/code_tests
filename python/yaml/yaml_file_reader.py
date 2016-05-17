"""
A utility module that reads the yaml file and returns a list of
Module_Config objects.
"""
import yaml
import json
import module_group
import module_config

# fixed key names used in the yaml file
KEY_MODULES = 'modules'
KEY_FILE_PATH = 'file_path'
KEY_BINARY_MISSION_LOG_DATA = 'binary_mission_log_data'
KEY_BINARY_FLIGHT_LOG_DATA = 'binary_flight_log_data'
KEY_PROTOBUF_MISSION_LOG_DATA = 'protobuf_mission_log_data'
KEY_PROTOBUF_FLIGHT_LOG_DATA = 'protobuf_flight_log_data'


def get_module_configs(yaml_file_name):

    modules = yaml.load(open(yaml_file_name))
    print('modules', type(modules))
    print('yaml contents', modules)

    print('-------------------------')
    print('LEVEL 1: modules', type(modules))
    print('modules', modules)
    print('modules size', len(modules))

    list_of_module_groups = []

    # iterate thru the list of modules
    for dict_of_modules in modules:
        print('-------------MODULE GROUP-------------')
        print('LEVEL 2: dict_of_modules', type(dict_of_modules))
        print('dict_of_modules', dict_of_modules)

        ordered_list_of_module_config = []
        list_of_module_groups.append(ordered_list_of_module_config)

        # pull the modules out of the dictionary as a list
        # each item in the list is a dictionary keyed by 'modules'
        list_of_modules = dict_of_modules[KEY_MODULES]

        print('LEVEL 3: list_of_modules type', type(list_of_modules))
        print('list_of_modules', list_of_modules)

        for module_dict in list_of_modules:
            print('LEVEL 4: module_dict type', type(module_dict))
            print('module_dict', module_dict)

            for module_name in module_dict:
                print('LEVEL 5: module_name type', type(module_name))
                print('module_name', module_name)
                params_dict = module_dict[module_name]
                for param_name in params_dict:
                    param_value = params_dict[param_name]
                    print(param_name, param_value)
                    # ordered_list_of_module_config.append(module_config(module_name, params_dict))

    return list_of_module_groups

###############################################
# testing logic
###############################################
yaml_file_name = 'yaml.yaml'
list_of_module_groups = get_module_configs(yaml_file_name)
# for module_group in list_of_module_groups:
#     print("-------modules-------")
#     for module_config in module_group.ordered_list_of_module_config:
#         print(module_config.module_name)
#         for key in module_config.params_dictionary:
#             print(key, module_config.params_dictionary[key])


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
