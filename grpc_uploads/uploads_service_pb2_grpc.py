# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import uploads_service_pb2 as uploads__service__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in uploads_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class UploadsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ClaimFile = channel.unary_unary(
                '/uploads.Uploads/ClaimFile',
                request_serializer=uploads__service__pb2.ClaimFileReq.SerializeToString,
                response_deserializer=uploads__service__pb2.ClaimFileResp.FromString,
                _registered_method=True)
        self.DeleteFile = channel.unary_unary(
                '/uploads.Uploads/DeleteFile',
                request_serializer=uploads__service__pb2.DeleteFileReq.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.ClearFiles = channel.unary_unary(
                '/uploads.Uploads/ClearFiles',
                request_serializer=uploads__service__pb2.ClearFilesReq.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class UploadsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ClaimFile(self, request, context):
        """Claim a file
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteFile(self, request, context):
        """Delete a file
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearFiles(self, request, context):
        """Clear a user's files
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UploadsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ClaimFile': grpc.unary_unary_rpc_method_handler(
                    servicer.ClaimFile,
                    request_deserializer=uploads__service__pb2.ClaimFileReq.FromString,
                    response_serializer=uploads__service__pb2.ClaimFileResp.SerializeToString,
            ),
            'DeleteFile': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteFile,
                    request_deserializer=uploads__service__pb2.DeleteFileReq.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ClearFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearFiles,
                    request_deserializer=uploads__service__pb2.ClearFilesReq.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'uploads.Uploads', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Uploads(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ClaimFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/uploads.Uploads/ClaimFile',
            uploads__service__pb2.ClaimFileReq.SerializeToString,
            uploads__service__pb2.ClaimFileResp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/uploads.Uploads/DeleteFile',
            uploads__service__pb2.DeleteFileReq.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ClearFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/uploads.Uploads/ClearFiles',
            uploads__service__pb2.ClearFilesReq.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
