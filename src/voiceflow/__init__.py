from dataclasses import dataclass, field
from typing import Literal

from .interact import Interact


@dataclass
class Voiceflow:
    api_key: str
    user_id: str
    version_id: Literal['production', 'development'] = 'development'
    interact: Interact = field(init=False)

    def __post_init__(self):
        self.interact = Interact(
            api_key=self.api_key,
            user_id=self.user_id,
            version_id=self.version_id,
        )
