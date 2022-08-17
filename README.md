# Voiceflow Python Package

This is an unofficial Python package for an easy use of the [Voiceflow API.](https://www.voiceflow.com/api/dialog-manager)

#### Basic usage
In your virtual environment:
```text
pip install voiceflow
```
Then in your Python code:
```python
import os
from voiceflow import Voiceflow

vf = Voiceflow(
    api_key=os.getenv('VOICEFLOW_API_KEY'),
    user_id='abc123'
)

# Launch the agent
vf_response = vf.interact.launch()

# Send a simple text input
vf_response = vf.interact.text(user_input='hello')


```

You can also call __launch()__ or __text()__ with your custom
__config__:
```python
vf_response = vf.interact.launch(config={'stripSSML': False})
```
Default __config__ values:
```python
{
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
```


<br>
<br>

#### About this project

This project is created and maintained by:
<br>
__Daian Gan__  
Github: [daiangan](https://github.com/daiangan)  
E-mail: daian@ganmedia.com  
Website: https://daiangan.com  
