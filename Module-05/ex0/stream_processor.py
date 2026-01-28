from typing import Any
from abc import ABC, abstractclassmethod


# Class
class DataProcessor(ABC):
    @abstractclassmethod
    def process(self, data: Any) -> str:
        return str(data)

    @abstractclassmethod
    def validate(self, data: Any) -> bool:
        return False if data == 'Error' else True

    def format_output(self, result: str) -> str:
        print("output", result)


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        self.processed_numbers = 0
        self.sum = 0
        self.avr = 0
        if not data:
            return 'Error'
        try:
            for num in data:
                self.sum += num
                self.processed_numbers += 1
            self.avr = self.sum / self.processed_numbers
        except TypeError:
            return "Error"
        return "Good"

    def validate(self, data: any) -> bool:
        super().validate(data)

    def format_output(self, result: str) -> str:
        if result == 'Good':
            return (f"Processed {self.processed_numbers} "
                    f"numeric values, sum={self.sum}, avr={self.avr}")
        return "Error validating data, please a valid data"


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        self.words = 1
        self.chars = 0
        if not data:
            return 'Error'

        for c in data:
            if not (c >= ' ' and c <= '}'):
                return 'Error'
            if c == ' ':
                self.words += 1
            self.chars += 1
        return 'Good'

    def validate(self, data: any) -> bool:
        super().validate(data)

    def format_output(self, result: str) -> str:
        if result == 'Good':
            return f"Processed text: {self.chars}, {self.words} words"
        return "Error validating data, please a valid data"


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        error_types = ["ERROR", "INFO"]
        for error in error_types:
            if error in data:
                self.error_type = error
                j = 0
                for i in error:
                    j += 1
                self.message = data[j + 2::]
                break
        if not self.error_type:
            self.error_type = None
            self.message = None
            return 'Error'
        return 'Good'

    def validate(self, data: any) -> bool:
        super().validate(data)

    def format_output(self, result: str) -> str:
        if result == 'Good':
            return f""


# Testing
print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

print("\nInitializing Numeric Processor...")
numeric = NumericProcessor()
print("Processing data: [1, 2, 3, 4, 5]")
num_res = numeric.process([1, 2, 3, 4, 5])
if numeric.validate(num_res):
    print("Validation: Numeric data verified")
else:
    print("Cant verify all the numbers")
print("Output:", numeric.format_output(num_res))

print("\nInitializing Text Processor...")
text = TextProcessor()
print("Processing data: \"Hello Nexus World\"")
text_res = text.process("Hello Nexus World")
if text.validate(text_res):
    print("Validation: Numeric data verified")
else:
    print("Cant verify all the numbers")
print("Output:", text.format_output(text_res))

print("\nInitializing Log Processor...")
log = LogProcessor()
log_res = log.process("ERROR: Connection timeout")
if log.validate(log_res):
    print("Validation: Numeric data verified")
else:
    print("Cant verify all the numbers")
log.format_output(log_res)

# print("\n=== Polymorphic Processing Demo ===")
# print("Processing multiple data types through same interface...")

# data = (NumericProcessor(), TextProcessor(), LogProcessor())
# to_process = [[1, 2, 3], "hello world ", "INFO: connection lost"]
# i = 0

# for d in data:
#     print(f"Result {i + 1}: ", end='')
#     d.process(to_process[i])
#     d.validate()
#     d.format_output()
#     i += 1
