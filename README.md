
# Multi-Class Eye Disease Detection Using Deep Learning

## Overview

This project is a deep learning-based image classification system designed to identify multiple eye diseases from retinal fundus images. Early detection of eye diseases is important for preventing vision loss, but manual diagnosis can be time-consuming and requires medical expertise. This project aims to assist in the screening process by automatically classifying retinal images into different disease categories.

The model is trained using transfer learning techniques and can recognize various eye conditions from retinal scans with high accuracy.

---

## Problem Statement

Eye diseases such as diabetic retinopathy, glaucoma, cataracts, and retinal disorders can significantly affect vision if not diagnosed at an early stage. Traditional diagnosis relies on expert ophthalmologists and specialized equipment.

The goal of this project is to develop an automated system that can analyze retinal images and predict the corresponding eye disease category, helping in faster and more accessible preliminary screening.

---

## Dataset

The project uses a publicly available retinal image dataset containing multiple eye disease categories.

### Dataset Characteristics

* Retinal fundus images
* Multiple disease classes
* Images collected from different patients
* Used for supervised image classification

### Disease Categories

* Cataract
* Diabetic Retinopathy
* Glaucoma
* Normal Eye
* Other Retinal Diseases

---

## Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* Pandas
* Matplotlib
* OpenCV
* Scikit-learn
* Jupyter Notebook

---

## Project Workflow

### 1. Data Collection

The retinal image dataset is collected and organized into separate folders based on disease categories.

### 2. Data Preprocessing

The images are preprocessed before training:

* Image resizing
* Normalization
* Data augmentation
* Dataset splitting into training, validation, and testing sets

### 3. Model Development

Transfer learning is used to improve classification performance.

Key steps include:

* Loading a pre-trained CNN model
* Freezing base layers
* Adding custom classification layers
* Fine-tuning selected layers

### 4. Model Training

The model is trained using labeled retinal images while monitoring:

* Training accuracy
* Validation accuracy
* Training loss
* Validation loss

### 5. Model Evaluation

The trained model is evaluated using standard classification metrics:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

---

## Model Architecture

The project utilizes a pre-trained convolutional neural network (VGG19) through transfer learning.

Architecture highlights:

* Pre-trained feature extraction layers
* Global pooling layer
* Fully connected dense layers
* Dropout for regularization
* Softmax output layer for multi-class classification

---

## Results

The trained model successfully classifies retinal images into multiple disease categories.

### Performance Metrics

* Test Accuracy: 93%
* Precision: 86%
* Recall: 79%
* F1 Score: 83%


---

## Project Structure

```text
Multi-class-Eye-Disease-Detection/
│
├── dataset/
├── notebooks/
├── models/
├── images/
├── app/
├── requirements.txt
├── README.md
└── model_training.ipynb
```

---

## How to Run the Project

### Clone the Repository

```bash
git clone https://github.com/gireeshpatgar17/Multi-class-Eye-Disease-Detection.git
```

### Navigate to the Project Directory

```bash
cd Multi-class-Eye-Disease-Detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python app.py
```

---

## Future Improvements

* Increase dataset size for better generalization
* Deploy the model as a web application
* Integrate explainable AI techniques such as Grad-CAM
* Improve performance on minority classes
* Support real-time screening in healthcare environments

---

## Learning Outcomes

Through this project, I gained practical experience in:

* Deep Learning
* Transfer Learning
* Medical Image Classification
* Data Preprocessing
* Model Evaluation
* Computer Vision using TensorFlow/Keras
* End-to-End Machine Learning Workflow

---

## Author

**Gireesh Patgar**

Artificial Intelligence and Machine Learning Engineering Student

GitHub: https://github.com/gireeshpatgar17
