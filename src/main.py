from resources.ec2_resource import EC2Resource
from resources.rds_resource import RDSResource
from utils.backup_manager import manage_backup_tags

def main():
    ec2_manager = EC2Resource()
    rds_manager = RDSResource()

    manage_backup_tags(ec2_manager)
    manage_backup_tags(rds_manager)

if __name__ == "__main__":
    main()
