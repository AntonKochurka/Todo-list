from fastapi import FastAPI

app = FastAPI(title="Todo App API")

@app.get("/")
def root():
    return {"message": "Todo API is running"}