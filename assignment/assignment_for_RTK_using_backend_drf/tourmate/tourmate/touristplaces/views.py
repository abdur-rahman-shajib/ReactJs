from sqlalchemy.orm import noload
from sqlalchemy import desc, func
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions

from tourmate.models.tourist_place import TouristPlace
from tourmate.models.user import User
from tourmate.models.enosis_project import EnosisProject
from tourmate.models.techstack import TechStack

from tourmate.serializers.tourist_place import TouristPlaceSerializer
from tourmate.serializers.user import UserSerializer
from tourmate.serializers.enosis_project import EnosisProjectSerializer
from tourmate.serializers.techstack import TechStackSerializer

from touristplaces.permissions import IsOwnerOrReadOnly


class UserList(APIView):
    def get(self, request, format=None):
        session = request.db_session
        users = session.query(User).options(noload(User.touristplaces)).all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserDetail(APIView):
    def get(self, request, pk, format=None):
        session = request.db_session
        users = session.query(User).filter(User.id == pk).all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class TouristPlaceList(APIView):
    def get(self, request, format=None):
        session = request.db_session

        sortorder = self.request.query_params.get('sortorder', None)
        if sortorder and sortorder.lower() == 'asc':
            tourist_places = session.query(TouristPlace).order_by(TouristPlace.rating).all()
        elif sortorder and sortorder.lower() == 'desc':
            tourist_places = session.query(TouristPlace).order_by(desc(TouristPlace.rating)).all()
        else:
            tourist_places = session.query(TouristPlace).all()

        serializer = TouristPlaceSerializer(tourist_places, many=True)
        return Response(serializer.data)
    

    def post(self, request, format=None):
        try:
            print('fs')
            print(request.data)
            serializer = TouristPlaceSerializer(data=request.data)
            print('fdf2')
            if serializer.is_valid():
                session = request.db_session
                touristplace = serializer.save()
                currentUser = session.query(User).filter(User.username == request.user.username).first()
                touristplace.creator = currentUser
                session.add(touristplace)
                session.commit()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print('fdfd')
                print(serializer.errors)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TechStackList(APIView):
    def get(self, request, format=None):
        try:
            session = request.db_session
            projects = session.query(TechStack).all()
            serializer = TechStackSerializer(projects, many=True)
            #if serializer.is_valid():
            return Response(serializer.data)
            #    print(serializer.errors)
        except Exception as e:
            print(e)    
        return Response([])
    

    def post(self, request, format=None):
        try:
            serializer = TechStackSerializer(data=request.data)
            if serializer.is_valid():            
                session = request.db_session
                project = serializer.save()
                print('fdfd4')

                session.add(project)
                session.commit()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectList(APIView):
    def get(self, request, format=None):
        try:
            session = request.db_session
            projects = session.query(EnosisProject).all()
            print(len(projects))
            print(projects)
            serializer = EnosisProjectSerializer(projects, many=True)
            print(serializer)
            #if serializer.is_valid():
            return Response(serializer.data)
            #    print(serializer.errors)
        except Exception as e:
            print(e)    
        return Response([])
    

    def post(self, request, format=None):
        try:
            print('fdvvv')
            serializer = EnosisProjectSerializer(data=request.data)
            print('fdfd')
            if serializer.is_valid():            
                print('fdfd3')

                session = request.db_session
                project = serializer.save()
                print('fdfd4')

                session.add(project)
                session.commit()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    # def get(self, request, format=None):
    #     data = [
        # {
        #     'name': "Name",
        #     'mode': "mode",
        #     'se_count': 1,
        #     'sse_count': 1,
        #     'total_resources': 3,
        #     'non_lead_resources': 2,
        #     'planned': True,
        #     'manager': "mr sfgds",
        #     'lead': "lead",
        #     'dev_lead': "Messi",
        #     'tech_lead': "John Smith",
        #     'buffer': 2,
        #     'archived': True
        # },
    #     {
    #         'name': "Name2",
    #         'mode': "mode",
    #         'se_count': 1,
    #         'sse_count': 1,
    #         'total_resources': 3,
    #         'non_lead_resources': 2,
    #         'planned': True,
    #         'manager': "mr sfgds",
    #         'lead': "lead",
    #         'dev_lead': "Neymar",
    #         'tech_lead': "John F Kenedy",
    #         'buffer': 4,
    #         'archived': False
    #     },
    #     {
    #         'name': "Name5",
    #         'mode': "mode",
    #         'se_count': 1,
    #         'sse_count': 1,
    #         'total_resources': 3,
    #         'non_lead_resources': 2,
    #         'planned': True,
    #         'manager': "mr sfgds",
    #         'lead': "lead",
    #         'dev_lead': "Neymar",
    #         'tech_lead': "John F Kenedy",
    #         'buffer': 4,
    #         'archived': False
    #     },
    #     {
    #         'name': "Name3",
    #         'mode': "mode",
    #         'se_count': 1,
    #         'sse_count': 1,
    #         'total_resources': 3,
    #         'non_lead_resources': 2,
    #         'planned': True,
    #         'manager': "mr sfgds",
    #         'lead': "lead",
    #         'dev_lead': "Harry Poter",
    #         'tech_lead': "John Smith1",
    #         'buffer': 1,
    #         'archived': True
    #     },
    #     {
    #         'name': "Name4",
    #         'mode': "mode2",
    #         'se_count': 2,
    #         'sse_count': 4,
    #         'total_resources': 5,
    #         'non_lead_resources': 7,
    #         'planned': True,
    #         'manager': "mr sfgds1",
    #         'lead': "lead2",
    #         'dev_lead': "Klassen",
    #         'tech_lead': "John Doe",
    #         'buffer': 3,
    #         'archived': False
    #     },
    #     ]
    #     return Response(data)
    

    # def post(self, request, format=None):
    #     try:
    #         modified_data = request.data.copy()
    #         modified_data['archived'] = modified_data['status'] == 'Archived'
            
    #         modified_data['se_count'] = 1
    #         modified_data['sse_count'] = 2
    #         modified_data['total_resources'] = 5
    #         modified_data['non_lead_resources'] = 4
    #         modified_data['planned'] = True
    #         modified_data['manager'] = 'manager1'
    #         modified_data['lead'] = 'lead1'
    #         modified_data['dev_lead'] = 'fds sd dfsfs'
    #         modified_data['tech_lead'] = 'dsadasff dsf'
    #         modified_data['buffer'] = 3

    #         return Response(modified_data, status=status.HTTP_201_CREATED)
    #     except Exception as e:
    #         return Response({}, status=status.HTTP_400_BAD_REQUEST)
        

