from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"get": "GET"}

@app.put("/")
def put():
    return {"put": "PUT"}

@app.post("/")
def post():
    return {"post": "POST"}

@app.delete("/")
def delete():
    return {"delete": "DELETE"}
