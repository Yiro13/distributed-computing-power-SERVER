import grpc
from concurrent import futures

from generated import sendToken_pb2
from generated import sendToken_pb2_grpc

# from generated import status_pb2
from generated import status_pb2_grpc


class VerifyTokenService(sendToken_pb2_grpc.VerifyTokenServiceServicer):
    def verifyToken(self, request, context):
        """
        Simple verification example - needed db validation token
        """
        if request.token == "my_test_token":
            return sendToken_pb2.VerifyTokenResponse(user="Yiro", success=True)
        return sendToken_pb2.VerifyTokenResponse(success=False)


class StatusService(status_pb2_grpc.Status):
    def verifyStatus(self, request, context):
        print(request.user)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sendToken_pb2_grpc.add_VerifyTokenServiceServicer_to_server(
        VerifyTokenService(), server
    )
    status_pb2_grpc.add_StatusServicer_to_server(StatusService(), server)

    server.add_insecure_port("[::]:50051")
    print("gRPC server listening on port 50051...")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
