#! /usr/bin/env python3

"""
Keep small children away from my code. 
It's so ugly it will eat them alive.
"""

# Setting up some stuff here
import sys
import boto3
import botocore
import os

# Some other stuff heeere
ec2_resource = boto3.resource("ec2")
ec2_client = boto3.client("ec2")

# And some stuff here so I don't have to type it all the time
DEFAULT_AMI = "ami-053a45fff0a704a47"
INSTANCE_TYPE = "t2.nano"
AVAILABILITY_ZONE = "us-east-1a"
KEY_NAME = ""
INSTANCE_NAME = ""

# Clear the screen
os.system("clear")

# User input for name.
print("Please enter a name for the instance: ")
name_input = input("==> ")
if name_input == "":
    print("You must enter a name for the instance")
    sys.exit()
else:
    INSTANCE_NAME = name_input

# User input for the key name.
print("Please enter the name of the key pair you want to use.")
key_input = input("==> ")
try:
    ec2_client.describe_key_pairs(KeyNames=[key_input])
    print(f"Key pair {key_input} exists and will be used.")
    KEY_NAME = key_input
except botocore.exceptions.ClientError as e:
    # The pain that is reading AWS EC2 documentation... In this case, API Reference
    # https://docs.aws.amazon.com/AWSEC2/latest/APIReference/errors-overview.html#api-error-codes-table
    if e.response["Error"]["Code"] == "InvalidKeyPair.NotFound":
        print(f"Key pair {key_input} does not exist.")
        sys.exit(1)
    else:
        raise

# Create the instance
instance = ec2_resource.create_instances(
    ImageId=DEFAULT_AMI,
    InstanceType=INSTANCE_TYPE,
    KeyName=KEY_NAME,
    MinCount=1,
    MaxCount=1,
    Placement={
        "AvailabilityZone": AVAILABILITY_ZONE,
    },
    TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": INSTANCE_NAME,
                },
            ],
        },
    ],
)

print()
print(f"Instance created!")
print(f"Instance ID:{instance[0].id} ")
print(f"Instance Name: {INSTANCE_NAME}")
print()
print(f"Waiting for instance to be running...")

instance[0].wait_until_running()
instance[0].reload()

print()
print(f"Instance is running: {instance[0].id}")
print(f"Instance Name: {INSTANCE_NAME}")
