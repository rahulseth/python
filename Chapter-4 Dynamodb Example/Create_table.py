import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

def create_dynamodb_table():
    try:
        # Create the table
        table = dynamodb.create_table(
        TableName='employee',
        KeySchema=[
        {
        'AttributeName': 'emp_id',
        'KeyType': 'HASH'
        },{
        'AttributeName': 'first_name',
        'KeyType': 'RANGE'
        }],
        AttributeDefinitions=[
        {
        'AttributeName': 'emp_id',
        'AttributeType': 'S'
        },{
        'AttributeName': 'first_name',
        'AttributeType': 'S'
        }],
        ProvisionedThroughput = {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
        })
    except:
        print("An exception occurred")
    else:
        # Wait until the table exists.
        table.meta.client.get_waiter('table_exists').wait(TableName='employee')
        # Print out some data about the table.
        print("Table created successfully")


def lambda_handler(event, context):
    create_dynamodb_table()
    return "Done"
