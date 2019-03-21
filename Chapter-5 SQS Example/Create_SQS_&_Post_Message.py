import boto3

# Get the service resource
sqs = boto3.resource('sqs')

def send_message_sqs():
    queue_url = None
    try:
        queue = sqs.get_queue_by_name(QueueName='my_test')
        queue_url = queue.url
        print(queue_url)
    except:
        if queue_url is None:
            # Create the queue. This returns an SQS.Queue instance
            queue = sqs.create_queue(QueueName='my_test', Attributes = {'DelaySeconds': '5'})
            # You can now access identifiers and attributes
            print("Queue created")
            print(queue.url)
            print(queue.attributes.get('DelaySeconds'))

    response = queue.send_messages(Entries=[{
    'Id': '1',
    'MessageBody': 'world'
    },
    {
    'Id': '2',
    'MessageBody': 'New message body',
    'MessageAttributes': {
    'Author': {
    'StringValue': 'Rahul Seth',
    'DataType': 'String'
    }}}
    ])
    # Print out any failures
    print(response.get('Failed'))


def lambda_handler(event, context):
    send_message_sqs()
    return 1
