def manage_backup_tags(resource_manager):
    for resource in resource_manager.list_resources():
        resource_id = resource.get('InstanceId') or resource.get('DBInstanceIdentifier')
        resource_arn = resource.get('DBInstanceArn', '')

        if not resource_manager.has_backup_tag(resource):
            if resource_arn:
                resource_manager.apply_backup_tag(resource_arn)
            elif resource_id:
                resource_manager.apply_backup_tag(resource_id)
