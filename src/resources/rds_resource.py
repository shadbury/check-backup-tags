import boto3
from .aws_resource import AWSResource
from utils.tag_list import TagList

class RDSResource(AWSResource):
    def __init__(self):
        super().__init__(boto3.client('rds'))

    def list_resources(self):
        instances = self.client.describe_db_instances()
        return instances['DBInstances']

    def has_backup_tag(self, instance):
        tags = self.client.list_tags_for_resource(ResourceName=instance['DBInstanceArn'])['TagList']
        return any(tag['Key'] in TagList.list() for tag in tags)

    def apply_backup_tag(self, instance_arn):
        keys = TagList.list_keys()
        print(f"Keys {keys}")
        self.client.add_tags_to_resource(ResourceName=instance_arn, 
                         Tags=[{'Key': key, 'Value': value} for key, value in zip(keys, TagList.list())])
