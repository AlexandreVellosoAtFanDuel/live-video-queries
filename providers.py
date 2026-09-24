from enum import Enum
from sports import Sport

class Provider(Enum):
    PERFORM_V2_OTHER=31
    BETRADAR_V2=33
    BETRADAR_V3=34
    IMG_GOLF=36
    PERFORM_MCC_VIDEO=38
    GENIUS=40

class ProviderClass:
    
    def __init__(self, id, provider_sports_type):
        self.id = id
        self.provider_sports_type
