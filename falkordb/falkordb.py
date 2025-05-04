from typing import (
    Callable,
    List,
    Mapping,
    Optional,
    TYPE_CHECKING,
    Union,
)

from redis.connection import ConnectionPool
from redis.retry import Retry

from .__version__ import __version__


if TYPE_CHECKING:
    import ssl
    import OpenSSL


class FalkorDB(object):
    """
    """

    def __init__(
        self,
        host: str = "localhost",
        port: Union[int, str] = 6379,
        *,
        password: Optional[str] = None,
        socket_timeout: Optional[float] = None,
        socket_connect_timeout: Optional[float] = None,
        socket_keepalive: Optional[bool] = None,
        socket_keepalive_options: Optional[Mapping[int, Union[int, bytes]]] = None,
        connection_pool: Optional[ConnectionPool] = None,
        unix_socket_path: Optional[str] = None,
        encoding: str = "utf-8",
        encoding_errors: str = "strict",
        decode_responses: bool = False,
        retry_on_timeout: bool = False,
        retry_on_error: Optional[List[Exception]] = None,
        ssl: bool = False,
        ssl_keyfile: Optional[str] = None,
        ssl_certfile: Optional[str] = None,
        ssl_cert_reqs: Union[str, "ssl.Verifymode"] = "required",
        ssl_ca_certs: Optional[str] = None,
        ssl_ca_path: Optional[str] = None,
        ssl_ca_data: Optional[str] = None,
        ssl_check_hostname: bool = True,
        ssl_password: Optional[str] = None,
        ssl_validate_ocsp: bool = False,
        ssl_validate_ocsp_stapled: bool = False,
        ssl_ocsp_context: Optional["OpenSSL.SSL.Context"] = None,
        ssl_ocsp_expected_cert: Optional[str] = None,
        ssl_min_version: Optional["ssl.TLSVersion"] = None,
        ssl_ciphers: Optional[str] = None,
        max_connections: Optional[int] = None,
        single_connection_client: bool = False,
        health_check_interval: int = 0,
        client_name: Optional[str] = None,
        lib_name: Optional[str] = "FalkorDB",
        lib_version: Optional[str] = __version__,
        username: Optional[str] = None,
        redis_connect_func: Optional[Callable] = None,
        credential_provider: Optional[CredentialProvider] = None,
        protocol: Optional[int] = 2,
        cache: Optional[CacheInterface] = None,
        cache_config: Optional[CacheConfig] = None,
        event_dispatcher: Optional[EventDispatcher] = None,

        cluster_error_retry_attempts: int = 3,
        startup_nodes: Optional[] = None,
        dynamic_startup_nodes: bool = True,
        require_full_coverage: bool = False,
        reinitialize_steps: int = 5,
        read_from_replicas: bool = False,
        url: Optional[str] = None,
        address_remap: Optional[] = None,
    ) -> None:
        """ """

        conn = redis.Redis(
            host=host,
            port=port,
            db=0,
            password=password,
            socket_timeout=socket_timeout,
            socket_connect_timeout=socket_connect_timeout,
            socket_keepalive=socket_keepalive,
            socket_keepalive_options=socket_keepalive_options,
            connection_pool=connection_pool,
            unix_socket_path=unix_socket_path,
            encoding=encoding,
            encoding_errors=encoding_errors,
            decode_responses=decode_responses,
            retry_on_timeout=retry_on_timeout,
            retry_on_error=retry_on_error,
            ssl=ssl,
            ssl_keyfile=ssl_keyfile,
            ...
        )
