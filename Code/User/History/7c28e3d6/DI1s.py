#! /usr/bin/env python3

"""
Keep small children away from my code. 
It's so ugly it will eat them alive.
"""

# Setting up some stuff here
import sys
import boto3
import os

# Some other stuff heeere
ec2 = boto3.resource('ec2')
ec2 = boto3.client('ec2')

# And some stuff here so I don't have to type it all the time
DEFAULT_AMI = "ami-053a45fff0a704a47"
INSTANCE_TYPE = "t2.nano"
AVAILABILITY_ZONE = "us-east-1a"
KEY_NAME = ""
INSTANCE_NAME = ""

# Clear the screen
os.system('clear')

# User input for name.
name_input = input("Please enter a name for the instance: ")
if name_input == "":
    print("You must enter a name for the instance")
    sys.exit()
else:
    INSTANCE_NAME = name_input

# User input for the key name.
key_input = input("Please enter the key name: ")
try:
    ec2.describe_key_pairs(KeyNames=[key_input])
    print(f"Key pair {key_input} exists and will be used.")
except ec2.exceptions.InvalidKeyPair_NotFound:
    print(f"Key pair {key_input} does not exist.")
    sys.exit(1)

    
    




instance = ec2.create_instances(
    ImageId=DEFAULT_AMI,
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
