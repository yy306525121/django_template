from rest_framework.response import Response
from rest_framework.views import exception_handler


class Rsp(Response):
    def __init__(self, code=1, data=None, msg='success'):
        self.response = {
            'code': code,
            'data': data,
            'msg': msg,
            'total': 0 if data is None else len(data)
        }
        super().__init__(data=self.response)

    @classmethod
    def success(cls, data):
        return cls(data=data)

    @classmethod
    def fail(cls, msg):
        return cls(code=0, msg=msg)


def custom_exception_handler(exc, context):
    """
    自定义异常处理器
    """
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
    if response is None and exc is not None:
        return Rsp.fail(str(exc))

    return response
