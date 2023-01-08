from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET','POST','PUT'])
def index(request):
    courses={
        'course_name':'python',
        'learn':['flask','django','toranado','fastAPI'],
        'course_prov':'scalar'
        }
    if request.method=='GET':
        print('you hit a GET method')
        return Response(courses)
    elif request.method=='POST':
        data=request.data
        print(data)
        print('you hit a Post method')
        return Response(courses)
    elif request.method=='PUT':
        print('you hit a PUT method')
        return Response(courses)

