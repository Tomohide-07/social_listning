import json
import boto3
from config import MODEL_ID, AWS_REGION

bedrock = boto3.client('bedrock', region_name=AWS_REGION)


def analyze_sentiments(texts: list[str]) -> list[str]:
    """
    Invoke AWS Bedrock Nova Micro/Lite to classify each text as POSITIVE or NEGATIVE.
    """
    labels = []
    for text in texts:
        payload = {"input": text, "attributes": ["sentiment"]}
        resp = bedrock.invoke_model(
            modelId=MODEL_ID,
            contentType='application/json',
            accept='application/json',
            body=json.dumps(payload)
        )
        result = json.loads(resp['body'])
        label = result['predictions'][0]['sentiment']
        labels.append(label)
    return labels