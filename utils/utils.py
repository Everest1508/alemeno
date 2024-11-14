from rest_framework.response import Response

def standard_response(status_code, message, data=None):
    response_structure = {
        "status_code": status_code,
        "message": message,
        "data": data if data is not None else {}
    }
    return Response(response_structure, status=status_code)
