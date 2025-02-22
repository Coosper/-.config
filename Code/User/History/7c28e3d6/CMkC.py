#! /usr/bin/env python3

import sys
import boto3

ec2 = boto3.resource('ec2')

REGION = "us-east-1"
AVAILABILITY_ZONE = "us-east-1a"
KEY_NAME = "CoosperKey"
AMI_ID = "ami-053a45fff0a704a47"
INSTANCE_TYPE = "t2.nano"

instance = ec2.create_instances(
    ImageId=AMI_ID,
    InstanceType=INSTANCE_TYPE, 
    KeyName=KEY_NAME,     
    MinCount=1,
    MaxCount=1,
    KeyName=KEY_NAME
)