from dataclasses import dataclass, field

import requests


@dataclass
class Interact:
    api_key: str
    user_id: str
    api_base_url: str = 'https://general-runtime.voiceflow.com'
    headers: dict = field(init=False)

    def __post_init__(self):
        self.headers = {
            'Authorization': self.api_key,
        }

    def interact_request(self, body: dict):
        response = requests.post(
            f'{self.api_base_url}/state/user/{self.user_id}/interact',
            json=body,
            headers=self.headers,
        )
        return response.json()

    def launch(self):
        body = {
            'action': {
                'type': 'launch',
            }
        }
        response = self.interact_request(body=body)
        return response

    def text(self, user_input: str):
        body = {
            'action': {
                'type': 'text',
                'payload': user_input,
            }
        }
        response = self.interact_request(body=body)
        return response
