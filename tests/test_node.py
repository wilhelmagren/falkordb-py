from falkordb import Node


def test_eq():
    n1 = Node(alias="a")
    n2 = Node(alias="b", node_id=4, labels="l")
    n3 = Node(alias="c", node_id=1, labels=["j", "k"])
    n4 = Node(alias="d", node_id=2, properties={"friends": 4})
    n5 = Node(alias="e", node_id=4, labels="l")

    assert n1 != n2
    assert n2 != n3
    assert n3 != n4
    assert n2 == n5

