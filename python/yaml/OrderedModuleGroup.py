from ModuleConfigData import ModuleConfigData

class OrderedModuleGroup:

    def __init__(self, ordered_list_of_module_config):
        self.ordered_list_of_module_config = ordered_list_of_module_config

    # def __repr__(self):
    #     result = []
    #     for i in self.ordered_list_of_module_config:
    #         result.append(str(i))
    #     return i

# dict = {'a': 'one', 'b': "two"}
# mc = ModuleConfigData("test_module_name", dict)
# dict2 = {'aa': 'aaone', 'bb': "bbtwo"}
# mc2 = ModuleConfigData("test_module_name_2", dict2)
# list = [mc, mc2]
# o = OrderedModuleGroup(list)
# print(o)