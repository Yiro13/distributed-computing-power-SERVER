from google.protobuf import empty_pb2

from com.cli.generated import status_pb2_grpc


class StatusService(status_pb2_grpc.Status):
    def status(self, request, context):
        print(request.user)
        return empty_pb2.Empty()
