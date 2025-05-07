from __future__ import annotations

from typing import (
    Any,
    Dict,
    List,
    Optional,
    Union,
)


class Node:
    """Representation of a node in a graph."""

    def __init__(
        self,
        alias: str = "n",
        node_id: Optional[int] = None,
        labels: Optional[Union[str, List[str]]] = None,
        properties: Optional[Dict[str, Any]] = None,
    ) -> None:

        if isinstance(labels, str):
            labels = [labels]

        self._alias = alias
        self._node_id = node_id
        self._labels = labels
        self._properties = properties or {}

    @property
    def alias(self) -> str:
        """Get the alias of the node."""
        return self._alias

    @property
    def id(self) -> Optional[int]:
        """Get the id of the node."""
        return self._node_id

    @property
    def node_id(self) -> Optional[int]:
        """Get the id of the node."""
        return self._node_id

    @property
    def labels(self) -> List[str]:
        """Get the node labels."""
        return self._labels

    @property
    def properties(self) -> Dict[str, Any]:
        """Get the node properties."""
        return self._properties

    def __eq__(self, other: Node) -> bool:
        """Check if two nodes are equal."""
        return all((
            self._node_id == other._node_id,
            self._labels == other._labels,
            self._properties == other._properties,
        ))
