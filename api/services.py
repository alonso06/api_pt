from rest_framework import status 
from rest_framework.response import Response 


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