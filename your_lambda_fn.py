from script import execute

def handler(event, context):  # pylint: disable=unused-argument
    """Events corresponds to params."""
    try:
        execute()
    except Exception as error:  # pylint: disable=broad-except
        raise error