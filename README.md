# Boto3 Demo

Quality control server that aggregates labeled data, and corrects them for any anomalies.

## Setting Up

##### Initialize a virtual enviroment

Windows:

```
$ python3 -m venv venv
$ venv\Scripts\activate.bat
```

Unix/MacOS:

```
$ python3 -m venv venv
$ source venv/bin/activate
```

##### Install requirements

```
$ pip install requirements.txt
```

##### Create Enviromental File

- In root directory, create '.env' file
- Here are the necessary enviromental variables: ACCESS_KEY, SECRET_KEY, REGION_NAME
