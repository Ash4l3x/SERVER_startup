DEFAULT_REQUEST_SIZE = 4
DEFAULT_STRING_SIZE = 1024
DEFAULT_CHUNK_SIZE = 4096

EOF_TRANSFER = "><EOF><"
EOFLEN = len(EOF_TRANSFER)

MAX_CLIENTS = 4

CLIENT_SIDE_REQUEST = "0x01"
SERVER_SIDE_REQUEST = "0x02"
CLOSE = "0x03"

ERROR = "0xff"
ACKWNOLDEGE = "0x00"

TESTING = "0xaa"

class REQUEST_TYPES:
    FILE_PUT_REQUEST = "0x10"
    FILE_PUT_TEMPLATE = {
        "request_name" : "file_put",
        "save_to_path" : "",
        "save_as_filename" : ""
    }

    FILE_GET_REQUEST = "0x11"
    FILE_GET_TEMPLATE = {
        "request_name" : "file_get",
        "path" : "",
        "filename" : ""
    }

    PATHFINDER_REQUEST = "0x12"
    PATHFINDER_TEMPLATE = {
        "request_name" : "pathfinder",
        "base_directory" : "",
        "subpaths" : {}
    }

    RUNCOMMAND_REQUEST ="0x13"
    RUNCOMMAND_TEMPLATE = {
        "request_name" : "rundcommand",
        "command" : "", 
        "terminal" : "", 
        "__default__terminal" : "cmd.exe"
    }

    RETURN_RESPONSE_REQUEST = "0x14"
    RETURN_RESPONSE_TEMPLATE= {
        "request_name" : "return_response",
        "response_str" : ""
    }

DEFAULT_INCOMING_PATH = "./incoming"