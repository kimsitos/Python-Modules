from pydantic import BaseModel, Field, model_validator
from enum import Enum
from datetime import datetime
from typing import List, Optional


class Rank(Enum):
    commander = 1
    captain = 2
    lieutenant = 3
    officer = 4
    cadet = 5


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field()
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field()
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: Optional[str] = Field('planned')
    budget_millions: float = Field(ge=1, le=10000)

    @model_validator(mode='after')
    def validate_mission(self):
        if self.mission_id[0] != 'M':
            raise ValueError("Mission ID must start with \"M\"")

        captain_found = False
        total_crew = 0
        experience_crew = 0
        for crew in self.crew:
            crew = crew.model_dump()
            if not crew.get('is_active'):
                raise ValueError('All crew members must be active')
                print(crew.get('rank').name)
            if crew.get('rank').value <= 2 and crew.get('is_active'):
                captain_found = True
            experience_crew += 1 if crew.get('years_experience') >= 5 else 0
            total_crew += 1

        if not captain_found:
            raise ValueError('Must have at least one Commander or Captain')

        if self.duration_days > 365 and not experience_crew >= total_crew / 2:
            raise ValueError("Long missions (> 365 days) need 50% "
                             "experienced crew (5+ years)")

        return self


def print_mission(mission: SpaceMission):
    mis = mission.model_dump()
    print('Mission:', mis.get('mission_name'))
    print('ID:', mis.get('mission_id'))
    print('Destination', mis.get('destination'))
    print(f"Duration: {mis.get('duration_days')} days")
    print(f"Budget: ${mis.get('budget_millions')}M")
    print('Crew size:', len(mis.get('crew')))
    print('Crew members:')
    for crew in mis.get('crew'):
        print(f"- {crew.get('name')} ({crew.get('rank').name}) - "
              f"{crew.get('specialization')}")


if __name__ == '__main__':
    mission = SpaceMission(
        mission_id="M2024_TITAN",
        mission_name="Solar Observatory Research Mission",
        destination="Solar Observatory",
        launch_date="2024-03-30T00:00:00",
        duration_days=451,
        crew=[
          CrewMember(
            member_id="CM001",
            name="Sarah Williams",
            rank=Rank.commander,
            age=43,
            specialization="Mission Command",
            years_experience=19,
            is_active=True
          ),
          CrewMember(
            member_id="CM004",
            name="David Smith",
            rank=Rank.cadet,
            age=27,
            specialization="Security",
            years_experience=2,
            is_active=True
          ),
          CrewMember(
            member_id="CM005",
            name="Maria Jones",
            rank=Rank.cadet,
            age=55,
            specialization="Research",
            years_experience=9,
            is_active=True
          )
        ],
        mission_status="planned",
        budget_millions=2208.1
    )

    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    print_mission(mission)

    print("\n=========================================")
    print("Expected validation error:")
    try:
        SpaceMission(
            mission_id="M2024_TITAN",
            mission_name="Solar Observatory Research Mission",
            destination="Solar Observatory",
            launch_date="2024-03-30T00:00:00",
            duration_days=451,
            crew=[
              CrewMember(
                member_id="CM001",
                name="Sarah Williams",
                rank=Rank.cadet,
                age=43,
                specialization="Mission Command",
                years_experience=19,
                is_active=True
              )
            ],
            mission_status="planned",
            budget_millions=2208.1
            )
    except (ValueError, Exception) as e:
        print(e)
