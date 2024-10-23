from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil
import os

app = FastAPI()

# lets Set up templates and static files
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Create directories for user uploads and gallery if they don't exist
os.makedirs("static/images/user_uploads", exist_ok=True)
os.makedirs("static/images/gallery", exist_ok=True)

# here is a Home page
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Gallery page for viewing posted images
@app.get("/gallery", response_class=HTMLResponse)
async def gallery(request: Request):
    gallery_images = os.listdir("static/images/gallery")
    return templates.TemplateResponse("gallery.html", {"request": request, "images": gallery_images})

# Upload page for customers
@app.get("/upload", response_class=HTMLResponse)
async def upload_page(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

# Handle image upload by customers
@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    file_location = f"static/images/user_uploads/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return RedirectResponse(url="/upload", status_code=303)

# Admin page to post gallery images
@app.get("/admin", response_class=HTMLResponse)
async def admin_page(request: Request):
    return templates.TemplateResponse("admin.html", {"request": request})

# Admin upload to add images to gallery
@app.post("/admin/upload")
async def admin_upload_image(file: UploadFile = File(...)):
    file_location = f"static/images/gallery/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return RedirectResponse(url="/admin", status_code=303)
