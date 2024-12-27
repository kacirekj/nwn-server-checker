import boto3


bucket_name = 'nwn-server-checker-bucket'
s3 = boto3.client('s3')


def save_image_public(file_name, data):
    return s3.put_object(Bucket=bucket_name, Key=file_name, Body=data, ContentType='image/png', ACL='public-read')


def find(file_name):
    return s3.get_object(Bucket=bucket_name, Key=file_name)['Body'].read()

