import boto3, sys
import click

@click.command()
@click.argument('name',default="DEMO")

def list_object(name):
    "List S3 objects"
    click.echo('this is {}'.format(name))
    session = boto3.Session(profile_name='developer')
    s3 = session.resource('s3')
    my_bucket = s3.Bucket('sqsrahul')
    for object in my_bucket.objects.all():
        print(object)

if __name__ == '__main__':
    #print(sys.argv)
    list_object()
