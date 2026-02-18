from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class Space_Station(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0, le=100)
    oxygen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime = Field()
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(None, max_length=200)


def print_report(station: Space_Station):
    station = station.model_dump()
    print('ID:', station.get('station_id'))
    print('Name', station.get('name'))
    print('Crew:', station.get('crew_size'), 'people')
    print(f"Power: {station.get('power_level')}%")
    print(f"Oxygen: {station.get('oxygen_level')}%")
    print('Status:', 'Operational' if station.get('is_operational')
          else 'Non operational')


if __name__ == '__main__':
    space = Space_Station(
        station_id='ISS001',
        name='International Space Station',
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2032-04-23T10:20:30.400+02:30",
        is_operational=False,
        )

    print('Space Station Data Validation')
    print('========================================')
    print('Valid station created:')
    print_report(space)

    print('\n========================================')
    print('Expected validation error:')
    try:
        space = Space_Station(
            station_id='ISS001',
            name='International Space Station',
            crew_size=6,
            power_level=85.5,
            oxygen_level=999999.5,
            last_maintenance="2032-04-23T10:20:30.400+02:30",
            is_operational=False,
            notes="maybe works?")
        print_report(space)
    except Exception as e:
        print(e)
