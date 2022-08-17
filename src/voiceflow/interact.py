from dataclasses import dataclass, field

import requests

DEFAULT_CONFIG = {
    'tts': False,
    'stripSSML': True,
    'stopAll': True,
    'stopTypes': [],
    'excludeTypes': [
        'block',
        'debug',
        'flow',
    ]
}


@dataclass
class Interact:
    api_key: str
    user_id: str
    version_id: str
    api_base_url: str = 'https://general-runtime.voiceflow.com'
    headers: dict = field(init=False)

    def __post_init__(self):
        self.headers = {
            'Authorization': self.api_key,
            'versionID': self.version_id,
        }

    def interact_request(self, body: dict) -> dict:
        response = requests.post(
            f'{self.api_base_url}/state/user/{self.user_id}/interact',
            json=body,
            headers=self.headers,
        )
        return response.json()

    def launch(self, config: dict = None) -> dict:
        body = {
            'action': {
                'type': 'launch',
            },
            'config': config or DEFAULT_CONFIG,
        }
        response = self.interact_request(body=body)
        return response

    def text(self,
             user_input: str,
             config: dict = None) -> dict:
        body = {
            'action': {
                'type': 'text',
                'payload': user_input,
            },
            'config': config or DEFAULT_CONFIG,
        }
        response = self.interact_request(body=body)
        return response
