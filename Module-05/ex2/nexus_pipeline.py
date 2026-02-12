from typing import Any, Union
from abc import ABC, abstractmethod


# Processing Stages
class InputStage:
    def process(self, data: Any) -> dict:
        return data


class TransformStage:
    def process(self, *data: Any) -> dict:
        final_data = []
        for stage in data:
            final_data.append(stage)
        return final_data


class OutputStage:
    def process(self, data: Any) -> str:
        return data


# Base Class Pipe
class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str = "GenericID") -> None:
        self.pipeline_id = pipeline_id
        self.stages = []

    def add_stage(self, *stages) -> None:
        for stage in stages:
            self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        try:
            for stage in self.stages:
                data = stage.process(data)
            return data
        except Exception as e:
            return f"Error: {e}"


# Data Adapter
class JSONAdapter(ProcessingPipeline):
    def process(self, data: dict[str, Any]) -> str:
        try:
            sensor = data.get('sensor')
            value = data.get('value')
            unit = data.get('unit')

            if sensor and value and unit:
                return f"Processed {sensor} reading {value}{unit}"
            return "Error getting the data"
        except Exception as e:
            return f"Error: {e}"


class CSVAdapter(ProcessingPipeline):

    def process(self, data: str) -> str:
        try:
            data = data.split(',')
            total_actions = 0
            for d in data:
                if d == 'action':
                    total_actions += 1
            return f"User activity logged: {total_actions} actions processed"
        except Exception as e:
            return f"Error: {e}"


class StreamAdapter(ProcessingPipeline):

    def process(self, data: Any) -> Union[str, Any]:
        super().process(data)


# Nexus Manager
class NexusManager:
    def __init__(self) -> None:
        self._pipelines = []

    def add_pipeline(self, *stages) -> None:
        for stage in stages:
            if isinstance(stage, ProcessingPipeline):
                self._pipelines.append(stage)

    def process_data(self, data: Any) -> Union[str, Any]:
        for pipe in self._pipelines:
            print(pipe.process(data))


# Testing
print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")

print("\nInitializing Nexus Manager...")
nexus = NexusManager()

stream_processing = []
print("\nCreating Data Processing Pipeline...")
print("Stage 1: Input validation and parsing")
stageinput = InputStage()
print("Stage 2: Data transformation and enrichment")
stagetransform = TransformStage()
print("Stage 3: Output formatting and delivery")
stageoutput = OutputStage()

print("\n=== Multi-Format Data Processing ===")

print("\nProcessing JSON data through pipeline...")
json = JSONAdapter("JSONAdapter_0001")
json.add_stage(stageinput, stagetransform, stageoutput)
datajson = {'sensor': 'temp', 'value': 25.6, 'unit': 'C'}
print("Input:", datajson)
print("Transform: Enriched with metadata and validation")
print("Output:", json.process(datajson))


print("\nProcessing CSV data through same pipeline...")
csv = CSVAdapter("CSVAdapter_0001")
csv.add_stage(stageinput, stagetransform, stageoutput)
datacsv = 'user,action,timestamp,action'
print("Transform: Parsed and structured data")
print("Input:", datacsv)
print("Output:", csv.process(datacsv))


print("\nProcessing Stream data through same pipeline...")
stream = StreamAdapter("StreamAdapter_0001")
stream.add_stage(stageinput, stagetransform, stageoutput)
datastream = "Real-time sensor stream"
print('Input', datastream)
print("Transform: Aggregated and filtered")
print("Output:", stream.process(datastream))

print("\n===Pipeline Chaining Demo===")
print("Pipeline A -> Pipeline B -> Pipeline C")
print("Data flow: Raw -> Processed -> Analyzed -> Stored\n")


print("=== Error Recovery Test ===")
nexus.add_pipeline(json, csv, stream)
nexus.process_data(None)
