from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"method": "GET"}

@app.put("/")
def put():
    return {"method": "PUT"}

@app.post("/")
def post():
    return {"method": "POST"}

@app.delete("/")
def delete():
    return {"method": "DELETE"}
