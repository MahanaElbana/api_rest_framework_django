## ---------------   imports --------------------###
from django.http.response import JsonResponse
from rest_framework import pagination, serializers # ! method 1 and 2
from .models import Person  # ! method 2
from .serializers import PersonSerializer  # !method[3-1]
from rest_framework.decorators import action, api_view, parser_classes  # !method[3-1]
from rest_framework.response import Response  # !method[3-1]
from rest_framework import status  # !method[3]
from rest_framework.views import APIView  # !method[4]
from rest_framework import mixins , generics ,  viewsets# !method[5]
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action # !the last
###---------------- views ----------------------###

##* ---------- how to make pagination ----------##
from rest_framework.pagination import PageNumberPagination
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size =3
##* ---------- how to make pagination ----------##

#! ---- [1] the first method for api (get method) without rest_framework---
# *     http://127.0.0.1:8000/apioute/method1/
def get_static_data_no_rest_no_model(request):
    json_data = [
        {'name': 'Ali', 'email': 'Ali@yahoo.com', 'age': 21},
        {'name': 'Ahmed', 'email': 'Ahmed@yahoo.com', 'age': 22},
        {'name': 'gado', 'email': 'gado@yahoo.com', 'age': 23}
    ]

    return JsonResponse(json_data, safe=False)


#! ---- [2] the second method for getting data from model without rest_framework---
# *        http://127.0.0.1:8000/apioute/method2/
def get_data_no_rest_from_model(request):
    person = Person.objects.all()
    # print(list(Person.values())) to convert guest.values() to list
    json_data = {
        "bringing all Persons": list(person.values())
    }
    return JsonResponse(json_data, safe=False)


#! ----[3-1]the third method for 'GET' and 'POST' data  with rest_framework :-
''' 
      1- get data from model .
      2- passing data in serializer for converting to json 
      3- using FBV function base view from rest_frame_work
      4- GeustSerializer(instance=None, data=empty, **kwargs)
          1- any serializer take instance or data or **kwargs
'''
@api_view(['GET', 'POST'])
def fbv_list(request):
    # GET
    if request.method == 'GET':
        person = Person.objects.all()
        #PersonSerializer(instance=None, data=empty, **kwargs)
        serializer = PersonSerializer(instance=person, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST => for creating item
    elif request.method == 'POST':
        # passing data as json to serializer
        person = PersonSerializer(data=request.data)
        if person.is_valid():
            person.save()  # saving data in models
            return Response(person.data, status=status.HTTP_201_CREATED)
        return Response("error occurs no data stored !", status=status.HTTP_400_BAD_REQUEST)


#! ----[3-2]the third method for 'GET', 'PUT' and 'DELETE' data  with rest_framework :-
''' 
      in this method we need pk for access only item .
      in 'PUT' => required new data and old instance .   
'''
@api_view(['GET', 'PUT', 'DELETE'])
def fbv(request, pk):
    try:
        person = Person.objects.get(id=pk)
    except:
        return Response("this item is not exist !", status=status.HTTP_404_NOT_FOUND)

    # GET ==> for bringing data
    if request.method == 'GET':
        serializer = PersonSerializer(instance=person )
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST ==> for Updating item
    elif request.method == 'PUT':
        # passing data and instance
        personSerialize = PersonSerializer(instance=person , data=request.data)
        if  personSerialize.is_valid():
            personSerialize.save()  # override on instance with new data
            return Response( personSerialize.data, status=status.HTTP_202_ACCEPTED)
        return Response("error occurs . 'reservation' ,'name' ,'mobile' required in body",
                status=status.HTTP_400_BAD_REQUEST)

    # DELETE ==> for Deleting item
    elif request.method == 'DELETE':
        person.delete()
        return Response("item was deleted !",status=status.HTTP_204_NO_CONTENT)

#! ----[4-1]the fourth method for 'GET' and 'POST' data  with rest_framework :-
#*    http://127.0.0.1:8000/apioute/method4-1/
class CBV_LIST(APIView):

    #GET list
    def get(self ,request):
       person = Person.objects.all()
       serializers =PersonSerializer(instance= person ,many =True)
       return Response(serializers.data)
    
    #POST   
    def post(self ,request):
        person =  PersonSerializer(data= request.data)  
        if person.is_valid():
            person.save()
            return Response(person.data,status=status.HTTP_201_CREATED)
        return Response("error occurs BCV . 'reservation' ,'name' ,'mobile' required in body",
                status=status.HTTP_400_BAD_REQUEST)


#! ----[4-2]the fourth method for 'GET','PUT' and 'DELETE' data  with rest_framework :-
#*    http://127.0.0.1:8000/apioute/method4-2/2/
class CBV(APIView):

    # return item  
    def get_key_data(self , pk):
        try:
             return Person.objects.get(id=pk)
        except Person.DoesNotExist:
             return Response(status=status.HTTP_404_NOT_FOUND)  
      

    #GET list
    def get(self ,request, pk):
       person = self.get_key_data(pk)
       serializer =PersonSerializer(instance=person)
       return Response(serializer.data)
    
    #PUT  
    def put(self ,request ,pk):
        personModel =self.get_key(pk)
        person =  PersonSerializer(instance=personModel,data= request.data)  
        if person.is_valid():
            person.save()
            return Response(person.data,status=status.HTTP_201_CREATED)
        return Response("error occurs BCV . 'reservation' ,'name' ,'mobile' required in body",
                status=status.HTTP_400_BAD_REQUEST)

    # DELETE ==> for Deleting item
    def delete(self ,request ,pk):
        person = self.get_key_data(pk)
        person.delete()
        return Response("item was deleted !",status=status.HTTP_204_NO_CONTENT)


#! ----[5-1]the Fiveth method for 'GET' and 'POST' data  with rest_framework :-
class Mixin_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
  
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self ,request):
        return self.list(request)

    def post(self ,request):
        return self.create(request)   

