from unittest.mock import Mock


def mock_return_discord_messages():
    expected_messages = [
        {
            'content': 'OVERRIDE This is a response with no attachments',
            'author': {'id': '123'},
            'attachments': []
        },
        {
            'content': 'OVERRIDE This is a response with a PNG attachment',
            'author': {'id': '789'},
            'attachments': [{'url': 'http://example.invalid/image.png'}]
        },
    ]
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = expected_messages
    return mock_response
