from app.domain.task.service import TaskService


def test_chunked_subscribers_is_equal_node_length():
    # given
    subscribers = [i for i in range(8)]
    nodes_len = 6
    # when
    chunked_subscribers = TaskService._chunk_subscribers(subscribers, nodes_len)
    # then
    assert len(chunked_subscribers) == nodes_len
