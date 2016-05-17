import context

# This class is an extension of the Context class. 
# It adds the field _flight_logs to hold all of the raw flight log data
# This additional field was included as a design decision, rather than 
# using the Dictionary provided in the base class to carry this data. 

class FlightLogContext_(context.Context):

	def __init__(self, flight_logs, message_definition_file_path):
        # flight_logs contains the raw binary data
		self.flight_logs = flight_logs

        # proto logs contains the converted protobuf data
		self.proto_logs = None

		self.message_definition_file_path = message_definition_file_path

