## Get project quotas
This snippet aims at fetching the MAXIMUM quotas for a specific resource in a 
specific Google Cloud Platform Project.

To my knowledge, there is currently no way to fetch the current state of you quotas
(for example, check that you used 50% of your quotas).

## Setup

Setup your default application credentials
```shell
gcloud auth application-default login
```

Create virtualenv venv
```shell
python3 -m venv venv
```

Activate venv
```shell
source venv/bin/activate
```

Install dependencies
```shell
pip install -r requirements.txt
```

Run
```shell
python main.py
```
