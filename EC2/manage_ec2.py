import boto3

# Initialize EC2 resource
ec2 = boto3.resource('ec2')

# Launch an EC2 instance
def launch_instance():
    instance = ec2.create_instances(
        ImageId='ami-0abcdef1234567890',  # Replace with a valid AMI ID
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
        KeyName='your-key-pair',  # Replace with your key pair name
    )
    print(f'Launched Instance: {instance[0].id}')

# Stop an EC2 instance
def stop_instance(instance_id):
    ec2_client = boto3.client('ec2')
    ec2_client.stop_instances(InstanceIds=[instance_id])
    print(f'Stopped Instance: {instance_id}')

# Terminate an EC2 instance
def terminate_instance(instance_id):
    ec2_client = boto3.client('ec2')
    ec2_client.terminate_instances(InstanceIds=[instance_id])
    print(f'Terminated Instance: {instance_id}')
