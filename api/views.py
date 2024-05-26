from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from files.preprocessing import ReadingDocument
# Create your views here.

@api_view(["POST"])
def document_chat(request):
    file = request.FILES.get("file")
    print(file)
    text = ReadingDocument.pdf_reader(file)
    return Response({"output":text})