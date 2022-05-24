import boto3

def S3_Resource():
    session = boto3.Session(
    aws_access_key_id='AKIA3L2SPHU7PZL2ZCW2',
    aws_secret_access_key='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'
    )

    #Creating S3 Resource From the Session.
    s3 = session.resource('s3')
    return s3