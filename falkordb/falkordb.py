from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    List,
    Mapping,
    Optional,
    Tuple,
    Union,
)

import redis
from redis.backoff import ExponentialWithJitterBackoff
from redis.cache import (
    CacheConfig,
    CacheInterface,
)
from redis.cluster import ClusterNode
from redis.connection import ConnectionPool
from redis.credentials import CredentialProvider
from redis.events import EventDispatcher
from redis.retry import Retry

from .__version__ import __version__

if TYPE_CHECKING:
    import ssl

    import OpenSSL


class FalkorDB(object):
    """
    Object for interacting with a FalkorDB server.
    """

    @classmethod
    def from_url(cls, url: str, **kwargs: Dict[str, Any]) -> FalkorDB:
        """
        Create a new FalkorDB client from a URL.

        Parameters
        ----------
        url : str
            The URL string.
        kwargs : dict
            Additional keyword arguments to intialize the client with.

        Returns
        -------
        FalkorDB
            The initialized FalkorDB client.

        """

        url = url.replace("falkor://", "redis://") \
            .replace("falkors://", "rediss://")

        return cls(**kwargs)

    def __init__(
        self,
        host: str = 'localhost',
        port: Union[int, str] = 6379,
        *,
        password: Optional[str] = None,
        socket_timeout: Optional[float] = None,
        socket_connect_timeout: Optional[float] = None,
        socket_keepalive: Optional[bool] = None,
        socket_keepalive_options: Optional[Mapping[int, Union[int, bytes]]] = None,
        connection_pool: Optional[ConnectionPool] = None,
        unix_socket_path: Optional[str] = None,
        encoding: str = 'utf-8',
        encoding_errors: str = 'strict',
        decode_responses: bool = True,
        retry_on_timeout: bool = False,
        retry: Optional[Retry] = None,
        retry_on_error: Optional[List[Exception]] = None,
        ssl: bool = False,
        ssl_keyfile: Optional[str] = None,
        ssl_certfile: Optional[str] = None,
        ssl_cert_reqs: Union[str, ssl.Verifymode] = 'required',
        ssl_ca_certs: Optional[str] = None,
        ssl_ca_path: Optional[str] = None,
        ssl_ca_data: Optional[str] = None,
        ssl_check_hostname: bool = True,
        ssl_password: Optional[str] = None,
        ssl_validate_ocsp: bool = False,
        ssl_validate_ocsp_stapled: bool = False,
        ssl_ocsp_context: Optional[OpenSSL.SSL.Context] = None,
        ssl_ocsp_expected_cert: Optional[str] = None,
        ssl_min_version: Optional[ssl.TLSVersion] = None,
        ssl_ciphers: Optional[str] = None,
        max_connections: Optional[int] = None,
        single_connection_client: bool = False,
        health_check_interval: int = 0,
        client_name: Optional[str] = None,
        lib_name: Optional[str] = 'FalkorDB',
        lib_version: Optional[str] = __version__,
        username: Optional[str] = None,
        redis_connect_func: Optional[Callable] = None,
        credential_provider: Optional[CredentialProvider] = None,
        protocol: Optional[int] = 2,
        cache: Optional[CacheInterface] = None,
        cache_config: Optional[CacheConfig] = None,
        event_dispatcher: Optional[EventDispatcher] = None,
        cluster_error_retry_attempts: int = 3,
        startup_nodes: Optional[List[ClusterNode]] = None,
        dynamic_startup_nodes: bool = True,
        require_full_coverage: bool = False,
        reinitialize_steps: int = 5,
        read_from_replicas: bool = False,
        url: Optional[str] = None,
        address_remap: Optional[Callable[Tuple[str, int], Tuple[str, int]]] = None,
    ) -> None:

        if retry is None:
            retry = Retry(
                backoff=ExponentialWithJitterBackoff(base=1, cap=10),
                retries=3,
            )

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
            retry=retry,
            retry_on_error=retry_on_error,
            ssl=ssl,
            ssl_keyfile=ssl_keyfile,
            ssl_certfile=ssl_certfile,
            ssl_cert_reqs=ssl_cert_reqs,
            ssl_ca_certs=ssl_ca_certs,
            ssl_ca_path=ssl_ca_path,
            ssl_ca_data=ssl_ca_data,
            ssl_check_hostname=ssl_check_hostname,
            ssl_password=ssl_password,
            ssl_validate_ocsp=ssl_validate_ocsp,
            ssl_validate_ocsp_stapled=ssl_validate_ocsp_stapled,
            ssl_ocsp_context=ssl_ocsp_context,
            ssl_ocsp_expected_cert=ssl_ocsp_expected_cert,
            ssl_min_version=ssl_min_version,
            ssl_ciphers=ssl_ciphers,
            max_connections=max_connections,
            single_connection_client=single_connection_client,
            health_check_interval=health_check_interval,
            client_name=client_name,
            lib_name=lib_name,
            lib_version=lib_version,
            username=username,
            redis_connect_func=redis_connect_func,
            credential_provider=credential_provider,
            protocol=protocol,
            cache=cache,
            cache_config=cache_config,
            event_dispatcher=event_dispatcher,
        )

        # TODO: check if sentinel conn
        # TODO: check if cluster conn

        self._conn = conn
