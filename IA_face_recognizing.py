import cv2
from mtcnn import MTCNN
from os import listdir
from os.path import isfile, join

path = "Images"

file_name = [f for f in listdir(path) if isfile(join(path, f))]

print("List of folder file names: \n")

for file in file_name:
    print(file)

print()
print("End of the list\n")
file_name = input("Name of the file without '.jpg'. Example file name: 'Image1.jpg',just type 'Image1'.\n")

frame = cv2.imread("Images/{}.jpg".format(file_name))

#webcam = cv2.VideoCapture(0) 

detector = MTCNN()

while True:
    try:
        # Read the current frame
        #successeful_frame_read, frame = webcam.read()

        detection = detector.detect_faces(frame)

        cv2.rectangle(frame, (detection[0]["box"][0], detection[0]["box"][1]), 
                            (detection[0]["box"][0]+detection[0]["box"][2], detection[0]["box"][1]+detection[0]["box"][3]),
                            (0, 255, 0), 2) 

        for key in detection[0]["keypoints"]:
            cv2.circle(frame, detection[0]["keypoints"][key], 2, (0,255,0), 2)
            
        cv2.imshow("Face recognition", frame)
        key = cv2.waitKey(1)

        if key==81 or key==113:
            cv2.destroyAllWindows()
            break


    except:
        pass
