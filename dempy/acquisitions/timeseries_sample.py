from functools import partial
from typing import List, Dict, Any

from dempy._base import Entity
from dempy._protofiles import TimeseriesMessage


class TimeseriesSample(Entity):
    """TimeseriesSample class"""
    def __init__(self, type: str, id: str, tags: List[str], metadata: Dict[str, str], timestamp: int, acquisition_id: str, device_id: str,
                 sensor_id: str, **kwargs):
        super().__init__(type, id, tags, metadata)
        self.timestamp = timestamp
        self.acquisition_id = acquisition_id
        self.device_id = device_id
        self.sensor_id = sensor_id

        if self.type == "UniaxialSample":
            self.x: float = kwargs.get("x")
        elif self.type == "BiaxialSample":
            self.x: float = kwargs.get("x")
            self.y: float = kwargs.get("y")
        elif self.type == "TriaxialSample":
            self.x: float = kwargs.get("x")
            self.y: float = kwargs.get("y")
            self.z: float = kwargs.get("z")
        elif self.type == "QuadriaxialSample":
            self.x: float = kwargs.get("x")
            self.y: float = kwargs.get("y")
            self.z: float = kwargs.get("z")
            self.u: float = kwargs.get("u")
        elif self.type == "QuinqueaxialSample":
            self.x: float = kwargs.get("x")
            self.y: float = kwargs.get("y")
            self.z: float = kwargs.get("z")
            self.u: float = kwargs.get("u")
            self.w: float = kwargs.get("w")
        else:
            raise ValueError

    @staticmethod
    def to_protobuf(obj: "TimeseriesSample") -> TimeseriesMessage:
        """Encode a timeseries sample to a Protobuf message

        Arguments:
            obj {TimeseriesSample} -- timeseries sample to be encoded

        Returns:
            TimeseriesMessage -- encoded timeseries sample
        """
        timeseries_message = TimeseriesMessage()
        timeseries_message.entity.CopyFrom(Entity.to_protobuf(obj))

        timeseries_message.timestamp = obj.timestamp
        timeseries_message.acquisition_id = obj.acquisition_id

        if obj.device_id is not None:
            timeseries_message.device_id = obj.device_id
        if obj.sensor_id is not None:
            timeseries_message.sensor_id = obj.sensor_id

        if obj.type == "UniaxialSample":
            timeseries_message.x = obj.x
        elif obj.type == "BiaxialSample":
            timeseries_message.x = obj.x
            timeseries_message.y = obj.y
        elif obj.type == "TriaxialSample":
            timeseries_message.x = obj.x
            timeseries_message.y = obj.y
            timeseries_message.z = obj.z
        elif obj.type == "QuadriaxialSample":
            timeseries_message.x = obj.x
            timeseries_message.y = obj.y
            timeseries_message.z = obj.z
            timeseries_message.u = obj.u
        elif obj.type == "QuinqueaxialSample":
            timeseries_message.x = obj.x
            timeseries_message.y = obj.y
            timeseries_message.z = obj.z
            timeseries_message.u = obj.u
            timeseries_message.w = obj.w
        else:
            raise ValueError

        return timeseries_message

    @staticmethod
    def from_protobuf(timeseries_message: TimeseriesMessage) -> "TimeseriesSample":
        """Decode a Protobuf message to {TimeseriesSample}

        Arguments:
            obj {TimeseriesMessage} -- message to be decoded

        Returns:
            TimeseriesSample -- decoded timeseries sample
        """
        return TimeseriesSample(
            type=timeseries_message.entity.type,
            id=timeseries_message.entity.id,
            tags=timeseries_message.entity.tags,
            metadata=timeseries_message.entity.metadata,
            timestamp=timeseries_message.timestamp,
            acquisition_id=timeseries_message.acquisition_id,
            device_id=timeseries_message.device_id if timeseries_message.HasField("device_id") else None,
            sensor_id=timeseries_message.sensor_id if timeseries_message.HasField("sensor_id") else None,
            x=timeseries_message.x if timeseries_message.HasField("x") else None,
            y=timeseries_message.y if timeseries_message.HasField("y") else None,
            z=timeseries_message.z if timeseries_message.HasField("z") else None,
            u=timeseries_message.u if timeseries_message.HasField("u") else None,
            w=timeseries_message.w if timeseries_message.HasField("w") else None
        )

    @staticmethod
    def from_json(obj: Dict[str, str]) -> Any:
        """Parse a JSON dictionary to {TimeseriesSample}

        Arguments:
            obj {Dict[str, str]} -- JSON object

        Raises:
            ValueError: unexpected object or sub-object

        Returns:
            Any -- parsed object and sub-objects
        """
        if "type" in obj and obj["type"].endswith("axialSample"):
            timeseries = partial(
                TimeseriesSample,
                type=obj["type"],
                id=obj["id"],
                tags=obj["tags"],
                metadata=obj["metadata"],
                timestamp=obj["timestamp"],
                acquisition_id=obj["acquisitionId"],
                device_id=obj["deviceId"],
                sensor_id=obj["sensorId"],
            )

            if obj["type"] == "UniaxialSample":
                return timeseries(x=obj["x"])
            elif obj["type"] == "BiaxialSample":
                return timeseries(x=obj["x"], y=obj["y"])
            elif obj["type"] == "TriaxialSample":
                return timeseries(x=obj["x"], y=obj["y"], z=obj["z"])
            elif obj["type"] == "QuadriaxialSample":
                return timeseries(x=obj["x"], y=obj["y"], z=obj["z"], u=obj["u"])
            elif obj["type"] == "QuinqueaxialSample":
                return timeseries(x=obj["x"], y=obj["y"], z=obj["z"], u=obj["u"], w=obj["w"])
            else:
                raise ValueError

        return obj


__all__ = [
    "TimeseriesSample"
]
