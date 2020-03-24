import boto3
import logging
from botocore.exceptions import ClientError
import json
import copy

class BucketACL:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
    
    def is_bucket_exist(self, bucket_name):
        s3_client = boto3.client('s3')
        response = s3_client.list_buckets()
        for bucket in response['Buckets']:
            if bucket['Name'] == self.bucket_name:
                return True
                break
    
    def get_bucket_acl(self, bucket_name):
        s3_client = boto3.client('s3')
        response = s3_client.get_bucket_acl(Bucket = self.bucket_name)
        print('\nGet Bucket ACL for', self.bucket_name, '\n', response['Grants'])
    
    def put_bucket_acl(self, bucket_name):
        s3_client = boto3.client('s3')
        AccessControlPolicy={
            'Grants': [
                {
                    'Grantee': {
                        'DisplayName': 'jeevitha.madan',
                        'ID': 'ad0a15b95ffc3619ffad7338dc5b6f0bc955c9258d395c1da3c8ac5e9cc6e668',
                        'Type': 'CanonicalUser',
                    },
                    'Permission': 'FULL_CONTROL'
                },
            ],
            'Owner': {
                 'DisplayName': 'jeevitha.madan',
                 'ID': 'ad0a15b95ffc3619ffad7338dc5b6f0bc955c9258d395c1da3c8ac5e9cc6e668'
            }
        }
        try:
            response = s3_client.put_bucket_acl(
                Bucket=self.bucket_name,
                AccessControlPolicy=AccessControlPolicy
            )
        except ClientError as e:
            logging.error(e)
            return False
        print('\nCreated ACL for the Bucket', self.bucket_name)
        return True

if __name__ == '__main__':
    print('Bucket ACL')
    bucket_name = input('Enter the bucket name: ')
    bucketaclobj = BucketACL(bucket_name)

    if bucketaclobj.is_bucket_exist(bucket_name):
        bucketaclobj.put_bucket_acl(bucket_name)
        bucketaclobj.get_bucket_acl(bucket_name)
    else:
        print('Invalid Bucket Name, does not exist')
