from app.domain.node.repository import NodeRepository


class NodeService:
    def __init__(self, node_repo: NodeRepository):
        self._node_repo = node_repo

    async def get_active_nodes(self) -> list[str]:
        all_nodes: set[str] = set(await self._node_repo.get_all_nodes())
        active_nodes: set[str] = {node for node in all_nodes if await self._node_repo.is_active(node)}

        should_delete_nodes = all_nodes - active_nodes
        for node in should_delete_nodes:
            await self._node_repo.delete_node(node)

        return list(active_nodes)
