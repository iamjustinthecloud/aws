# Test the serverless stack

import pytest
from aws_cdk import App
from aws_cdk.assertions import Template
from serverless_stack import ServerlessStack


def test_ses_email_identities():
    app = App()
    stack = ServerlessStack(app, "ServerlessStack")
    template = Template.from_stack(stack)

    # Define the expected SES email addresses.
    expected_emails = [
        "iamjustinthecloud+customerservice@gmail.com",
        "iamjustinthecloud+customerservice@gmail.com"
    ]

    # check if the EmailIdenty resources are created with the expected properties.

    for email in expected_emails:
        template.has_resource_properties("AWS::SES::EmailIdentity", {"EmailIdentity": email})
