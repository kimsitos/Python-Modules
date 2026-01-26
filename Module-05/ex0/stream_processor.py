from typing import Any, List


# Class
class DataProcessor:
    def process(self, data: Any) -> None:
        data = data

    def validate(self) -> None:
        print(f"Data {self.data} ok")

    def format_output(self) -> None:
        print("output", self.data)


class NumericProcessor(DataProcessor):
    def process(self, data: List[int]) -> None:
        self.sum = 0
        self.total_numbers = 0
        try:
            for number in data:
                if not (number >= 0 and number <= 9):
                    break
                else:
                    self.sum += number
                    self.total_numbers += 1
        except TypeError:
            self.sum = None
            self.total_numbers = None

    def validate(self) -> None:
        self.result = True
        if not self.sum and not self.total_numbers:
            self.result = False

    def format_output(self) -> None:
        if not self.result:
            print("No output generated")
        else:
            print(f"Processed {self.total_numbers} numeric values, "
                  f"sum={self.sum}, avg={self.sum/self.total_numbers}")


class TextProcessor(DataProcessor):
    def process(self, data: str) -> None:
        self.words = 0
        self.chars = 0
        try:
            for c in data:
                if not ((c >= 'a' and c <= 'z') or
                        (c >= 'A' and c <= 'Z') or c == ' '):
                    break
                else:
                    if c == ' ':
                        self.words += 1
                    self.chars += 1

        except TypeError:
            self.words = None
            self.chars = None

    def validate(self) -> None:
        self.result = True
        if not self.words and not self.chars:
            self.result = False

    def format_output(self) -> None:
        if not self.result:
            print("No format_output generated")
        else:
            print(f"Processed text {self.chars} characters {self.words} words")


class LogProcessor(DataProcessor):
    def process(self, data: str) -> None:
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

    def validate(self) -> None:
        self.result = True
        if not self.error_type and not self.message:
            self.result = False

    def format_output(self) -> None:
        if self.result:
            print(f"[{self.error_type}] MESSAGE: {self.message}")
        else:
            print("No output generated")


# Testing
print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

print("\nInitializing Numeric Processor...")
numeric = NumericProcessor()
numeric.process([2, 5, 1])
numeric.validate()
numeric.format_output()

print("\nInitializing Text Processor...")
text = TextProcessor()
text.process("hello world")
text.validate()
text.format_output()

print("\nInitializing Log Processor...")
log = LogProcessor()
log.process("ERROR: Connection timeout")
log.validate()
log.format_output()

print("\n=== Polymorphic Processing Demo ===")
print("Processing multiple data types through same interface...")

data = (NumericProcessor(), TextProcessor(), LogProcessor())
to_process = [[1, 2, 3], "hello world :)", "INFO: connection lost"]
i = 0

for d in data:
    print(f"Result {i + 1}: ", end='')
    d.process(to_process[i])
    d.validate()
    d.format_output()
    i += 1
