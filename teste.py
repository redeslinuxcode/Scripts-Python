import boto3
import os
import shutil

sts_client = boto3.client('sts')

assumed_role_object=sts_client.assume_role(
    RoleArn="arn:aws:iam::613036180535:role/AssumeRoleTeste",
    RoleSessionName="AssumeRoleSession",
    ExternalId="123"
    
)
credentials=assumed_role_object['Credentials']

s3_resource=boto3.client(
    's3',
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'],
    aws_session_token=credentials['SessionToken'],
    
)

s3_resource.upload_file (   
    "./teste.txt" ,
    "bkt-gustavo-martins",
    "new_file3.csv",

)

source = r'C:\\Users\\robert.barros\\Desktop\\caminho-raiz\\'
destination = r'C:\\Users\\robert.barros\Desktop\\caminho-novo\\'
files = os.listdir(source)

try:
    os.mkdir(destination)
except FileExistsError as e:
    print(f'Pasta {destination} ja existe')

for file in files:
    new_path = shutil.move(f"{source}/{file}", destination)
    print(new_path)





