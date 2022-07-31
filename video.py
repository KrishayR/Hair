import cv2
import cvzone

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
img_counter = 0



def pick(hair):
    overlay = cv2.imread(f'styles/{hair}.png', cv2.IMREAD_UNCHANGED)
    while True:
        try:
            _, frame = cap.read()
            gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = cascade.detectMultiScale(gray_scale)
            cv2.putText(frame, 'ESC to close', (500,100), cv2.FONT_HERSHEY_SIMPLEX, 2, (50, 1, 100), 2, cv2.LINE_AA)
            for (x, y, w, h) in faces:
                overlay_resize = cv2.resize(overlay, (int(w*1.5), int(h*1.2)))
                if x > 200 and y > 200:
                    frame = cvzone.overlayPNG(frame, overlay_resize, [x-50, y-100])
                else:
                    continue
            k = cv2.waitKey(1)  
            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                cv2.destroyAllWindows()
                break

        except:
            pass
        cv2.imshow('Hair', frame)
        if cv2.waitKey(10) == ord('q'):
            cv2.destroyAllWindows()
            break

