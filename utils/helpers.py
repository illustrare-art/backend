from users.models import User


def get_first_matching_attr(obj, *attrs, default=None):
    for attr in attrs:
        if hasattr(obj, attr):
            return getattr(obj, attr)

    return default


def get_error_message(exc) -> str:
    if hasattr(exc, "message_dict"):
        return exc.message_dict
    error_msg = get_first_matching_attr(exc, "message", "messages")

    if isinstance(error_msg, list):
        error_msg = ", ".join(error_msg)

    if error_msg is None:
        error_msg = str(exc)

    return error_msg


def jwt_response_payload_handler(token, user: User = None, request=None):
    return {
        "token": token,
        "requested_user": {
            "name": user.name,
            "email": user.email,
        },
    }
