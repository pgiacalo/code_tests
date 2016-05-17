import key_names

def execute(context_and_task_params):
    """Reads a binary log file and puts the binary data into the given context object using the key from the task_params"""

    # context = context_and_task_params[key_names.KEY_TASK_CONTEXT]
    # task_params = context_and_task_params[key_names.KEY_TASK_PARAMS_DICTIONARY]

    context = context_and_task_params[0]
    task_params = context_and_task_params[1]

    log_file_path = task_params[key_names.KEY_LOG_FILE_PATH]
    binary_data_key_name = task_params[key_names.KEY_BINARY_LOG_DATA]

    f = open(log_file_path, 'rb')
    binary_data = f.read()
    f.close()

    context.set_value(binary_data_key_name, binary_data)

    print('log_file_reader ========FINISHED========== log_file_path', log_file_path)
    print('log_file_reader, binary byte count', len(binary_data))
