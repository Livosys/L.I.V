_state = {}

def get_state(sid): return _state.get(sid, {})
def set_state(sid, s): _state[sid] = s
def push(sid, node):
    s = _state.setdefault(sid, {"stack":[]})
    s["stack"].append(node)
def pop(sid):
    s = _state.get(sid, {"stack":[]})
    return s["stack"].pop() if s["stack"] else None
