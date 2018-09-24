import boto3

# Quick add a username, access and secret keys, add to Group
# and remove all of the above

def iam_add():
    iam = boto3.client('iam')

    # Add user to system

    iam.create_user(
        UserName='UserName'
    )

    iam.create_login_profile(
        UserName='UserName',
        Password='Combat123!@#'
    )

    result = iam.create_access_key(
    UserName='UserName'
    )

    print(result)

    # Add user into system-admins group

    iam.add_user_to_group(
    GroupName='system-admins',
    UserName='UserName'
    )

# Remove Usuer
def iam_remove():
    iam = boto3.client('iam')

    # Delete your IAM username
    iam.delete_access_key(
    UserName='UserName',
    AccessKeyId='AKIAJI4AFLCIVMCU2IEA'
    )

    # Remove user from group

    iam.remove_user_from_group(
        GroupName='system-admins',
        UserName='UserName'
    )

    # Finally completely remove user from system

    iam.delete_login_profile(
    UserName='UserName'
    )

    iam.delete_user(
        UserName='UserName'
    )

    print('Message: Removal complete')

iam_add()
