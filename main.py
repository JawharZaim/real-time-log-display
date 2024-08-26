from fastapi import FastAPI, Request, Form, HTTPException, WebSocket
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
import asyncio

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="templates"), name="static")


LOGS_DIRECTORY = "/opt/odoo/akwa/akwa-git/FAST_API/DockerLog"


@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    # Fetch log file names from the directory
    log_files = [f for f in os.listdir(LOGS_DIRECTORY) if f.endswith('.log')]
    log_files = [f.replace('.log', '') for f in log_files]  # Remove the .log extension
    return templates.TemplateResponse("form.html", {"request": request, "log_files": log_files})

@app.post("/submit")
async def handle_form(request: Request, name: str = Form(...)):
    return RedirectResponse(url=f"/log/{name}", status_code=303)

@app.get("/log/{filename}", response_class=HTMLResponse)
async def read_log(request: Request, filename: str):
    path = os.path.join(LOGS_DIRECTORY, f"{filename}.log")
    try:
        with open(path, "r") as f:
            content = f.read()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Log file not found")

    return templates.TemplateResponse("log.html", {"request": request, "filename": filename, "content": content})


@app.websocket("/ws/log/{filename}")
async def websocket_endpoint(websocket: WebSocket, filename: str):
    print('test')
    await websocket.accept()
    log_file_path = f"{filename}.log"

    if not os.path.isfile(log_file_path):
        await websocket.send_text("Log file not found.")
        await websocket.close()
        return

    # Tail the log file
    with open(log_file_path, "r") as file:
        file.seek(0, os.SEEK_END)  # Move to the end of the file
        while True:
            line = file.readline()
            if line:
                await websocket.send_text(line)
            else:
                await asyncio.sleep(1)  # Sleep briefly to avoid tight loop


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)