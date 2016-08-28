# Import necessary packages
import boto3
import os


# Create AWS sesison
session = boto3.Session(
                        aws_access_key_id=os.environ["ACCESS_KEY"],
                        aws_secret_access_key=os.environ["SECRET_KEY"]
                       )

# Define path to bucket
s3 = session.resource('s3')
bucket = s3.Bucket('t206')

key = bucket.objects.filter(Prefix='cv').get_key('data.h5')
key.get_contents_to_filename('~/Desktop/works.h5')#
