from fastapi import FastAPI

app = FastAPI(title="CrawlEngine")

@app.get("/")
def read_root():
    return {"message": "CrawlEngine API is running"}
