from psutil import cpu_percent, virtual_memory
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def monitoring(req: Request) -> _TemplateResponse:
    cpu = cpu_percent()
    memory = virtual_memory().percent
    return templates.TemplateResponse(
        request=req, name="index.html", context={"cpu": cpu, "memory": memory, "message": ""}
    )

