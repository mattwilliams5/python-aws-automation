import boto3

# This is the shell of my s3 bucket script. Just for fun and refreshing
# my s3 skills. This will be built out more.

def buckets():
    s3 = boto3.resource('s3')
    # Get all buckets in s3

    for bucket in s3.buckets.all():
        print(bucket.name)
