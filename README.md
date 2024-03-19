# IET-Project---Image-Based-Gaming

## Aim
The primary objective of this project is to develop a real-time gesture-controlled keyboard simulator. By leveraging computer vision techniques, we aim to create an intuitive interface that allows users to control basic keyboard functions through hand gestures captured by a webcam.

## Introduction
Gesture control has emerged as an exciting frontier in human-computer interaction, offering a natural and intuitive means of communication with digital systems. In this project, we harness the power of computer vision to detect and interpret hand gestures in real-time. These gestures are then translated into corresponding keyboard inputs, enabling users to interact with applications without physical input devices.

## Methodology
The methodology employed in this project encompasses several key steps:

1. **Real-time Video Capture**:
   - Initialize a video capture object using OpenCV (`cv2.VideoCapture(0)`). This object captures frames from the webcam in real-time.

2. **GUI Initialization**:
   - Create a named window using OpenCV (`cv2.namedWindow('Result')`) to display the processed output.
   - Create trackbars to allow interactive adjustment of HSV (Hue, Saturation, Value) values used for color segmentation.

3. **Gesture Detection**:
   - Read each frame from the webcam (`cap.read()`), resize it, and flip it horizontally (`cv2.flip(frame, 1)`).
   - Define a region of interest (ROI) within the frame, typically encompassing the area where hand gestures will be performed.
   - Convert the color space of the ROI from BGR to HSV (`cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)`).

4. **Color Segmentation**:
   - Apply Gaussian blur (`cv2.GaussianBlur`) to reduce noise in the image.
   - Define lower and upper thresholds to create a binary mask (`cv2.inRange`) isolating the desired color (usually skin tones representing the hand).

5. **Contour Detection**:
   - Apply morphological operations (`cv2.morphologyEx`), such as opening, to the mask to remove small noise and smooth the edges.
   - Detect contours (`cv2.findContours`) within the binary mask, representing the boundaries of objects.
   - Select the largest contour, typically representing the hand, based on its area (`max(contours, key=lambda x: cv2.contourArea(x))`).

6. **Convex Hull and Extreme Points**:
   - Compute the convex hull of the hand contour (`cv2.convexHull`) to obtain a polygon that encloses the hand region.
   - Identify extreme points of the convex hull, such as the top, bottom, left, and right points, to calculate the center and other parameters.

7. **Gesture Analysis**:
   - Compute Euclidean distances between key points, such as fingertips and palm center (`pairwise.euclidean_distances`), to analyze gestures.
   - Calculate slopes between specific points to determine hand orientation or gesture direction.

8. **Keyboard Simulation**:
   - Based on the analyzed gestures, simulate predefined keyboard commands (e.g., W, A, S, D) using the `Control` class (`control.py`).
   - The `Control` class interprets hand gestures and triggers corresponding keyboard commands using the `directkeys.py` module.

9. **Interactive Control**:
   - Continuously check for user interactions, such as adjusting HSV values through trackbars or activating gesture control with a start button.
   - Upon detecting gestures and analyzing them, simulate keyboard inputs accordingly, allowing users to control applications or games.

10. **Display and User Feedback**:
    - Display the processed output, including the hand ROI, detected contours, and simulated keyboard inputs, in real-time using OpenCV.
    - Print relevant information, such as Euclidean distances and slopes, to the console for debugging or user feedback purposes.

11. **Termination**:
    - Continue the main loop until the user presses the 'Esc' key (`k == 27`), at which point release the video capture object and destroy OpenCV windows.

By following this methodology, the code achieves real-time gesture-controlled keyboard simulation, providing users with an intuitive and interactive means of interfacing with digital systems.


## Implementation
The implementation of the gesture-controlled keyboard simulator consists of three primary components:

1. **final.py**: The main script responsible for capturing webcam input, processing hand gestures, and simulating keyboard inputs based on the detected gestures.
2. **control.py**: A module containing the Control class, which interprets hand gestures and triggers appropriate keyboard commands.
3. **directkeys.py**: A utility module providing functions to simulate keyboard key presses and releases using low-level system calls.

### Libraries used:
•	python 3.x
•	imutils
•	numpy
•	opencv2
•	time
•	sklearn
•	ctypes


### Steps to run the code:
1.	Download the zip file and unzip all in same folder. We have used PyCharm Community Edition to run the codes. You may use other python editors which support the above libraries.
2.	Run the final.py file.
3.	Adjust the HSV values using the track bar, so that only your hand is visible.
4.	After that, set the Start track bar to 1. 

You can now use your hand to control the game. 

### Note: 
1.	Please use plain white or black background for more accuracy. Also, make sure the room is well lit.
2.	You are free to modify the slope and distance values depending upon the gesture you make in control.py.
3.	You can map more gestures with keys. Refer to: https://gist.github.com/dretax/fe37b8baf55bc30e9d63

## Results
Through rigorous testing and experimentation, we have achieved promising results with our gesture-controlled keyboard simulator. Users can effectively control basic keyboard functions using intuitive hand gestures, providing a seamless and engaging interaction experience.

## Conclusion
Gesture control represents a compelling approach to human-computer interaction, offering benefits such as natural interaction, accessibility, and hands-free operation. While our project focuses on a basic implementation of gesture-controlled keyboard input, the underlying principles can be extended and adapted for various applications, including gaming, accessibility tools, and interactive interfaces.

## References
For further exploration and understanding of the technologies and methodologies employed in this project, we recommend the following resources:

- [OpenCV Documentation](https://opencv.org/)
- [NumPy Documentation](https://numpy.org/doc/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [Code to interact with the keyboard keys](https://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game%20#%20http://www.gamespp.com/directx/directInputKeyboardScanCodes.html)

![image](https://github.com/Cborgg/IET-Project---Image-Based-Gaming/assets/118260187/e7fea732-7dd4-4d1c-8fd4-5b907c392315)


## Mentors and Mentees
Mentees:
Gautam Sivakumar
Abhijeet Adi
Akash Reddy


