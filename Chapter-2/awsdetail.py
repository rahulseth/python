import boto3

if __name__ == '__main__':
    session = boto3.Session(profile_name='awsdetail')
    ec2 = session.resource(ec2)
    for i in ec2.inatances.all():
        print(i)
