from typing import Dict, Any, List


# Class
class DataStream:
    def __init__(self, ID: str) -> Any:
        self.ID = ID

    def process_batch(self, data: Any) -> None:
        self.num_events = 0
        for _ in data:
            self.num_events += 1

    def analysis(self) -> None:
        print(f"Data analysis {self.num_events}")


class SensorStream(DataStream):
    def __init__(self, ID: str) -> None:
        super().__init__(ID)
        self.type = "Environmental Data"

    def process_batch(self, data: Dict) -> None:
        super().process_batch(data)
        try:
            self.temperature = data['temp']
        except KeyError:
            self.temperature = None

    def analysis(self) -> None:
        print(f"Sensor analysis: {self.num_events} readings _ed, "
              f"avr temp: {self.temperature}C")


class TransactionStream(DataStream):
    def __init__(self, ID: str) -> None:
        super().__init__(ID)
        self.type = "Financial Data"

    def process_batch(self, data: Dict) -> None:
        super().process_batch(data)
        self.net = 0
        for transaction, quantity in data:
            if transaction == 'buy':
                self.net += quantity
            elif transaction == 'sell':
                self.net -= quantity

    def analysis(self) -> None:
        print(f"Transaction analysis: {self.num_events} operations, "
              f"net flow: {self.net} units")


class EventStream(DataStream):
    def __init__(self, ID: str) -> None:
        super().__init__(ID)
        self.type = "System Events"

    def process_batch(self, data: List) -> None:
        super().process_batch(data)
        self.num_error = 0
        for e in data:
            if e == 'error':
                self.num_error += 1

    def analysis(self) -> None:
        print(f"Event analysis: {self.num_events} events, "
              f"{self.num_error} error detected")


class StreamProcessor():
    def process_batch(self, data: DataStream, events: Any) -> None:
        if isinstance(data, DataStream):
            data.process_batch(events)
            data.analysis()


# Test
print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

print("\nInitializig Sensor Stream...")
sensor = SensorStream("SENSOR_001")
print(f"Stream ID: {sensor.ID}, Type: {sensor.type}")
print("Processing sensor batch:",
      "{'temp': 22.5, 'humidity': 65, 'pressure': 1013}")
sensor.process_batch({'temp': 22.5, 'humidity': 65, 'pressure': 1013})
sensor.analysis()

print("\nInitializing Transaction Stream...")
transaction = TransactionStream("TRANS_001")
print(f"Stream ID: {transaction.ID}, Type: {transaction.type}")
print("Processing transaction batch: "
      "[('buy', 100), ('sell', 150), ('buy', 75)]")
transaction.process_batch([('buy', 100), ('sell', 150), ('buy', 75)])
transaction.analysis()

print("\nInitializing Event Stream...")
event = EventStream('Event_001')
print(f"Stream ID: {event.ID}, Type: {event.type}")
print("Processing event batch: [login, error, logout]")
event.process_batch(['login', 'error', 'logout'])
event.analysis()

# Polymorphic Test
print("=== Polymorphic Stream Processing ===")

print("\nProcessing mixed stream types through unified interface...")

i = 0
long_data = 0
data = [{'temp': 22.5, 'humidity': 65, 'pressure': 1013, 'hours': 10},
        [('buy', 100), ('sell', 150), ('buy', 75), ('buy', 400)],
        ['login', 'error', 'logout']]

data_class = (SensorStream("SENSOR_002"), TransactionStream("TRANS_002"), 
              EventStream("Event_002"))

polymorphic_processor = StreamProcessor()
for d in data_class:
    print('-', end=' ')
    polymorphic_processor.process_batch(d, data[i])
    i += 1
    long_data += 1 if d.num_events > 3 else 0

print("\nThe number of data processed that is more than 3 is", long_data)
print("\nAll streams processed successfully. Nexus throughput optimal.")
