from .details import (
    _create_subject, _delete_subject, 
    _get_device, _create_device, _delete_device, _get_device_usage,
    _get_image_samples, _get_image_samples_count,
    _get_video_samples, _get_video_samples_count,
    _get_timeseries_samples, _get_timeseries_samples_count, 
    _get_annotations, _get_annotations_count
)

class Acquisition:
    def __init__(self, type="Acquisition", id="", creationTimestamp=0, syncOffset=None, timeUnit="", ownerId="",
                 creatorId="", datasetId="", subject=object(), devices=[], metadata={}, tags=[],
                 hasTimeSeriesSamples=False, hasImageSamples=False, hasVideoSamples=False):
        self.id = id
        self.creationTimestamp = creationTimestamp
        self.syncOffset = syncOffset
        self.timeUnit = timeUnit
        self.ownerId = ownerId
        self.creatorId = creatorId
        self.datasetId = datasetId
        self._subjectData = subject
        self._devicesData = devices
        self.metadata = metadata
        self.tags = tags
        self.hasTimeSeriesSamples = hasTimeSeriesSamples
        self.hasImageSamples = hasImageSamples
        self.hasVideoSamples = hasVideoSamples
        self._timeSeriesSamplesData = []

    @property
    def subject(self):
        class inner:
            @staticmethod
            def get():
                return self._subjectData

            @staticmethod
            def create(subject):
                self._subjectData = _create_subject(self.id, subject)
                return self._subjectData

            @staticmethod
            def delete():
                _delete_subject(self.id, self._subjectData.id)
                self._subjectData = None

        return inner()

    @property
    def devices(self):
        class inner:
            @staticmethod
            def get(deviceId=None):
                if deviceId is None:
                    return self._devicesData
                else:
                    return _get_device(self.id, deviceId)  # TODO: verificar isto

            @staticmethod
            def create(device):
                device_created = _create_device(self.id, device)
                self._devicesData.append(device_created)
                return device_created

            # TODO:
            """@staticmethod
            def modify(deviceId, new_device):
                return _modify_device(self.id, deviceId, new_device)
                pass"""

            @staticmethod
            def delete(deviceId):
                # self._devicesData = [device for device in self._devicesData if device.id != deviceId]
                for index in range(len(self._devicesData)):
                    if self._devicesData[index].id == deviceId:
                        del self._devicesData[index]
                _delete_device(self.id, deviceId)

            @staticmethod
            def usage():
                return _get_device_usage(self.id)

            @staticmethod
            def count():
                return len(self._devicesData)

        return inner()

    @property
    def imageSamples(self):
        class inner:
            @staticmethod
            def get():
                return _get_image_samples(self.id)

            @staticmethod
            def count():
                return _get_image_samples_count(self.id)

        return inner()

    @property
    def videoSamples(self):
        class inner:
            @staticmethod
            def get():
                return _get_video_samples(self.id)

            @staticmethod
            def count():
                return _get_video_samples_count(self.id)
        return inner()

    @property
    def timeSeriesSamples(self):
        class inner:
            @staticmethod
            def get():
                return _get_timeseries_samples(self.id) \

            @staticmethod
            def count():
                return _get_timeseries_samples_count(self.id)

        return inner()

    @property
    def annotations(self):
        class inner:
            @staticmethod
            def get():
                return _get_annotations(self.id)

            @staticmethod
            def count():
                return _get_annotations_count(self.id)

        return inner()

    def keys(self):
        return self.__dict__.keys()

    def __getitem__(self, key):
        return getattr(self, key)

    def __repr__(self):
        return f"<Acquisition id=\"{self.id}\">"
