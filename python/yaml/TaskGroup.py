from TaskConfig import TaskConfig

class TaskGroup:

    def __init__(self, list_of_task_config):
        self.list_of_task_config = list_of_task_config

    # def __repr__(self):
    #     result = []
    #     for i in self.list_of_task_config:
    #         result.append(str(i))
    #     return i

# dict = {'a': 'one', 'b': "two"}
# mc = TaskConfig("test_task_name", dict)
# dict2 = {'aa': 'aaone', 'bb': "bbtwo"}
# mc2 = TaskConfig("test_task_name_2", dict2)
# list = [mc, mc2]
# o = TaskSet(list)
# print(o)