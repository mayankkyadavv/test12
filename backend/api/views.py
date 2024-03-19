from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
import fitz  # PyMuPDF

@api_view(['POST'])
def upload(request):
    # Ensure there is a file in the request
    print("being called!")
    if 'file' not in request.FILES:
        return JsonResponse({'error': 'No file provided.'}, status=400)

    # Get the uploaded file
    pdf_file = request.FILES['file']

    # Open the PDF file
    try:
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
        text = ""
        # Iterate through each page and extract text
        for page in doc:
            text += page.get_text()

        print(text)  # Print the extracted text

        return Response({'message': 'PDF processed successfully.'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
