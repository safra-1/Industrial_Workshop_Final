from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
import uvicorn

from app.routers import news, summary



# app = FastAPI()

app = FastAPI(
    title="AI based News Summary API",
    version="0.2",
    description="This is the API documentation for News Summary generating by AI.",
   
    contact={
        "name": "Safra",
       
        "email": "safra@gmail.com",
    },
   
    redoc_url="/documentation",
    docs_url="/try-out",
)

app.include_router(news.router)
app.include_router(summary.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the News Summary API"}


#if __name__ == "__main__":
    # uvicorn.run("main:app", host="localhost", port=8001, reload=True)
if __name__ == "__main__":
      uvicorn.run("main:app", host="localhost", port=8011, reload=True)
      