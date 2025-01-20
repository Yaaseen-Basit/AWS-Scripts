import boto3
import zipfile

# Initialize Lambda client
lambda_client = boto3.client('lambda')

# Deploy a Lambda function
def deploy_lambda(function_name, zip_file_path, role_arn, handler):
    with open(zip_file_path, 'rb') as f:
        zipped_code = f.read()

    response = lambda_client.create_function(
        FunctionName=function_name,
        Runtime='python3.9',
        Role=role_arn,  # Replace with your IAM role ARN
        Handler=handler,
        Code={'ZipFile': zipped_code},
        Timeout=15,
        MemorySize=128,
    )
    print(f'Deployed Lambda Function: {function_name}')

# Invoke the Lambda function
def invoke_lambda(function_name, payload):
    response = lambda_client.invoke(
        FunctionName=function_name,
        InvocationType='RequestResponse',
        Payload=payload.encode()
    )
    print(f'Lambda Response: {response["Payload"].read().decode()}')
