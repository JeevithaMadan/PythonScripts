import boto3
import logging
from botocore.exceptions import ClientError
import json

class BucketPolicy:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
    
    def is_bucket_exist(self, bucket_name):
        s3_client = boto3.client('s3')
        response = s3_client.list_buckets()
        for bucket in response['Buckets']:
            if bucket['Name'] == self.bucket_name:
                return True
                break
    
    def get_bucket_policy(self, bucket_name):
        s3_client = boto3.client('s3')
        response = s3_client.get_bucket_policy(Bucket=self.bucket_name)
        print('\nBucket Policy for', self.bucket_name, '\n', response['Policy'])
    
    def put_bucket_policy(self, bucket_name):
        s3_client = boto3.client('s3')
        bucket_policy = {
            'Version': '2012-10-17',
            'Statement': [{
            'Sid': 'AddPerm',
            'Effect': 'Allow',
            'Principal': '*',
            'Action': ['s3:GetObject'],
            'Resource': "arn:aws:s3:::%s/*" % bucket_name
            }]
        }
        bucket_policy = json.dumps(bucket_policy)
        s3_client.put_bucket_policy(Bucket = self.bucket_name, Policy = bucket_policy)
        print('\nCreated new bucket policy for', self.bucket_name)
    
    def delete_bucket_policy(self, bucket_name):
        s3_client = boto3.client('s3')
        response = s3_client.delete_bucket_policy(Bucket=self.bucket_name)
        print('\nDelete bucket policy of', self.bucket_name)

if __name__ == '__main__':
    print('Bucket Policy Services')
    bucket_name = input('Enter the bucket name: ')
    bucketpolicy = BucketPolicy(bucket_name)

    if bucketpolicy.is_bucket_exist(bucket_name):
        bucketpolicy.put_bucket_policy(bucket_name)
        bucketpolicy.get_bucket_policy(bucket_name)
        bucketpolicy.delete_bucket_policy(bucket_name)
    else:
        print('Invalid Bucket Name, does not exist')
