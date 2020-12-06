from __future__ import annotations
from typing import Dict


class Entity:
    def __init__(self):
        pass

    def serialize(entity: Entity) -> Dict:
        pass

    def deserialize(serialized_entity: Dict) -> Entity:
        pass
