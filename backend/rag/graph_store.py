import json
from pathlib import Path

GRAPH_PATH = Path("rag/graph.json")


def _load():
    if GRAPH_PATH.exists():
        return json.loads(GRAPH_PATH.read_text())
    return {"nodes": {}, "edges": []}


def _save(graph):
    GRAPH_PATH.write_text(json.dumps(graph, indent=2))


def add_node(node_id: str, node_type: str, data: dict):
    graph = _load()
    graph["nodes"][node_id] = {
        "type": node_type,
        "data": data
    }
    _save(graph)


def add_edge(src: str, dst: str, relation: str):
    graph = _load()
    graph["edges"].append({
        "from": src,
        "to": dst,
        "relation": relation
    })
    _save(graph)


def get_related(node_ids: list[str]) -> list[dict]:
    graph = _load()
    related = set(node_ids)

    for edge in graph["edges"]:
        if edge["from"] in related:
            related.add(edge["to"])
        if edge["to"] in related:
            related.add(edge["from"])

    return [
        graph["nodes"][nid]
        for nid in related
        if nid in graph["nodes"]
    ]