class TouristPlaceDetail(APIView):
    def get(self, request, pk, format=None):
        session = request.db_session
        tourist_place_id = pk
        tourist_place = session.query(TouristPlace).filter(TouristPlace.id == tourist_place_id).first()
        tourist_place_serializer = TouristPlaceSerializer(tourist_place)
        return Response(tourist_place_serializer.data)

    
    def put(self, request, pk, format=None):
        try:
            session = request.db_session
            tourist_place = session.query(TouristPlace).filter(TouristPlace.id == pk).first()
            self.check_object_permissions(request, tourist_place)
            tourist_place.updated_at = func.now()

            serializer = TouristPlaceSerializer(tourist_place, data=request.data)
            updated_place = serializer.update(tourist_place, request.data)
            
            session.commit()
            return Response(TouristPlaceSerializer(updated_place).data)
        except PermissionDenied as ex:
            session.rollback()
            raise ex

    def delete(self, request, pk, format=None):
        try:
            session = request.db_session
            tourist_place = session.query(TouristPlace).filter(TouristPlace.id == pk).first()
            self.check_object_permissions(request, tourist_place)
            session.query(TouristPlace).filter(TouristPlace.id == pk).delete()
            session.commit()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except PermissionDenied as ex:
            session.rollback()
            raise ex