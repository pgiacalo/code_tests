from multiprocessing import Pool
import traceback
import importlib
import key_names

class Orchestrator:
    # @param list_of_task_groups - a list of TaskGroup objects to be run by this orchestrator
    # @param context - a Context object containing information needed at runtime
    # @return bool True means processing was successful, else false
    def run_tasks(self, list_of_task_groups, context):

        try:
            for task_group in list_of_task_groups:
                module_name = None
                list_of_task_config = task_group.list_of_task_config
                pool = Pool(len(list_of_task_config))  # start a worker process for each task in the group

                # The pool needs a list of the parameters to be passed to the execute function.
                # We need to collect them all by looping thru the list_of_task_config.
                task_params_list = []
                for task_config in list_of_task_config:
                    if module_name == None:
                        module_name = task_config.module_name
                    elif module_name != task_config.module_name:
                        print('Orchestrator.run_tasks() yaml file configuration error: all tasks grouped together to run in parallele must be the same type of module')
                        return False;
                    params_dict = task_config.params_dictionary
                    # task_params_list.append([{key_names.KEY_TASK_CONTEXT: context, key_names.KEY_TASK_PARAMS_DICTIONARY: params_dict}])
                    task_params_list.append([context, params_dict])

                # now, import the module by name and call the execute function via the multiprocessing pool
                module = importlib.import_module(module_name)   # import the module by name
                # module = __import__(module_name, fromlist=['non-empty-hack'])  # fromlist needs to be non-empty
                execute_function = getattr(module, "execute")
                pool.map(execute_function, task_params_list)

            return True
        except Exception as e:
            print e
            traceback.print_exc()
            return False
