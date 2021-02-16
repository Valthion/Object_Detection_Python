from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

while (True):
 os.system('cls')
 print("======PROGRAM DETEKSI GAMBAR=======")
 print("====================================")
 print("PETUNJUK :")
 print("1. Letakkan gambar yang mau diiuji dalam satu folder dengan file ini dan rename dengan nama image.jpg")
 print("2. Silahkan menunggu hingga hasil sudah keluar.")
 pil = str(input("Press ' Y ' Continue OR 'N' To Exit...."))

 if pil == 'Y' or  pil == 'y' :

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    detections, extracted_images = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "image.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"), extract_detected_objects=True)
    os.system('cls')
    for eachObject in detections:
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
    continue

 else:
    print("Exiting App....")
    break