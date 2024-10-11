from abc import ABC, classmethod

class Model(ABC):

    @classmethod
    def from_json(json_payload):
        pass

    @classmethod
    def to_json(model):
        pass
