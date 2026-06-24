import os
from werkzeug.utils import secure_filename
from flask import current_app
from PIL import Image

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'doc', 'docx'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_uploaded_file(file, folder='uploads'):
    """Save uploaded file and return the filename"""
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], folder)
        os.makedirs(upload_path, exist_ok=True)
        
        # Make filename unique
        base, ext = os.path.splitext(filename)
        counter = 1
        while os.path.exists(os.path.join(upload_path, filename)):
            filename = f"{base}_{counter}{ext}"
            counter += 1
        
        file_path = os.path.join(upload_path, filename)
        file.save(file_path)
        
        return filename
    return None

def resize_image(image_path, max_size=(800, 800)):
    """Resize image to max dimensions"""
    try:
        with Image.open(image_path) as img:
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            img.save(image_path, optimize=True, quality=85)
    except Exception as e:
        print(f"Image resize error: {e}")
