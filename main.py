from fastapi import FastAPI
from math import sqrt

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello FastAPI"}

@app.get("/IsPrime/{num}")
def is_prime(num: int):
    if num < 2:
        return {"is_prime": False}
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return {"is_prime": False}
    return {"is_prime": True}


#hdsfhhfhdfjk
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)