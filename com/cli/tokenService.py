from com.cli.generated import sendToken_pb2
from com.cli.generated import sendToken_pb2_grpc


class VerifyTokenService(sendToken_pb2_grpc.VerifyTokenServiceServicer):
    def verifyToken(self, request, context):
        """
        Simple verification example - needed db validation token
        """
        if request.token == "my_test_token":
            return sendToken_pb2.VerifyTokenResponse(user="Yiro", success=True)
        return sendToken_pb2.VerifyTokenResponse(success=False)
