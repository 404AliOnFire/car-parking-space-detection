# Car Parking Space Detection Using Computer Vision

This project detects available and occupied parking spaces from a video feed using computer vision techniques. It analyzes predefined parking regions and determines whether each space is free or occupied in real time.

<img width="1096" height="742" alt="car_parking" src="https://github.com/user-attachments/assets/2ed9f3e1-599b-4b0a-84a5-38a6844d04a3" />


## Project Overview
The system works in two stages.  
First, parking space positions are manually selected using a mouse interface.  
Second, a video stream is processed to detect which parking spaces are available based on pixel intensity analysis.

<img width="1092" height="711" alt="threshold_car" src="https://github.com/user-attachments/assets/218b9f08-a8c2-4432-817c-4dd0d7bc04e5" />


## Key Features
* Detects free and occupied parking spaces from video
* Manual parking slot selection using mouse clicks
* Real time visual feedback with bounding boxes
* Displays the number of available parking spaces
* Lightweight and efficient image processing

## Technologies and Libraries
* Python
* OpenCV
* NumPy
* Pickle
* CVZone

## Project Structure
```
car-parking-space-detection/
Main.py
CarParking.py
carPark.mp4
carParkImg.png
car_pos
images/
README.md
```

## Step 1 Define Parking Spaces
Run the following file to define parking spaces manually.

```bash
python CarParking.py
```

Instructions
* Left mouse click to add a parking space
* Right mouse click to remove a parking space
* Positions are saved automatically in the car_pos file

## Step 2 Run Parking Detection
After defining parking spaces, run:

```bash
python Main.py
```

The system will analyze each parking region, mark free spaces in green, and occupied spaces in red. The total number of free spaces is displayed on screen.

## How It Works
1. The video frame is converted to grayscale
2. Noise is reduced using median blur
3. Adaptive thresholding is applied
4. Each parking region is analyzed by counting white pixels
5. A space is considered free if the pixel count is below a threshold

## Dependencies
```
opencv-python
numpy
cvzone
```

## Use Cases
* Smart parking systems
* Computer vision learning projects
* Traffic and parking analysis
* Intelligent transportation systems

## License
This project is licensed under the MIT License.

## Author
Ali Hassoneh
