#! /usr/bin/env python3

import sys
import boto3

ec2 = boto3.resource('ec2')


AMI_ID = "ami-053a45fff0a704a47"
INSTANCE_TYPE = "t2.nano"
AVAILABILITY_ZONE = "us-east-1a"
KEY_NAME = "CoosperKey"



instance = ec2.create_instances(
    ImageId=AMI_ID,
    InstanceType=INSTANCE_TYPE, 
    KeyName=KEY_NAME,     
    MinCount=1,
    MaxCount=1,
    Placement={
        'AvailabilityZone': AVAILABILITY_ZONE,
    },
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'CoosperInstance'
                },
            ]
        },
    ],
)
print (instance[0].id)