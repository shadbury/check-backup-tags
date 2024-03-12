from enum import Enum

class TagList(Enum):
    Daily = 'Backup-Daily'
    Weekly = 'Backup-Weekly'
    Monthly = 'Backup-Monthly'
    Yearly = 'Backup-Yearly'

    @staticmethod
    def list():
        return [tag.value for tag in TagList]
    
    @staticmethod
    def list_keys():
        return [tag.name for tag in TagList]
