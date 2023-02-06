from rest_framework import views, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404           # get_objects_or_404 불러오기
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def HelloAPI(request):
    return Response("hello world!") 

@api_view(['GET', 'POST'])                                      # GET/POST 요청을 처리하게 만들어주는 데코레이터
def booksAPI(request):                                          # /book/
    if request.method == 'GET':                                 # GET 요청 (도서 전체 정보)
        books = Book.objects.all()                              # book 모델로 부터 전체 데이터 가져오기         
        serializer = BookSerializer(books, many=True)           # 시리얼라이저에 전체 데이터를 한번에 집언허기(직렬화, . many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) # return Response!

    elif request.method =='POST':                               # POST 요청 (도서 정보 등록)
        serializer = BookSerializer(data=request.data)          # POST 요청으로 들어온 데이터를 시리얼라이즈에 집어넣기

        if serializer.is_valid():                               # 유효한 데이터라면 집어 넣기
            serializer.save()                                   # 시리얼라이저의 역직렬화를 통해 save(), 모델 시리얼라이저의 기본 create()함수가 동작
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 201 메세지를 보내며 성공!

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST) # 400 잘못된 요청

@api_view(['GET'])
def bookAPI(request, bid):                                      #/book/bid/
    book = get_object_or_404(Book, bid=bid)                     # bid= id인 데이터를 Book에서 가져오고, 없으면 404 에러
    serializer = BookSerializer(book)                           # 시리얼라이저에 데이터를 집어넣기(직렬화)
    return Response(serializer.data, status=status.HTTP_200_OK) # return Response!

class BooksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class BookAPI(APIView):
    def get(self, request, bid):
        book = get_object_or_404(Book, bid=bid)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)