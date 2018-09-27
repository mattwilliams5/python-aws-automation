import boto3
import click

session = boto3.Session(profile_name='mdw')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass

@cli.command('list-buckets')
def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-buckets-objects')
@click.argument('bucket')
def list_buckets_objects(bucket):
    "List objects in s3 bucket"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)

@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    "Create and configure S3 bucket"
    s3_bucket = s3.create_bucket(
        Bucket= bucket,
        CreateBucketConfiguration={'LocationConstraint': session.region_name}
    )

    policy = """
    {
      "Version":"2012-10-17",
      "Statement":[{
      "Sid":"PublicReadGetObject",
      "Effect":"Allow",
	  "Principal": "*",
          "Action":["s3:GetObject"],
          "Resource":["arn:aws:s3:::%s/*"
          ]
        }
      ]
    }
    """ % s3_bucket.name
    policy = policy.strip()

    pol = s3_bucket.Policy()
    pol.put(Policy=policy)

    ws = s3_bucket.Website()
    ws.put(WebsiteConfiguration={
       'ErrorDocument': {
           'key': 'error.html'
       },
       'IndexDocument':{
           'Suffix': 'index.html'
       }
    })

    return
    #url = "http://%s.s3.us-east-2.amazonaws.com" % s3_bucket.name


if __name__ == '__main__':
    cli()
