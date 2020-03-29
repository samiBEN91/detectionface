import cv2

face_cascade=cv2.CascadeClassifier("./haarcascade_frontalface_alt2.xml")
eye_cascade=cv2.CascadeClassifier("./haarcascade_eye.xml")
cap=cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()
    tickmark=cv2.getTickCount()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #passerl image en noir et blanc
    face=face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3) #SCaleFactor nombre de carree
    for x, y, w, h in face: #face est un quadruplet
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    eye=eye_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3) #SCaleFactor nombre de carree
    for x, y, w, h in eye: #face est un quadruplet
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    if cv2.waitKey(1)==ord('q'):
        break
    fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
    cv2.putText(frame, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.imshow('video', frame)
cap.release()
cv2.destroyAllWindows()
#coucou juste un test