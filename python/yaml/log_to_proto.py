import sys
import struct
import key_names

sys.path.append('../common')
import sync_messages

def execute(context_and_task_params):
    """
    Gets the binary log data from the given context object and converts it to a list of protobuf objects.
    This function converts a vehicle's binary log data into a list of protobuf objects.
    The resulting list of protobuf objects is returned by putting it in the given context object.
    """

    # context = context_and_task_params[key_names.KEY_TASK_CONTEXT]
    # task_params = context_and_task_params[key_names.KEY_TASK_PARAMS_DICTIONARY]

    context = context_and_task_params[0]
    task_params_dictionary = context_and_task_params[1]


    # we need to generate the itc_to_proto code at runtime
    message_definition_file_path = context[key_names.KEY_MESSAGE_DEFINITION_FILE_PATH]
    print(message_definition_file_path)
    message_generator = sync_messages.MessageParser(exit_if_shas_match=False, stork_messages_filename=message_definition_file_path, inside_docker=True)
    message_generator.parse()

    import itc_to_proto

    # get all the log data from the given context (one vehicle's log data)
    list_of_list_of_bytes = context[key_names.KEY_BINARY_LOG_DATA]

    # a dictionary will hold ALL of the converted messages, with lookup by message_name
    protobufs_dictionary = {}

    for binary_log_file in list_of_list_of_bytes:
        while len(binary_log_file) > 0:
            # the first 4 bytes contain the msg_id
            msg_id = struct.unpack('>I', binary_log_file[0:4])[0]
            print "MSG ID: " + str(msg_id) + ", len = " + str(len(binary_log_file))

            # we need to remove the bytes carrying the msg_id before calling itc_to_proto() below
            msg_start = binary_log_file[4:]

            # now call itc_to_proto.itc_to_proto() to convert the binary data to a protobuf object.
            # this pops off the associated bytes from the binary_data, and returns the protobuf object.
            protobuf_obj, bytes_consumed = itc_to_proto.itc_to_proto(msg_id, msg_start)
            print(protobuf_obj)
            if protobuf_obj is None:
                binary_log_file = binary_log_file[1:]
                continue

            binary_log_file = binary_log_file[4+bytes_consumed:]

            message_type = protobuf_obj.itc_message.itc_name
            if message_type in protobufs_dictionary:
                protobufs_dictionary[message_type].append(protobuf_obj)
            else:
                protobufs_dictionary[message_type] = [protobuf_obj]

    # now that we've got all the protobuf objects, we'll put them in the context
    context.proto_logs.add(protobufs_dictionary)

