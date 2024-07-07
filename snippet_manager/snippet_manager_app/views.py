from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.reverse import reverse

from .models import Tag, Snippet
from .serializers import TagSerializer, SnippetSerializer,UserSerializer,DetailAPISerializer

# Create your views here.


class RegisterView(APIView):
    permission_classes = []

    def post(self,request):
        serial = UserSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data,status=status.HTTP_201_CREATED)
        

class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

class TagCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OverviewAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        data = serializer.data
        for item in data:
            item['detail'] = reverse('snippet_detail_view', args=[item['id']], request=request)
        response_data = {
            'total_count': len(snippets),
            'snippets': data
        }
        return Response(response_data)
    
    
class CreateAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class DetailAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        try:
            snippets = Snippet.objects.get(id = pk)
            print(snippets)
            serializer = DetailAPISerializer(snippets)
            return Response(serializer.data)
        except Snippet.DoesNotExist:
            return Response({"error":"Page not found."})
        
        
class UpdateAPI(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            snippet = Snippet.objects.get(id = pk)
            serializer = SnippetSerializer(snippet, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Snippet.DoesNotExist:
            return Response({"error":"Page not found."})
    

class DeleteAPI(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            snippet = Snippet.objects.get(id = pk)
            serializer =  DetailAPISerializer(snippet)
            snippet.delete()
            return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
        except Snippet.DoesNotExist:
            return Response({"error":"Page not found."})
        
        
class TagListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    
    
class TagDetailAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        snippets = Snippet.objects.filter(tags = pk)
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

class TagDetailAPI1(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        snippets = Snippet.objects.filter(tags = pk)
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
    
#newwww
#fjdkmfdklvdfm
#fhduifheurdigfe

#fjrdijgijrdg
#@fuhergfer
#vnnjhfbjh
#mmfkjjgj
#@fuuufrjuifj

#joifhiud
#nvhjfdghutfh

#nfjkdhgrheuigh
#bhjedrufhhergyue

#jdfishfiuhuifh
    
        



   
