# Voiceflow Python Package

This is an unofficial Python package for an easy use of the [Voiceflow API.](https://www.voiceflow.com/api/dialog-manager)

#### Basic usage
```python
import os
from voiceflow import Voiceflow

vf = Voiceflow(
    api_key=os.getenv('VOICEFLOW_API_KEY'),
    user_id='abc123',
)

vf.interact(user_input='hello')

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
