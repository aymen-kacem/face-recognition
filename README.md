📸 Real-Time Face Recognition with Python

Harness the power of OpenCV and Face Recognition to identify faces in real-time! This project uses a dataset of face images to recognize individuals through a live webcam feed. 🚀

- 🛠️ Features

Face Detection 🕵️‍♂️: Identifies faces in real-time using a webcam.

Face Recognition 🔍: Matches detected faces against a preloaded dataset.

Live Video Processing 🎥: Works with your webcam for immediate feedback.

Dynamic Name Display ✨: Displays the name of the recognized person or "Unknown" if not recognized.

- 🚀 How It Works
  
Dataset Preparation 📂

Organize your dataset with the following structure:


markdown

Copier le code

dataset/

├── Person1/

│   ├── image1.jpg

│   ├── image2.jpg

└── Person2/

    ├── image1.jpg
    
    └── image2.jpg
    
- Real-Time Recognition 🎥

Detects faces using face_recognition library.

Matches detected faces with precomputed encodings from the dataset.

Displays results on a live webcam feed using OpenCV.

- 🧰 Prerequisites
  
Python 3.8+ 🐍

Libraries:

OpenCV (pip install opencv-python)

face_recognition (pip install face_recognition)

NumPy (pip install numpy)

- 🎬 Usage

Copier le code

python face_recognition.py

Press Q to quit the webcam feed.

- 🖼️ Preview

✨ Future Enhancements

Support for video files 📹

Add emotion recognition 😃😢

Improve performance for larger datasets 🚀

- 🤝 Contribution
  
Feel free to fork this repo and submit pull requests! Contributions are welcome. 😊

Let me know if you'd like me to customize this further! 🚀
