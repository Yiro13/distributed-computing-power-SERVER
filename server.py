import grpc
from concurrent import futures

from com.cli.generated import sendToken_pb2_grpc
from com.cli.tokenService import VerifyTokenService

from com.cli.generated import status_pb2_grpc
from com.cli.statusService import StatusService

from com.cli.generated import sendCredentials_pb2_grpc
from com.cli.credentialsService import VerifyCredentialsService


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sendToken_pb2_grpc.add_VerifyTokenServiceServicer_to_server(
        VerifyTokenService(), server
    )
    status_pb2_grpc.add_StatusServicer_to_server(StatusService(), server)
    sendCredentials_pb2_grpc.add_VerifyCredentialsServiceServicer_to_server(
        VerifyCredentialsService(), server
    )

    server.add_insecure_port("[::]:50051")
    print("gRPC server listening on port 50051...")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
