import boto3
from .aws_resource import AWSResource
from utils.tag_list import TagList

class EBSResource(AWSResource):
    def __init__(self):
        super().__init__(boto3.client('ec2')) 

    def list_resources(self):
        volumes = self.client.describe_volumes()
        return volumes['Volumes']

    def has_backup_tag(self, volume):
        tags = volume.get('Tags', [])
        return any(tag['Key'] in TagList.list() for tag in tags)

    def apply_backup_tag(self, volume_id):
        keys = TagList.list_keys()
        self.client.create_tags(Resources=[volume_id], 
                                Tags=[{'Key': key, 'Value': value} for key, value in zip(keys, TagList.list())])
