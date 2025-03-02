from rest_framework.exceptions import APIException

class ProtectedDeletionException(APIException):
    status_code = 400
    default_detail = "No se puede eliminar este registro porque está en uso."
    default_code = "protected_deletion"