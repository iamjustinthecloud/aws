#!/usr/bin/env python3

from aws_cdk import App

from serverless_stack import ServerlessStack


def initialize_app():
    app = App()
    ServerlessStack(app, "ServerlessStack")
    return app


if __name__ == "__main__":  # pragma: no cover
    app = initialize_app()
    app.synth()
