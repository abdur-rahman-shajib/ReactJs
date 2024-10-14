from django.http import JsonResponse

from tourmate.db import LocalSession


class SQLAlchemyDBSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.db_session = LocalSession()
        response = self.get_response(request)
        LocalSession.remove()
        return response

    def process_exception(self, request, exception):
        request.db_session.rollback()
        print(exception)
        response_data = {
            'error': 'An unexpected error occured in server while processing the data.'
        }
        LocalSession.remove()
        return JsonResponse(response_data, status=500)