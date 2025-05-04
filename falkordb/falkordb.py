from typing import (
    Mapping,
    Optional,
    Union,
)

from redis.backoff import ExponentialWithJitterBackoff
from redis.connection import ConnectionPool
from redis.retry import Retry


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
        retry: Retry = Retry(
            backoff=ExponentialWithJitterBackoff(base=1, cap=10), retries=3,
        ),
    ) -> None:
        """ """
        pass
