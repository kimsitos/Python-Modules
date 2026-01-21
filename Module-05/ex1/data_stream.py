from typing import Dict, Any


# Class
class DataStream:
    def __init__(self, ID: str) -> Any:
        self.streamID = ID

    def process_events(self, events: Dict) -> int:
        self.num_events = 0
        for _ in events:
            self.num_events += 1
        return self.num_events


class SensorStream(DataStream):
    def __init__(self, ID: str) -> None:
        super().__init__(ID)
        self.type = "Environmental Data"

    def process_events(self, events: Dict) -> int:
        super().process_events()


class TransactionStream(DataStream):
    def __init__(self, ID: str) -> None:
        super().__init__(ID)
        self.type = "Financial Data"

    def process_events(self, events: Dict) -> int:
        return self.hello


class EventStream(DataStream):
    def __init__(self, ID: str) -> None:
        super().__init__(ID)
        self.type = "System Events"

    def process_events(self, events: Dict) -> int:
        return self.hello


class StreamProcessor():
    def process_batch(self, data: DataStream) -> None:
        if isinstance(data, DataStream):
            print(data.process_events())
        else:
            print("lol nothig")
        return


# Test
streams = [
    SensorStream("1").process_events({"error": 2, "maybe": 1234}),
    TransactionStream("2").process_events({"error": 2, "maybe": 1234}),
    EventStream("3").process_events({"error": 2, "maybe": 1234})
]

processor = StreamProcessor()

for s in streams:
    processor.process_batch(s)
