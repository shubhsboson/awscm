def add_profile():
    pass

def edit_profile():
    pass

def get_aws_session(**kwargs):
    import boto3
    aws_session = boto3.session.Session(**kwargs)
    return aws_session

def get_aws_client(aws_session, service, region=None, **kwargs):
    aws_client = aws_session.client(service, region, **kwargs)
    return aws_client
