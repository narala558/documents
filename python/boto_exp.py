import os

import boto
from boto.file import Key

# aws_access_key = os.environ.get('AWS_ACCESS_KEY')
# aws_secret_key = os.environ.get('AWS_SECRET_KEY')
# s3 = boto.connect_s3(aws_access_key, aws_secret_key)

aws_access_key='EVXUEBI94IM85PN9SZN3'
aws_secret_key='1l+ER5HKJBG8sLWwMWcWNzb4/l9+jzrQs+iE82aE'

s3 = boto.connect_s3(
    aws_access_key,
    aws_secret_key,
    host='http://localhost:9000'
)

bucket_name = 'test'

bucket = s3.create_bucket(bucket_name)
bucket = s3.get_bucket(bucket_name)


# upload file to s3
file_name = 'foo.txt'
key = bucket.new_key(file_name)
key.set_contents_from_filename(file_name)
key.set_acl('public-read')

bucket.copy_key(
    src_bucket_name='test-old',
    src_key_name='foo',
    new_key_name='bar',
)


# list all key objects
bucket.list()


# to get the top level directories:
bucket.list("", "/")


# to get the subdirectories of files
bucket.list("files/", "/")


# to check for a key
bucket.lookup('foo')


# keys
key = bucket.get_key('foo')
key = Key(bucket, 'foo.txt')
key = bucket.new_key('foo')

key.set_contents_from_filename('foo.txt')
key.get_contents_to_filename('f.py')


# download file from s3
key = bucket.get_key('foo.txt')
key.get_contents_to_filename('foo.txt')

# cli - count objects
# aws s3api list-objects --bucket BUCKETNAME --output json --query "[length(Contents[])]"
