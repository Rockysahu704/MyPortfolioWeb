from rest_framework.views import exception_handler
from rest_framework.response import Response


def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is not None:

        response.data = {
            "success": False,
            "message": get_error_message(response),
            "errors": response.data,
        }

    return response


def get_error_message(response):

    if response.status_code == 400:
        return "Validation failed."

    if response.status_code == 401:
        return "Authentication credentials were not provided."

    if response.status_code == 403:
        return "You do not have permission to perform this action."

    if response.status_code == 404:
        return "Resource not found."

    return "An error occurred."