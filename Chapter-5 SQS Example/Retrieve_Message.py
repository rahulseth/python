import boto3
import json

# Get the service resource
sqs = boto3.resource('sqs')

def receive_message_sqs():
    queue_url = None
    #message_bodies = []
    messages_to_delete = []

    queue = sqs.get_queue_by_name(QueueName='my_test')
    while True:
        response = queue.receive_messages(MaxNumberOfMessages = 10)
        for message in response:
            body = message.body
            messages_to_delete.append({
            'Id': message.message_id,
            'ReceiptHandle': message.receipt_handle
            })
            print(body)
        if len(messages_to_delete) == 0:
            break
        else:
            delete_response = queue.delete_messages(
            Entries=messages_to_delete)


def lambda_handler(event, context):
    receive_message_sqs()
    return 1
