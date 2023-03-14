import os

class Config(object):
    
    BOT_TOKEN = "6043283784:AAHLV11M9g3gaDj5dE-Sr5fKhSCd8CT-lOc"
    
    API_ID = 7143337
    
    API_HASH = "1afa55a5f3bf7058c843d1b290f79c49"
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 0
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "1284818583"))

    SESSION_NAME = "uploaderMar_bot"
    
    MAX_RESULTS = "50"
