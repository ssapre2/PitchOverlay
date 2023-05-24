from ultralytics import YOLO

data = 'baseball-detection-2.v1i.yolov8/data.yaml'
imgsz = 640
epochs = 50
batch_size = 16
name = "pitch_detection_v1"

# Trains the model based on given parameters
def train_model(data, imgsz, epochs, batch_size, name):
    model = YOLO('yolov8n.pt')
    print("Model loaded")
    model.train(
        data=data,
        imgsz=imgsz,
        epochs=epochs,
        batch=batch_size,
        name=name
    )
    print("Model trained")
    return model

if __name__ == "__main__":
    #train a model
    fine_tuned_model = train_model(data, imgsz, epochs, batch_size, name)
    #export model
    fine_tuned_model.export(format='onnx')