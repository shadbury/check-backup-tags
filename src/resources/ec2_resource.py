import boto3
from .aws_resource import AWSResource
from utils.tag_list import TagList

class EC2Resource(AWSResource):
    def __init__(self):
        super().__init__(boto3.client('ec2'))

    def list_resources(self):
        instances = self.client.describe_instances()
        all_instances = []
        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                all_instances.append(instance)
        return all_instances

    def has_backup_tag(self, instance):
        tags = instance.get('Tags', [])
        return any(tag['Key'] in TagList.list() for tag in tags)

    def apply_backup_tag(self, instance_id):
        keys = TagList.list_keys()
        self.client.create_tags(Resources=[instance_id], 
                                Tags=[{'Key': key, 'Value': value} for key, value in zip(keys, TagList.list())])
