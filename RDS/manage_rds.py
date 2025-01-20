import boto3

# Initialize RDS client
rds_client = boto3.client('rds')

# Create an RDS instance
def create_rds_instance():
    response = rds_client.create_db_instance(
        DBName='TestDB',
        DBInstanceIdentifier='test-db-instance',
        AllocatedStorage=20,
        DBInstanceClass='db.t2.micro',
        Engine='mysql',
        MasterUsername='admin',
        MasterUserPassword='yourpassword',  # Replace with a strong password
    )
    print(f'Created RDS Instance: {response["DBInstance"]["DBInstanceIdentifier"]}')

# Delete an RDS instance
def delete_rds_instance(instance_id):
    response = rds_client.delete_db_instance(
        DBInstanceIdentifier=instance_id,
        SkipFinalSnapshot=True
    )
    print(f'Deleted RDS Instance: {instance_id}')
