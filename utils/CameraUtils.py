import cv2
from ffmpy import FFmpeg
import time
import threading



def camera_record(t, stop_event ):
    cap = cv2.VideoCapture(-1)
    fourcc = cv2.VideoWriter_fourcc(*'H264')
    out = cv2.VideoWriter('output/'+str(int(t))+'.avi', fourcc, 6, (640, 480))
    frame_counts = 1
    start_time = time.time()
    while cap.isOpened() and not stop_event.is_set():
        ret, frame = cap.read()
        if ret is True:
            out.write(frame)
            frame_counts +=1
    elapsed_time = time.time() - start_time
    recorded_fps = frame_counts / elapsed_time
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    video_thread = threading.Thread(target=video_process, args=(recorded_fps,t))
    video_thread.start()


def video_process(recorded_fps, t):
    if abs(recorded_fps - 6 ) >= 0.01:
        ff = FFmpeg(
            inputs={'output/' + str(int(t)) + '.avi': '-r ' + str(recorded_fps)},
            outputs={'output/' + str(int(t)) + '.mp4': '-r 6'})
    else:
        ff = FFmpeg(
            inputs={'output/'+str(int(t))+'.avi': None},
            outputs={'output/'+str(int(t))+'.mp4': None}
        )
    ff.cmd
    ff.run()







