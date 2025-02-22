#! /usr/bin/env python3

"""
Keep small children away from my code. 
It's so ugly it will eat them alive.
"""

# Setting up some stuff here
import sys
from turtle import clearscreen
import boto3
import os

# Some other stuff heeere
ec2 = boto3.resource('ec2')

# And some stuff here so I don't have to type it all the time
DEFAULT_AMI = "ami-053a45fff0a704a47"
INSTANCE_TYPE = "t2.nano"
AVAILABILITY_ZONE = "us-east-1a"
KEY_NAME = "CoosperKey2"
INSTANCE_NAME = "CoosperInstance"

# Clear the screen
clearscreen()

# User input for AMI
user_input = input("Do you want to use the default AMI? ( Yes / No ) ")

if user_input == "yes":
    AMI_ID = DEFAULT_AMI
elif user_input == "no":
    AMI_ID = input("Enter the AMI ID: ")
    print(f"Using custom AMI: {AMI_ID}")
else:
    print("Invalid input. Exiting...")
    sys.exit()




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

# Some helper methods
def clear_screen():
    os.system('clear')