import boto3, os, json

FROM_EMAIL_ADDRESS = 'iamjustinthecloud+customerservice@gmail.com'

ses = boto3.client('ses')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event))
    ses.send_email(Source=FROM_EMAIL_ADDRESS,
                   Destination={'ToAddresses': [event['email']]},
                   Message={'Subject': {'Data': 'Your reminder'},
                            'Body': {'Text': {'Data': event['message']}}
                            }
                   )
    return 'Email sent successfully!'
