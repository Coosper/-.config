#! /usr/bin/env python3

import sys
import boto3

ec2 = boto3.resource('ec2')


AMI_ID = "ami-053a45fff0a704a47"
INSTANCE_TYPE = "t2.nano"
AVAILABILITY_ZONE = "us-east-1a"
KEY_NAME = "CoosperKey"
INSTANCE_NAME = "CoosperInstance"



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
                    'Value': INSTANCE_NAME,
                },
            ]
        },
    ],
)

print(
    f"Instance created: {instance[0].id} "
    f"Instance Name: {INSTANCE_NAME}"
)

print(
    f"Waiting for instance to be running..."
    )

instance[0].wait_until_running()
instance[0].reload()

print(
    f"Instance is running: {instance[0].id}  " 
    f"Instance Name: {INSTANCE_NAME}"
      )

