from fastapi import FastAPI

app = FastAPI()

@app.get("/get")
def read_root():
    return {"method": "METHOD"}

@app.put("/put")
def put():
    return {"put": "PUT"}

@app.post("/post")
def post():
    return {"post": "POST"}

@app.delete("/delete")
def delete():
    return {"delete": "DELETE"}
