import boto3

# Initialize CloudWatch Logs client
logs_client = boto3.client('logs')

# Create a log group
def create_log_group(log_group_name):
    logs_client.create_log_group(logGroupName=log_group_name)
    print(f'Created Log Group: {log_group_name}')

# Create a log stream
def create_log_stream(log_group_name, log_stream_name):
    logs_client.create_log_stream(
        logGroupName=log_group_name,
        logStreamName=log_stream_name
    )
    print(f'Created Log Stream: {log_stream_name}')

# Push logs to the stream
def push_logs(log_group_name, log_stream_name, messages):
    log_events = [{'timestamp': int(time.time() * 1000), 'message': msg} for msg in messages]
    logs_client.put_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        logEvents=log_events
    )
    print(f'Pushed logs to {log_stream_name}')
