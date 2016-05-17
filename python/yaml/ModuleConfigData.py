"""
A simple data holder that is populated for each module.
The fields are populated based on the values specified in the yaml file.
"""
class ModuleConfigData:

    def __init__(self, module_name, params_dictionary):
        self.module_name = module_name
        self.params_dictionary = params_dictionary

    def __repr__(self):
        return (self.module_name + ": " + str(self.params_dictionary))

# dict = {'a': 'one', 'b': "two"}
# mc = ModuleConfigData("test_module_name", dict)
# print(mc)
