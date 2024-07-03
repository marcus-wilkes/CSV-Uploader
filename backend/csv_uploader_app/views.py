from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CsvData
from .utils import validate_file, process_csv_data


@api_view(['POST'])
def upload_csv(request):
    uploaded_file = request.FILES.get('file', None)
    error_message, status = validate_file(uploaded_file)
    if error_message:
        return Response({'error': error_message}, status=status)

    try:
        objects_to_create = process_csv_data(uploaded_file)
        CsvData.objects.bulk_create(objects_to_create)
        return Response({'message': 'CSV file uploaded and processed successfully'})
    except Exception as e:
        return Response({'error': str(e)}, status=500)
