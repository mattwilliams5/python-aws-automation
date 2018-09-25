# coding: utf-8
import boto3

session = boto3.Session(profile_name='default')
s3 = session.resource('s3')
for l in s3.buckets.all():
      print(l)

new_bucket = s3.create.bucket(Bucket='mysanfrancloudbucketfam')
for l in s3.buckets.all():
      print(l)


ec2_client = session.client('ec2')
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('save', 'ipysession.py 1-10')
