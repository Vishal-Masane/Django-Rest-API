from django.shortcuts import render
# from serializer import BooksLibrarySerializer
from .serializer import BooksLibrarySerializer
from .models import BooksLibrary
from django.http import HttpResponse
import json
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def get_single_book(request, id):
    book = BooksLibrary.objects.get(id = id)
    py_data = BooksLibrarySerializer(book)
    print(py_data.data)
    # json_data = json.dumps(py_data.data)
    json_data = JSONRenderer().render(py_data.data)
    # return HttpResponse("success")
    return HttpResponse(json_data, content_type = "application/json")

def get_all_books(request):
    all_books = BooksLibrary.objects.all()
    py_data = BooksLibrarySerializer(all_books, many = True)
    # print(py_data)
    json_data = JSONRenderer().render(py_data.data)
    print(json_data)
    return HttpResponse(json_data, content_type = "application/json")

@csrf_exempt
def create_book(request):
    if request.method == "POST":
        book_data = request.body
        my_json = book_data.decode('utf8').replace("'", '"')
        # print(my_json)
        py_data = json.loads(my_json)
        # print(py_data)      # {'Name': 'book3', 'Price': 40, 'Quantity': 15, 'Is_Publish': True, 'Author': 'a3'}
        ser = BooksLibrarySerializer(data = py_data)
        if ser.is_valid():
            new_book = ser.save()
            # my_json = JSONRenderer().render(new_book.data)
            new_book.__dict__.pop("_state")
            my_json = json.dumps(new_book.__dict__)
            return HttpResponse(my_json, content_type = "application/json")
        else:
            return HttpResponse("Kindly share all details")
    else:
        error_msg = {"msg": "Only POST method is allow"}
        my_json = json.dumps(error_msg)
        return HttpResponse(my_json, content_type = "application/json")

