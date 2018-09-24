import boto3

# The shell of my ec2 script This will be built out more.

def ec2_check():
    # check all instances and their status in ec2
    ec2 = boto3.resource('ec2')
    instances = ec2.instances.filter(
                                     Filters=[{'Name': 'instance-state-name',
                                     'Values': ['terminated']}])

    for instance in instances:
        print(instance.id, instance.instance_type)

    for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
        print(status)
