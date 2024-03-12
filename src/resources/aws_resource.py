class AWSResource:
    def __init__(self, client):
        self.client = client

    def list_resources(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    def has_backup_tag(self, resource):
        raise NotImplementedError("This method should be implemented by subclasses")

    def apply_backup_tag(self, resource):
        raise NotImplementedError("This method should be implemented by subclasses")
