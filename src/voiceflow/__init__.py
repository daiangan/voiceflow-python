from dataclasses import dataclass, field

from .interact import Interact


@dataclass
class Voiceflow:
    api_key: str
    user_id: str
    interact: Interact = field(init=False)

    def __post_init__(self):
        self.headers = {
            'Authorization': self.api_key,
        }
        self.interact = Interact(
            api_key=self.api_key,
            user_id=self.user_id,
        )
