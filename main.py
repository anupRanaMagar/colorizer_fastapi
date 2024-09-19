from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from io import BytesIO
from PIL import Image
from model.model import colorize_image

app = FastAPI()

@app.post("/colorize")
async def colorize_image_endpoint(file: UploadFile = File(...)):
    try:
        # Read the uploaded image file
        image_bytes = await file.read()
        # print(image_bytes)
        # Open the image from the uploaded bytes and convert to RGB
        image = Image.open(BytesIO(image_bytes)).convert("RGB")

        # Call the colorization function (assume this is the function defined earlier)
        colorized_image = colorize_image(image)

        # Save the colorized image into a BytesIO object
        colorized_image_io = BytesIO()
        colorized_image.save(colorized_image_io, format="PNG")
        colorized_image_io.seek(0)  # Reset the stream position to the start

        # Return the colorized image as a streaming response
        return StreamingResponse(colorized_image_io, media_type="image/png")

    except Exception as e:
        # Handle any errors that occur during the process
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")
