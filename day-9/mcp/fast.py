# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def hello_world():
#     return {"messege":"welcome to fastapi"}

# @app.get("/add")
# def hello(a:int,b:int):
#     return {"result":a+b}

# # POST method
# @app.post("/add")
# def add_numbers(a: int, b: int):
#     return {"result": a+b}


# # PUT method
# @app.put("/add")
# def update_numbers(a: int, b: int):
#     return {"updated_result": a+b}


# # DELETE method
# @app.delete("/add")
# def delete_numbers():
#     return {"message": "Addition operation deleted successfully"}

# #http://127.0.0.1:8000/msg
# #http://127.0.0.1:8000/add?a=2&b=10
# #http://127.0.0.1:8000/docs
from fastapi import FastAPI

app = FastAPI()

number = 0

@app.get("/")
def get_number():
    return {"number": number}

@app.post("/add")
def add_number(a: int):
    global number
    number = a
    return {"message": "Number added", "number": number}

@app.put("/update")
def update_number(a: int):
    global number
    number = a
    return {"message": "Number updated", "number": number}