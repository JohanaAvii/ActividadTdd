from fastapi import FastAPI, Header , HTTPException
from pydantic import BaseModel
from math import sqrt

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello FastAPI"}

@app.get("/IsPrime/{num}")
def is_prime(num: int):

    if num>1:
        s=int(num/2)
        for i in range(2,s+1):
            if num%i==0:
                return {"changed": False, "msg": "No es primo"}
                break
        return {"changed": True, "msg": "Es primo"}
    else:
        return {"changed": False, "msg": "No es primo"}


@app.get("/fibonacci/{pos}")
def read_fibonacci(pos: int):
    if pos<1:
        return{"Error": "Posición inválida"}
    if pos==1:
        return {"fibonacci": 0}
    if pos==2:
        return {"fibonacci": 1}
    ant=0
    sig=1
    for i in range(pos-2):     
        num=ant+sig
        ant=sig
        sig=num
      
    return {"fibonacci": sig}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)