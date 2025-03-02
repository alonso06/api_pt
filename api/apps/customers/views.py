from rest_framework import (viewsets,
                            status) 
from rest_framework.decorators import action 
from rest_framework.response import Response 
from .models import (Customer as CustomerModel, 
                    CustomerType as CustomerTypeModel )
from .serializers import (CustomerTypeSerializer, CustomerSerializer)

class CustomerTypeLView(viewsets.ModelViewSet):
    queryset=CustomerTypeModel.objects.all()
    serializer_class=CustomerTypeSerializer
    
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
    
    @action(detail=True, methods=['patch'])
    def unsubscribe(self,
                    request,
                    pk=None):
        return unsubscribe_service(self,
                            request,
                            pk)
        

def unsubscribe_service(self,
                    request,
                    pk=None):
        obj = self.get_object() #type:ignore
        
        if not obj.state:
            return Response({'message': 'Ya dado de baja'},
                            status=status.HTTP_400_BAD_REQUEST)
        obj.state = False
        obj.save()
        
        return Response({'message': 'Dado de baja'},
                            status=status.HTTP_200_OK)