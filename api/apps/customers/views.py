from django.db.models import ProtectedError
from rest_framework import (viewsets,
                            status) 
from rest_framework.decorators import action 
from rest_framework.response import Response 
from .models import (Customer as CustomerModel, 
                    CustomerType as CustomerTypeModel )
from .serializers import (CustomerTypeSerializer, 
                          CustomerSerializer)

from api.exceptions import ProtectedDeletionException
from api.services import unsubscribe_service

class CustomerTypeLView(viewsets.ModelViewSet):
    queryset=CustomerTypeModel.objects.all()
    serializer_class=CustomerTypeSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        try:
            self.perform_destroy(instance)
        except ProtectedError:
            raise ProtectedDeletionException()

        return Response(status=status.HTTP_204_NO_CONTENT)
        
    @action(detail=True, methods=['patch'])
    def unsubscribe(self,
                    request,
                    pk=None):
        return unsubscribe_service(self,
                            request,
                            pk)
        

class CustomerView(viewsets.ModelViewSet):
    queryset=CustomerModel.objects.all()
    serializer_class=CustomerSerializer
    
    def get_queryset(self):
        name = self.request.query_params.get('name') #type: ignore
        if name:
            return self.queryset.filter(first_name__icontains=name)
        return self.queryset
    
    @action(detail=True, methods=['patch'])
    def unsubscribe(self,
                    request,
                    pk=None):
        return unsubscribe_service(self,
                            request,
                            pk)
        


        
        

