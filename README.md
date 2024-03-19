# IET-Project---Image-Based-Gaming

## Aim
The primary objective of this project is to develop a real-time gesture-controlled keyboard simulator. By leveraging computer vision techniques, we aim to create an intuitive interface that allows users to control basic keyboard functions through hand gestures captured by a webcam.

## Introduction
Gesture control has emerged as an exciting frontier in human-computer interaction, offering a natural and intuitive means of communication with digital systems. In this project, we harness the power of computer vision to detect and interpret hand gestures in real-time. These gestures are then translated into corresponding keyboard inputs, enabling users to interact with applications without physical input devices.

## Methodology
The methodology employed in this project encompasses several key steps:

1. **Real-time Hand Tracking**: Utilizing OpenCV, we capture video frames from a webcam and isolate regions of interest (ROI) corresponding to the user's hand.
2. **Gesture Recognition**: By analyzing the color distribution and contours within the ROI, we identify and interpret hand gestures. This involves techniques such as color segmentation, contour analysis, and convex hull detection.
3. **Mapping to Keyboard Inputs**: Detected gestures are mapped to predefined keyboard commands, enabling actions such as movement (forward, backward, left, right) and other interactions.

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

The repository includes three main python(.py) files particularly:
1.	control.py (Code to map gesture- slope and distance with the keys)
2.	directkeys.py (Code to interact with the keyboard keys. Reference: https://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game%20#%20http://www.gamespp.com/directx/directInputKeyboardScanCodes.html)
3.	final.py (Main code to take input i.e. hand gesture using background subtraction method, find end points of hand and henceforth distance and slope using convex hull)

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

## Mentors and Mentees
Mentees:
Gautam Sivakumar
Abhijeet Adi
Akash Reddy


