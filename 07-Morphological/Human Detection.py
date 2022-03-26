import cv2 
import numpy as np 
import time 
import matplotlib.pyplot as plt 

camera = cv2.VideoCapture(0) 
time.sleep(0.25) 

# initialize the first frame in the video stream 
firstFrame = None 
runsim = 0 
# Give min area to detect 
min_area = 10000 

while(True): 
    # grab the current frame 
    (grabbed, frame) = camera.read() 
    frame = cv2.resize(frame, (480, 360)) 
    
    text = "No Detection" 
    # if the frame could not be grabbed, then we have reached the end. break 
    # of the video 
    if not grabbed: 
        break 
        
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    gray = cv2.GaussianBlur(gray, (3, 3), 0) 
    bg = cv2.waitKey(1) & 0xFF 

    # if the first frame is None, initialize it 
    if bg == ord("c"):
        print("OK") 
        firstFrame = gray 
        runsim = 1 
        continue

    if runsim == 1:
        # compute the absolute difference between the current frame and 
        # first frame 
        frameDelta = cv2.absdiff(firstFrame, gray) 
        thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1] 
        
        # erode and dilate the thresholded image to fill in holes, then find contours 
        # on thresholded image 
        kernel1 = np.ones((11, 11), np.uint8) 
        kernel2 = np.ones((9,9), np.uint8) 
        
        erosion = cv2.erode(thresh, kernel1, iterations = 1) 
        dilation = cv2.dilate(erosion, kernel2, iterations = 2) 
        
        (cnts,_) = cv2.findContours(dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
        
        # loop over the contours 
        for c in cnts:
            # if the contour is too small, ignore it 
            if cv2.contourArea(c) < min_area: 
                continue 
            # compute the bounding box for the contour, draw it on the frame, 
            # and update the text 
            (x, y, w, h) = cv2.boundingRect(c) 
            
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) 
            text = "Detecting" 

        # draw the text and timestamp on the frame 
        cv2.putText(frame, "Status: {}".format(text), (10, 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2) 
        
        # show the frame and record if the user presses a key 
        horizontal1 = np.hstack((firstFrame, frameDelta))
        horizontal2 = np. hstack((thresh, erosion, dilation))
        cv2.imshow("FirstFrame & Frame Different", horizontal1)
        cv2.imshow("Thresh --- Erosion ----- Dilation",horizontal2)
        #cv2.imshow("Thresh", thresh)

    cv2.imshow("Frame", frame) 
    key = cv2.waitKey(1) & 0xFF 

    # if the 'q' key is pressed, break from the lop 
    if key == ord ("q"):
        break 
# cleanup the camera and close any open windows 
camera.release() 
cv2.destroyAllWindows()