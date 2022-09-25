from abc import abstractclassmethod, ABCMeta
import json
import pickle


class SerializationInterface(metaclass=ABCMeta):
    @abstractclassmethod
    def serialize(self):
        pass

    @abstractclassmethod
    def deserialize(self):
        pass


class JsonListSerialize(SerializationInterface):
    def serialize(self, data):
        return json.dumps(data)

    def deserialize(self, packed_data):
        return json.loads(packed_data)

class JsonDictSerialize(SerializationInterface):
    def serialize(self, data):
        return json.dumps(data)

    def deserialize(self, packed_data):
        return json.loads(packed_data)

class JsonSetSerialize(SerializationInterface):
    def serialize(self, data):
        return json.dumps(list(data))

    def deserialize(self, packed_data):
        return json.loads(packed_data)

class JsonTupleSerialize(SerializationInterface):
    def serialize(self, data):
        return json.dumps(list(data))

    def deserialize(self, packed_data):
        return tuple(json.loads(packed_data))

class BinListSerialize(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)

class BinListSerialize(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)

class BinDictSerialize(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)

class BinSetSerialize(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)

class BinTupleSerialize(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)
