import os

MODEL_ID   = os.getenv('BEDROCK_MODEL_ID', 'amazon.titan-nova-micro')
AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')