from typing import Any, List


# Processing Stages
class InputStage:
    def process(self, data: Any) -> Any:
        return data


class TransformStage:
    def process(self, *data: Any) -> List:
        final_data = []
        for stage in data:
            final_data.append(stage)
        return (final_data)


class OutputStage:
    def process(self, data: List) -> None:
        print(data)


# Base Class
class ProcessingPipeline():
    def __init__(self, stages: list, pipeline_id: str = "GenericID") -> None:
        self.pipeline_id = pipeline_id
        self.stages = stages

    def process(self, data: Any) -> None:
        try:
            for stage in self.stages:
                data = stage.process(data)
        except Exception:
            print("Something went wrong")


# Data Adapter
class JSONAdapter(ProcessingPipeline):
    def __init__(self, stages: list, pipeline_id: str = "GenJSONID") -> None:
        super().__init__(pipeline_id, stages)

    def process(self, data: Any) -> None:
        if (isinstance(data, dict) and
           'sensor' in data and 'value' in data and 'unit' in data):
            print(f"Processed {data['sensor']} reading: "
                  f"{data['value']}{data['unit']}")
        else:
            print("Need a dictionary type with 'sensor', 'value' and 'unit'")


class CSVAdapter(ProcessingPipeline):
    def __init__(self, stages: list, pipeline_id: str = "GenCSVID") -> None:
        super().__init__(pipeline_id, stages)

    def process(self, data: Any) -> None:
        values = 1
        if isinstance(data, str):
            for i in data:
                values += 1 if i == ',' else 0
            print(values, "values processed")
        else:
            print("Need a string type")


class StreamAdapter(ProcessingPipeline):
    def __init__(self, stages: list, pipeline_id: str = "GenSrteamID") -> None:
        super().__init__(pipeline_id, stages)

    def process(self, data: Any) -> None:
        super().process(data)


# Nexus Manager
class NexusManager:
    def process_pipeline(self, processing: ProcessingPipeline,
                         data: Any) -> None:
        if isinstance(processing, ProcessingPipeline):
            processing.process(data)


# Testing
print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")

print("\nInitializing Nexus Manager...")
nexus = NexusManager()

stream_processing = []
print("\nCreating Data Processing Pipeline...")
stream_processing.append(InputStage())
print("Stage 1: Input validation and parsing")
stream_processing.append(TransformStage())
print("Stage 2: Data transformation and enrichment")
stream_processing.append(OutputStage())
print("Stage 3: Output formatting and delivery")

print("\n=== Multi-Format Data Processing ===")

print("\nProcessing JSON data through pipeline...")
json = JSONAdapter("JSONAdapter_0001", stream_processing)
datajson = dict(sensor='Temp', value=25.6, unit='C')
print("Input:", datajson)
print("Transform: Enriched with metadata and validation")
print("Output:", end=' ')
json.process(datajson)

print("\nProcessing CSV data through same pipeline...")
csv = CSVAdapter("CSVAdapter_0001", stream_processing)
datacsv = 'user,action,timestamp'
print("Transform: Parsed and structured data")
print("Input:", datacsv)
print("Output:", end=' ')
csv.process(datacsv)

print("\nProcessing Stream data through same pipeline...")
stream = StreamAdapter("StreamAdapter_0001", stream_processing)
datastream = 'Real-time sensor stream'
print('Input', datastream)
print("Transform: Aggregated and filtered")
print("Output:", end=' ')
stream.process(datastream)

all_streams = [json, csv, stream]
all_data = [datajson, datacsv, datastream]

print("===Pipeline Chaining Demo===")
print("Pipeline A -> Pipeline B -> Pipeline C")
print("Data flow: Raw -> Processed -> Analyzed -> Stored\n")

i = 0
for streampipe in all_streams:
    nexus.process_pipeline(streampipe, all_data[i])
    i += 1
