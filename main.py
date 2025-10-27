from fastapi import FastAPI

app = FastAPI(title="Email Scraper", version="1.0.0")

@app.get("/")
def read_root():
    return {"Hello": "World"}