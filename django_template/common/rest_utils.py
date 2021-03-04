from rest_framework.response import Response

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
