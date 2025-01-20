import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Create a new S3 bucket
def create_bucket(bucket_name):
    s3.create_bucket(Bucket=bucket_name)
    print(f'Bucket created: {bucket_name}')

# Upload a file to the bucket
def upload_file(bucket_name, file_name):
    s3.upload_file(file_name, bucket_name, file_name)
    print(f'Uploaded {file_name} to {bucket_name}')

# List all objects in a bucket
def list_objects(bucket_name):
    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        print(f'Objects in {bucket_name}:')
        for obj in response['Contents']:
            print(f" - {obj['Key']}")
    else:
        print(f'No objects found in {bucket_name}')
