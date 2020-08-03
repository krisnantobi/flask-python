class BaseController(object):
    @staticmethod
    def _response(
        status: int = 200,
        message: str = 'Ok',
        data: dict = {}
        )->dict:
        return {
            'meta' : {
                'status': status,
                'message': message
            },
            'data' : data
        }