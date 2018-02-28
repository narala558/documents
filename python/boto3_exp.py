import datetime as dt
import os

import boto3
import botocore.exceptions


ak = os.environ.get('AWS_ACCESS_KEY_ID')
sk = os.environ.get('AWS_SECRET_ACCESS_KEY')


host = 'http://localhost:9000'


session = boto3.session.Session()

s3_client = session.client(
    service_name='s3',
    aws_access_key_id=ak,
    aws_secret_access_key=sk,
    # endpoint_url=host,
)

s3 = boto3.resource(
    service_name='s3',
    aws_access_key_id=ak,
    aws_secret_access_key=sk,
    # endpoint_url=host,
)

client = s3_client

# r = client.list_buckets()
# buckets = [b['Name'] for b in r['Buckets']]
# print(buckets)

bucket_name = 'test-bucket'


bucket = s3.Bucket(bucket_name)
print(bucket)

now = dt.datetime.now(dt.timezone.utc)

last_required_date = now - dt.timedelta(days=4)


# delete old objects
for item in bucket.objects.all():
    if item.last_modified < last_required_date:
        bucket.delete_objects(Delete={'Objects': [{'Key': item.key}]})
    else:
        print(item.key, item.last_modified)


# check if bucket exists
try:
    client.head_bucket(Bucket=bucket)
except botocore.exceptions.ClientError:
    client.create_bucket(Bucket=bucket)

policy = client.get_bucket_policy(Bucket=buckets[0])
print(policy)


filename = key = 'test.txt'
client.upload_file(Filename='test.txt', Bucket=bucket, Key=key)

client.download_file(bucket, key, 'foo.txt')



# Connect to EC2
# ec2 = boto3.resource('ec2')

# # Get information for all running instances
# running_instances = ec2.instances.filter(Filters=[{
#     'Name': 'instance-state-name',
#     'Values': ['running']}])

import boto.ec2
conn = boto.ec2.connect_to_region("us-east-1")
statuses = conn.get_all_instance_status()
print(statuses)


import boto3
import botocore

s3 = boto3.resource('s3')
exists = False

try:
    s3.Object('my-bucket', 'dootdoot.jpg').load()
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        exists = False
    else:
        raise
else:
    exists = True

print(exists)
