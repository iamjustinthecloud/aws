# Test the app.py file

from app import initialize_app


def test_app_contains_serverless_stack():
    app = initialize_app()
    assert len(app.synth().stacks) > 0
