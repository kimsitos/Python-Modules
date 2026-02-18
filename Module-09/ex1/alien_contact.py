from pydantic import BaseModel, Field, model_validator
from enum import Enum
from datetime import datetime
from typing import Optional


class ContactType(Enum):
    radio = 1
    visual = 2
    physical = 3
    telepathic = 4


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field()
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0, le=10)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = Field(default=True)

    @model_validator(mode='after')
    def verify(self):
        if self.contact_id[:2:] != 'AC':
            raise ValueError("Contact ID must start with "
                             "\"AC\" (Alien Contact)")
        if (self.contact_type.name == 'pysical' and
           not self.is_verified):
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type.name == 'telepathic' and
           not self.witness_count >= 3):
            raise ValueError("Telepathic contact requires at least "
                             "3 witnesses")
        if self.signal_strength > 7 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include "
                             "received messages")
        return self


def print_report(alien: AlienContact):
    alien = alien.model_dump()
    print('ID:', alien.get('contact_id'))
    print('Type:', alien.get('contact_type').name)
    print('Location:', alien.get('location'))
    print(f"Signal: {alien.get('signal_strength')}/10")
    print(f"Duration: {alien.get('duration_minutes')} minutes")
    print('Witness:', alien.get('witness_count'))
    print('Message:', alien.get('message_received'))


if __name__ == '__main__':
    print("Alien Contact Log Validation")
    print("======================================")

    alien = AlienContact(
        contact_id="AC_2024_001",
        timestamp="2024-10-20T00:00:00",
        location="Valladolid",
        contact_type=ContactType.telepathic,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True
        )
    print("Valid contact report:")
    print_report(alien)

    print('\n======================================')
    print('Expected validation error')
    try:
        alien = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2024-10-20T00:00:00",
            location="Valladolid",
            contact_type=ContactType.telepathic,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            is_verified=True
            )
    except (ValueError, Exception) as e:
        print(e)
