from rest_framework.response import Response

operation_failure = Response(status=400, data={"message": "OPERATION_FAILURE"})
operation_success = Response(status=200, data={"message": "OPERATION_SUCCESS"})

# 인증
certification_failure = Response(status=401, data={'message': 'CERTIFICATION_FAILURE'})
