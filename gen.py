import cv2
import random
import time, uuid

RESIZED_WIDTH = 64
RESIZED_WEIGHT = 64
CUT = 0.9

def gen_dataset():
    cap = cv2.VideoCapture(0)

    border_thickness = 3
    PART = 0.33

    while True:
        ret, frame = cap.read()
        height, width, _ = frame.shape
        scenes = []

        x1_part = int(width * PART)
        y1_part = int(height * PART)

        _x1 = 0
        while _x1 + x1_part < width:
            _y1 = 0
            while _y1 + y1_part < height:
                scenes.append((_x1, _y1, _x1 + x1_part, _y1 + y1_part))
                _y1 += y1_part
            _x1 += x1_part

        pivot = random.randint(0, 8)
        x = input("print any key")

        t = time.time()
        while int(time.time() - t) < 5:
            ret, frame = cap.read()
            if ret:
                frame = cv2.flip(frame, 1)
                cv2.rectangle(frame, (scenes[pivot][0], scenes[pivot][1]), (scenes[pivot][2], scenes[pivot][3]), (255, 0, 0), thickness=border_thickness)
                cv2.imshow('Camera', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        faces = []
        not_faces = []
        cnt = 0
        t = time.time()
        while cnt < 10:
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)

            if int(time.time() - t) > 1:
                for i in range(9):
                    x1 = scenes[i][0]
                    y1 = scenes[i][1]
                    x2 = scenes[i][2]
                    y2 = scenes[i][3]
                    cutted_image = frame[y1:y2, x1:x2]

                    if i == pivot:
                        faces.append(cutted_image)
                    else:
                        not_faces.append(cutted_image)
                t = time.time()
                cnt += 1
            else:
                cv2.rectangle(frame, (scenes[pivot][0], scenes[pivot][1]), (scenes[pivot][2], scenes[pivot][3]), (0, 255, 0), thickness=border_thickness)
            cv2.imshow('Camera', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2.rectangle(frame, (scenes[pivot][0], scenes[pivot][1]), (scenes[pivot][2], scenes[pivot][3]), (0, 0, 255), thickness=border_thickness)
        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        for img in faces:
            nome_arquivo = f"faces/img_{uuid.uuid4()}.jpg"
            cv2.imwrite(nome_arquivo, img)
        for img in not_faces:
            nome_arquivo = f"not_faces/img_{uuid.uuid4()}.jpg"
            cv2.imwrite(nome_arquivo, img)


if __name__ == "__main__":
    gen_dataset()