#! ----[5-2]the Fiveth method for 'GET','PUT' and 'DELETE' data  with rest_framework:-
class Mixin_pk(mixins.UpdateModelMixin,
mixins.DestroyModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):
  
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get(self ,request ,pk):
        return self.retrieve(request)

    def put(self ,request,pk):
        return self.update(request) 

    def delete(self ,request,pk):
        return self.destroy(request)                

#! ----[6-1]the 6 method for 'GET','POST'  data  with rest_framework:-
class generics_list(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

#! ----[6-2]the 6 method for 'GET','PUT','DELETE'  data  with rest_framework:-
class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer    

#! ----[7]the the seventh method for 'GET','POST','PUT','DELETE',viewsets.ModelViewSet, rest_framework:-

class viewset_list_pk(viewsets.ModelViewSet,StandardResultsSetPagination):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer  
    pagination_class =StandardResultsSetPagination

#! [8]the the eighth method for 'GET','PUT', 'DELETE' data viewsets.ViewSet,rest_framework:-
class GeustViewSet(viewsets.ViewSet):
   
    def list(self, request):
        person = Person.objects.all()
        serializer = PersonSerializer(instance= person  ,many =True)
        return Response(serializer.data)

    def create(self, request):
        personSerializer = PersonSerializer(data= request.data )
        if personSerializer.is_valid():
            personSerializer.save()
            return Response(personSerializer.data ,status=status.HTTP_201_CREATED)
        return Response("the data is not correct" , status=status.HTTP_400_BAD_REQUEST) 

    def retrieve(self, request, pk=None):
         persons = Person.objects.all()
         person = get_object_or_404(persons ,id=pk)
         serialize = PersonSerializer(instance=person)
         return Response(serialize.data ,status=status.HTTP_201_CREATED) 

    def update(self, request, pk=None):
        persons = Person.objects.all()
        person = get_object_or_404(persons ,id=pk)
        serialize = PersonSerializer(instance=person ,data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data ,status=status.HTTP_201_CREATED) 
        return Response("an error ocurs " ,status=status.HTTP_201_CREATED)

    ## def partial_update(self, request, pk=None):
    ##     geusts = Geust.objects.all()
    ##     geust = get_object_or_404(geusts ,id=pk)
    ##     serialized = GeustSerializer(geust, data=request.data, partial=True)
    ##     if serialized.is_valid():
    ##         serialized.save()
    ##         return Response( status=status.HTTP_206_PARTIAL_CONTENT)
    ##     return Response("an error ocurs " ,status=status.HTTP_201_CREATED)    

    def destroy(self, request, pk=None):
        persons = Person.objects.all()
        person = get_object_or_404(persons ,id=pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        


#! [9]the the eighth method for 'GET','PUT', 'DELETE' rest_framework:-
class TheLastViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
     
    #! ovverride  
    def update(self, request, *args, **kwargs):
        return Response({'overrid on update method':'stop you that use update'})
    
    #! ovverride 
    def create(self,request):
        return Response({'overrid on create method':'stop you that use create'})
    
    #--Action in api view
    #* http://127.0.0.1:8000/apioute/method7-8/TheLast/4/action_method/
    @action(detail=True)
    def action_method(self, request, pk=None):  #pk is required
        return Response('this is action ')
    
#!  ///pip3 install httpie // /// /// 
   
##------ another method from my trial to create Guest ----##
class TrialCode(APIView):
   #post  
    def post(self ,request):
        person = Person()
        if 'name' in request.data and 'mobile' in request.data : 
           person.name = request.data['name'] 
           person.mobile = request.data['mobile']
           person.save()   
           serialize = PersonSerializer(instance= person)
           return Response(serialize.data ,status=status.HTTP_201_CREATED) 
        else :
            return Response("data of person are required " ,status=status.HTTP_405_METHOD_NOT_ALLOWED) 


            