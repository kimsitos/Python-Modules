from typing import List, Optional, Any, Dict, Union
from abc import ABC, abstractclassmethod


# Class
class DataStream(ABC):
    def __init__(self, ID: Optional[str]) -> None:
        self.ID = ID
        self.data_read = 0

    @abstractclassmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        return "Good"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        filtered = []
        if criteria is not None:
            for data in data_batch:
                if data == criteria:
                    filtered.append(data)
            return filtered
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {'ID': self.ID}


class SensorStream(DataStream):
    def __init__(self, ID: Optional[str] = 'SensorDefault') -> None:
        super().__init__(ID)
        self.type = 'Environmental Data'

    def process_batch(self, data_batch: List[Any]) -> str:
        if not isinstance(data_batch, List):
            return 'Error'

        temperature = 0
        num_temp = 0

        try:
            for data in data_batch:
                processed = data.split(':')
                if processed[0] == 'temp':
                    temperature += float(processed[1])
                    num_temp += 1
                self.data_read += 1
        except ValueError:
            return 'Error'

        try:
            self.avr_temp = temperature / num_temp
        except ZeroDivisionError:
            self.avr_temp = None

        return 'Good'

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        try:
            print(f"{self.data_read} reading processed, avg temp: "
                  f"{self.avr_temp if self.avr_temp is not None else'0'}"
                  f"ºC")
            return {
                'ID': self.ID,
                'type': self.type,
                'avr_temp': self.avr_temp,
                'data_read': self.data_read}
        except AttributeError:
            print("Error. Try to introduce correct vormat values: "
                  "<name>:<value>")
            return


class TransactionStream(DataStream):
    def __init__(self, ID: Optional[str] = 'TransactionDefault') -> None:
        super().__init__(ID)
        self.type = 'Financial Data'

    def process_batch(self, data_batch: List[Any]) -> None:
        if not isinstance(data_batch, List):
            return 'Error'

        self.net_flow = 0
        try:
            for data in data_batch:
                transaction = data.split(':')
                if transaction[0] == 'buy':
                    self.net_flow += int(transaction[1])
                elif transaction[0] == 'sell':
                    self.net_flow -= int(transaction[1])
                else:
                    return 'Error'
                self.data_read += 1
        except ValueError:
            return 'Error'

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        print(f"{self.data_read} operations, "
              f"net flow: {self.net_flow} units")
        return {
                'ID': self.ID,
                'type': self.type,
                'net_flow': self.net_flow,
                'data_read': self.data_read}


class EventStream(DataStream):
    def __init__(self, ID: Optional[str] = 'Event Default') -> None:
        super().__init__(ID)
        self.type = 'System Events'
        self.num_error = 0

    def process_batch(self, data_batch: List[Any]) -> None:
        super().process_batch(data_batch)
        for data in data_batch:
            if data == 'error':
                self.num_error += 1
            self.data_read += 1

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        print(f"{self.data_read} events, "
              f"{self.num_error} error detected")


class StreamProcessor():
    def process_batch(self, data: DataStream, events: Any) -> None:
        if isinstance(data, DataStream):
            data.process_batch(events)
            data.get_stats()


# Test
print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

print("\nInitializig Sensor Stream...")
sensor = SensorStream()
print(f"Stream ID: {sensor.ID}, Type: {sensor.type}")
sensor_data = ['temp:22.5', 'humidity:65', 'pressure:1013']
print(f"Processing sensor batch: {sensor_data}")
sensor_data = sensor.filter_data(sensor_data)
sensor.process_batch(sensor_data)
print("Sensor analysis:", end=' ')
sensor.get_stats()

print("\nInitializing Transaction Stream...")
transaction = TransactionStream("TRANS_001")
print(f"Stream ID: {transaction.ID}, Type: {transaction.type}")
transaction_data = ['buy:100', 'sell:150', 'buy:75', 'sell:430']
print("Processing transaction batch:", transaction_data)
transaction_data = transaction.filter_data(transaction_data)
transaction.process_batch(transaction_data)
print("Transaction analysis:", end=' ')
transaction.get_stats()

print("\nInitializing Event Stream...")
event = EventStream('Event_001')
print(f"Stream ID: {event.ID}, Type: {event.type}")
event_data = ['login', 'error', 'logout']
print("Processing event batch:", event_data)
event_data = event.filter_data(['login', 'error', 'logout'])
event.process_batch(event_data)
print('Event Analysis:', end=' ')
event.get_stats()


# Polymorphic Test
print("=== Polymorphic Stream Processing ===")

print("\nProcessing mixed stream types through unified interface...")

i = 0
long_data = 0
data = [['temp: 22.5', 'humidity: 65', 'pressure: 1013', 'hours: 10'],
        ['buy: 100', 'sell: 150', 'buy: 75', 'buy: 40'],
        ['login', 'error', 'logout']]

data_class = (SensorStream("SENSOR_002"), TransactionStream("TRANS_002"),
              EventStream("Event_002"))

polymorphic_processor = StreamProcessor()
for d in data_class:
    print('-', end=' ')
    polymorphic_processor.process_batch(d, data[i])
    i += 1
    long_data += 1 if d.data_read > 3 else 0

print("\nThe number of data processed that is more than 3 is", long_data)
print("\nAll streams processed successfully. Nexus throughput optimal.")
