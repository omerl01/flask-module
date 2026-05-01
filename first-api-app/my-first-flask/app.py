from routes.tasks import router
from routes.lists import list_router
from db import init_db
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")
init_db()
app.include_router(router, tags=["tasks"])
app.include_router(list_router, tags=["lists"])

templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html", 
        context={"request": request}
    )

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)