DEFAULT_REQUEST_SIZE = 8
DEFAULT_STRING_SIZE = 1024
DEFAULT_CHUNK_SIZE = 4096

EOF_TRANSFER = "><EOF><"

MAX_CLIENTS = 4

CLIENT_SIDE_REQUEST = "0x01"
SERVER_SIDE_REQUEST = "0x02"
CLOSE = "0x03"

ERROR = "0xff"
ACKWNOLDEGE = "0x00"


TESTING = "0xaa"

class REQUEST_TYPES:
    FILE = {
        "request_name" : "file",
        "save_to_path" : "",
        "save_as_filename" : ""
    }

    PATHFINDER = {
        "request_name" : "pathfinder",
        "current_working_directory" : "", 
        "subpaths" : {}
    }

    RUNCOMMAND = {
        "request_name" : "rundcommand",
        "command" : "", 
        "terminal" : "", 
        "__default__terminal" : "cmd.exe"
    }

    RETURN_RESPONSE = {
        "request_name" : "return_response",
        "response_str" : ""
    }

    MESSAGE = {
        "request_name" : "message", 
        "string" : ""
    }

DEFAULT_INCOMING_PATH = "./incoming"