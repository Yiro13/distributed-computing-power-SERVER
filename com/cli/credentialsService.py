from com.cli.generated import sendCredentials_pb2
from com.cli.generated import sendCredentials_pb2_grpc


class VerifyCredentialsService(
    sendCredentials_pb2_grpc.VerifyCredentialsServiceServicer
):
    def verifyCredentials(self, request, context):
        if request.email == "yiro@neurogrid.ai" and request.password == "1234":
            return sendCredentials_pb2.VerifyCredentialsResponse(
                token="my_token", success=True
            )
        return sendCredentials_pb2.VerifyCredentialsResponse(success=False)
