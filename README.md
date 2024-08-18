# AI powered chatbot

The chatbot is powered by customized small language model and also support retrieval medical information from the database.

[![Demo](https://img.youtube.com/vi/oN55EJ3L3wc/0.jpg)](https://youtu.be/oN55EJ3L3wc?feature=shared)


## Installation

```bash
pip install -r requirements.txt
```

## Different way to run the app

```bash
make download

make up
```

Please use VSCode `Run and Debug` to run the app. 

* `Python Streamlit` for local inference and testing
* `Python Debugger` for launching the backend server in the production environment

![](./img/Screenshot%202024-08-18%20at%205.04.57 PM.png)


# For developer 

After running the app, check address below

```bash

# Root router of the server
http://127.0.0.1:8000

# Swagger UI
http://127.0.0.1:8000/docs
```

![](./img/Screenshot%202024-08-07%20at%2010.28.05 AM.png)