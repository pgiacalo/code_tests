import threading


# This is generic holder class of context information.
# An internal dictionary is provided to carry name: value pairs.
# The following thread safe functions are provided for clients using the dictionary. 
#	get_value(), set_value(), and delete_value() functions are used

# TODO - how will we handle race conditions across multiple processes? If a mutex is used below, then the following error is thrown: TypeError: can't pickle thread.lock objects
class Context:
    def __init__(self):
        self.dictionary = {}
        # self.mutex = threading.RLock()

    def __getitem__(self, item):
        return self.dictionary[item]

    def get_value(self, key):
        # with self.mutex:
            return self.dictionary[key]

    def set_value(self, key, value):
        # with self.mutex:
            self.dictionary[key] = value

    def delete_value(self, key):
        # with self.mutex:
            del self.dictionary[key]
