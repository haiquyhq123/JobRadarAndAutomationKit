from fastapi import FastAPI
from app.routers import crawler

app = FastAPI(title="CrawlEngine")

app.include_router(crawler.router)

@app.get("/")
def read_root():
    return {"message": "CrawlEngine API is running"}
