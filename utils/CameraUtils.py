import cv2
from ffmpy import FFmpeg


def camera_record(t, stop_event ):
    cap = cv2.VideoCapture(-1)
    fourcc = cv2.VideoWriter_fourcc(*'H264')
    out = cv2.VideoWriter('output/'+str(int(t))+'.avi', fourcc, 20.0, (640, 480))
    while cap.isOpened() and not stop_event.is_set():
        ret, frame = cap.read()
        if ret is True:
            out.write(frame)
    ff = FFmpeg(
        inputs={'output/'+str(int(t))+'.avi': None},
        outputs={'output/'+str(int(t))+'.mp4': None}
    )
    ff.cmd
    ff.run()
    cap.release()
    out.release()
    cv2.destroyAllWindows()






