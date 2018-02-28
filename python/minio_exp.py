import minio

mc = minio.Minio(
    endpoint='0.0.0.0:9000',
    access_key='EVXUEBI94IM85PN9SZN3',
    secret_key='1l+ER5HKJBG8sLWwMWcWNzb4/l9+jzrQs+iE82aE',
    secure=False,
)

print([i.name for i in mc.list_buckets()])


bucket = 'blackhole'


# mc.remove_bucket(bucket)

if not mc.bucket_exists(bucket):
    mc.make_bucket(bucket)

mc.set_bucket_policy(bucket, '', minio.policy.Policy.READ_WRITE)


file_key = 'test'

path = 'test.txt'

obj = mc.fput_object(bucket, str(file_key), path)

# print(mc.get_bucket_policy(bucket))

print('done', '\n\n')
