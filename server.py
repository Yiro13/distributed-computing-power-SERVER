import grpc
from concurrent import futures
import sendToken_pb2
import sendToken_pb2_grpc


class VerifyTokenService(sendToken_pb2_grpc.VerifyTokenServiceServicer):
    def verifyToken(self, request, context):
        # Simple verification example
        if request.token == "my_test_token":
            return sendToken_pb2.VerifyTokenResponse(user="User123", success=True)
        return sendToken_pb2.VerifyTokenResponse(success=False)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sendToken_pb2_grpc.add_VerifyTokenServiceServicer_to_server(
        VerifyTokenService(), server
    )
    server.add_insecure_port("[::]:50051")
    print("gRPC server listening on port 50051...")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
