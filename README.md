## FastAPI

#### Developer: [Sebastián Ramírez](https://github.com/tiangolo)

#### [Tutorial Page](https://fastapi.tiangolo.com/tutorial/intro/)
---

#### What is FastAPI?
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.



#### Installation
```
pip install fastapi

#install uvicorn to work as the server
pip install uvicorn

# install  email-validator
pip install email-validator
```

#### First app
```
# 1. Add a new file in tutorial folder (and change to insert mode by typing I)
vim tutorial/01main.py  

# 2. Copy the below code in main.py
# 1) import FastAPI.
from fastapi import FastAPI
# 2) Create an app instance
app = FastAPI()

# 3) Write a path operation decorator
@app.get("/")

#4) Write a path operation function
async def root():
    return {"message": "Hello World"}

# 3. Save and exit vim
Esc :wq!

# 4. Run the development server
uvicorn 01main:app --reload

```
```
# 5. Check the app content and docs
# check the app in the browser
http://127.0.0.1:8000

# check the interactive API documentation
http://127.0.0.1:8000/docs

# check the alternative automatic documentation
http://127.0.0.1:8000/redoc

# check the raw OpenAPI schema, which includes the API paths and the possible parameters
http://127.0.0.1:8000/openapi.json
```
