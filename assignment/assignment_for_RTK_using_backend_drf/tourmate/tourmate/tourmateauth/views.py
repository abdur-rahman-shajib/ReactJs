from sqlalchemy.exc import IntegrityError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User as AuthUser

from tourmate.models.user import User


class CreateUser(APIView):
    def post(self, request, format=None):
        try:
            user_alc = User(username = request.META.get('HTTP_USERNAME'), email = request.META.get('HTTP_EMAIL'))

            session = request.db_session
            session.add(user_alc)
            session.commit()
            
            user = AuthUser(
                username= user_alc.username,
                email= user_alc.email
            )

            user.set_password(request.META.get('HTTP_PASSWORD'))
            user.is_staff = True
            user.is_superuser = True
            user.save()

            return Response({}, status=status.HTTP_201_CREATED)
        except IntegrityError:
            session.rollback()
            return Response({'error': 'User with this email already exists.'}, status=status.HTTP_409_CONFLICT)