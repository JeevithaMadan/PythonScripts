import boto3
import logging
from botocore.exceptions import ClientError
import sys

class AWSService:
    def __init__(self, bucket_name, region = None):
        self.bucket_name = bucket_name
        self.region = region

    def create_bucket(self):
        try:
            print(self.region)
            if self.region is None:
                s3_client = boto3.client('s3')
                s3_client.create_bucket(Bucket = self.bucket_name)
                print(self.bucket_name, ' is created in default region.')
            else:
                s3_client = boto3.client('s3', region_name = self.region)
                location = {'LocationConstraint': self.region}
                s3_client.create_bucket(Bucket = self.bucket_name,
                                                CreateBucketConfiguration = location)
                print('{0} is created in region {1}'.format(self.bucket_name,self.region))
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def is_bucket_exist(self, bucket_name):
        s3_client = boto3.client('s3')
        response = s3_client.list_buckets()
        for bucket in response['Buckets']:
            if bucket['Name'] == self.bucket_name:
                return True
                break

    def upload_file(self, file_name, bucket_name, object_name = None):
        try:
            if object_name is None:
                object_name = file_name
            s3_client = boto3.client('s3')
            print(file_name,self.bucket_name,object_name)
            s3_client.upload_file(file_name, self.bucket_name, object_name )
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def download_file(self, bucket_name, object_name, file_name):
        try:
            s3_client = boto3.client('s3')
            s3_client.download_file(self.bucket_name, object_name, file_name )
        except ClientError as e:
            logging.error(e)
            return False
        return True

if __name__ == '__main__':
    print('AWS Basic Services are')
    print('1. Create Bucket\n2. Uploading files to Bucket\n3. Downloading files from Bucket\n4. Exit')
    try:
        action = int(input('Enter the option: '))

        if action == 1:
            bucket_name = input('Enter the s3 bucket name: ')
            region = input('Enter "None" for Default region.\nEnter region name: ')
            if region == 'None':
                awsservice = AWSService(bucket_name)
            else:
                awsservice = AWSService(bucket_name, region)
            if awsservice.create_bucket():
                print('Bucket created...')
            else:
                print('Error while creating s3 bucket')

        elif action == 2:
            bucket_name = input('Enter the s3 bucket name: ')
            file_name = input('Enter the filename to upload: ')
            awsservice = AWSService(bucket_name)
            if awsservice.is_bucket_exist(bucket_name):
                if awsservice.upload_file(file_name, bucket_name):
                    print('Uploaded file into the s3 bucket')
                else:
                    print('Error while uploading file to the s3 bucket')
            else:
                print('Invalid Bucket Name does not exist')

        elif action == 3:
            bucket_name = input('Enter the s3 bucket name: ')
            object_name = input('Enter the objectname to download: ')
            file_name = input('Enter the file path to save: ')
            awsservice = AWSService(bucket_name)
            if awsservice.is_bucket_exist(bucket_name):
                if awsservice.download_file(bucket_name,object_name, file_name):
                    print('Downloaded file from the s3 bucket')
                else:
                    print('Error while downloading file into the s3 bucket')
            else:
                print('Invalid Bucket Name does not exist')

        elif action == 4:
            print('Exit from script')
            sys.exit()

        else:
    	    print('Invalid input entered, Please try again')
    except ValueError as error:
        print('Value Error: ',error)
