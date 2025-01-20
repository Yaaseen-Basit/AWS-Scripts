import boto3

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')

# Create a DynamoDB table
def create_table():
    table = dynamodb.create_table(
        TableName='TestTable',
        KeySchema=[
            {'AttributeName': 'id', 'KeyType': 'HASH'}  # Partition key
        ],
        AttributeDefinitions=[
            {'AttributeName': 'id', 'AttributeType': 'S'}
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    print(f'Created Table: {table.table_name}')

# Insert an item into the table
def insert_item(table_name, item):
    table = dynamodb.Table(table_name)
    table.put_item(Item=item)
    print(f'Inserted item: {item}')

# Query items from the table
def query_items(table_name, key):
    table = dynamodb.Table(table_name)
    response = table.get_item(Key=key)
    print(f'Query result: {response.get("Item")}')
