from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import (get_object_or_404,
                              get_list_or_404)
from models import (Customer as CustomerModel, 
                    CustomerType as CustomerTypeModel )
from serializers import (CustomerTypeSerializer, CustomerSerializer)


class BaseView(generics.GenericAPIView):
    
    # TODO:implementar token de authe
    
    queryset = None
    serializer_class = None
    
    def get_by_id(self,
                  id:int):
        obj = get_object_or_404(self.queryset,id)
        serializer_obj = self.serializer_class(obj) #type: ignore
        return Response(serializer_obj.data)

    def get_all(self):
        obj = get_list_or_404(self.queryset)
        serializer_obj = self.serializer_class(obj) #type: ignore
        return Response(serializer_obj.data)
    
    def save(self, 
             request:dict):
        serializer_obj = self.serializer_class(request.data) # type: ignore
        if serializer_obj.is_valid(): # type: ignore
            serializer_obj.save() # type: ignore
            return Response(serializer_obj.data, status=201)
        
        return Response(serializer_obj.errors, status=400) 
         
    def update(self,
               id:int,
               request:dict):
        obj = get_object_or_404(self.queryset,id)
        update_serializer_obj = self.serializer_class(obj,
                                                      request) #type: ignore
        if update_serializer_obj.is_valid(): # type: ignore
            update_serializer_obj.save() # type: ignore
            return Response(update_serializer_obj.data, status=201)
        return Response(update_serializer_obj.errors, status=400) 
    def delete(self,
               id:int):
        obj = get_object_or_404(self.queryset,id)
        obj.delete()
        return Response({'message':'Usuario eliminado'},
                        status=204)
        

class CustomerTypeView(BaseView):
    queryset = CustomerModel.objects.all()
    serializer_class = CustomerTypeSerializer
