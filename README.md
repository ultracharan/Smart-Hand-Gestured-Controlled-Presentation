# Smart-Hand-Gestured-Controlled-Presentation
# Hand Gesture-Controlled Presentation

This project allows you to control a presentation using hand gestures captured by a webcam. The system detects specific hand gestures to navigate through presentation slides and annotate slides in real-time. The project uses OpenCV, CvZone, and NumPy for hand tracking and gesture recognition.

## Features

- Navigate through presentation slides using hand gestures.
- Annotate slides with a pointer or drawing.
- Erase annotations.
- Display the webcam feed alongside the slides.

## Requirements

- Python 3.x
- OpenCV
- CvZone
- NumPy

## Installation

1. Clone the repository:
  
   git clone https://github.com/ultracharan/Smart-Hand-Gestured-Controlled-Presentation.git
   cd hand-gesture-presentation

2. Install the required packages:
    pip install opencv-python cvzone numpy

3. Place your presentation images in the presentation 3 folder. Ensure the images are named in a sorted order.

4. Run the following command to start the application:
   python main2.py

5. Hand Gestures
  Gesture 1: Left - Move to the previous slide. (Thumb up)
  Gesture 2: Right - Move to the next slide. (Pinky up)
  Gesture 3: Pointer - Display a pointer on the slide. (Index and middle fingers up)
  Gesture 4: Draw - Annotate the slide. (Index finger up)
  Gesture 5: Erase - Erase the last annotation. (Index, middle, and ring fingers up)

6. Functions
  Camera Setup: Initialize the webcam and set resolution.
  Hand Detector: Initialize hand detection using CvZone.HandDetector.
  Main Loop: Capture webcam feed, detect hand gestures, navigate slides, and handle annotations.
