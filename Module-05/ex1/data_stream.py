from typing import Any


class DataStream:
    def process_batch(self) -> None:
        self.hello = "world" 


class SensorStream(DataStream):
    def process_batch(self, sensor: Any) -> None:
        super().process_batch()
        self.sensor = sensor


class TransactionStream(DataStream):
    def process_batch(self, transaction: Any) -> None:
        print(transaction)


class EventStream(DataStream):
    def process_batch(self, event: Any) -> None:
        print(event)


class StreamProcessor():
    def process_batch(self, data: DataStream) -> None:
        super().process_batch()


streams = [
    SensorStream(1),
    TransactionStream(2),
    EventStream(3)
]

processor = StreamProcessor()

for s in streams:
    processor.process_batch(s)
