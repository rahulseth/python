import boto3

if __name__ == '__main__':
    session = boto3.Session(profile_name='developer')
    s3 = session.resource('s3')
    my_bucket = s3.Bucket('sqsrahul')
    for object in my_bucket.objects.all():
        print(object)
