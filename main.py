from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from ultralytics import YOLO
import cv2
import numpy as np
import io
import os   

app = FastAPI()

# Get the absolute path to the .pt file
model_path = os.path.join(os.path.dirname(__file__), "yolov8n.pt")

# Load the YOLO model
model = YOLO(model_path)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello Geeks, Lets make Deployment witn FastApi Easier"}


@app.post("/detect-humans/")
async def detect_humans(file: UploadFile = File(...)):
    # Read the image file
    image_bytes = await file.read()
    image_np = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

    # Run the YOLO model on the image
    results = model(image)

    # Annotate the image with the results
    annotated_image = results[0].plot()

    # Convert the annotated image to a format that can be returned as a response
    _, encoded_image = cv2.imencode(".jpg", annotated_image)
    image_io = io.BytesIO(encoded_image.tobytes())
    return StreamingResponse(image_io, media_type="image/jpeg")






