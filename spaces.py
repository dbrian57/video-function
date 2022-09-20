# Step 1: Import the all necessary libraries and SDK commands.
import os
import boto3

# Step 2: The new session validates your request and directs it to your Space's specified endpoint using the AWS SDK.
session = boto3.session.Session()
client = session.client('s3',
                        endpoint_url='https://nyc3.digitaloceanspaces.com', # Find your endpoint in the control panel, under Settings. Prepend "https://".
                        region_name='nyc3', # Use the region in your endpoint.
                        aws_access_key_id='C58A976M583E23R1O00N', # Access key pair. You can create access key pairs using the control panel or API.
                        aws_secret_access_key=os.getenv('SPACES_SECRET')) # Secret access key defined through an environment variable.

# Step 3: Call the put_object command and specify the file to upload.
client.put_object(Bucket='example-space-name/example-folder/', # The path to the directory you want to upload the object to, starting with your Space name.
                  Key='hello-world.txt', # Object key, referenced whenever you want to access this file later.
                  Body=b'Hello, World!', # The object's contents.
                  ACL='private', # Defines Access-control List (ACL) permissions, such as private or public.
                  Metadata={ # Defines metadata tags.
                      'x-amz-meta-my-key': 'your-value'
                  }
                )