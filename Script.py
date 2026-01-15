# uvicorn Script:app --reload
# http://127.0.0.1:8000/docs
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from PIL import Image
import io

app = FastAPI(title="Black & White Image Converter API")

# 🏠 Root route
@app.get("/")
def root():
    return {"message": "Welcome to the Black & White Image Converter API! Use POST /convert to upload an image."}


def convert_to_black_white(image_file: UploadFile):
    """Convert the uploaded image to black and white (grayscale)."""
    try:
        # Open the uploaded image
        image = Image.open(image_file.file)

        # Convert to black and white
        bw_image = image.convert("L")

        # Save it to an in-memory buffer
        buffer = io.BytesIO()
        bw_image.save(buffer, format="JPEG")
        buffer.seek(0)

        return buffer

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing image: {str(e)}")


@app.post("/convert")
async def convert_image(file: UploadFile = File(...)):
    """Endpoint to upload an image and get its black & white version."""
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Please upload a valid image file.")

    # Convert the image
    bw_buffer = convert_to_black_white(file)

    # Return the black & white image
    return StreamingResponse(bw_buffer, media_type="image/jpeg")