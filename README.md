🌱 Crop Recommendation System using KMeans Clustering
This is a machine learning-powered web application built with Flask that recommends the most suitable crop to grow based on soil and environmental parameters. It uses a pre-trained KMeans clustering model to analyze the user's input and provide accurate crop suggestions.

📌 Features
🧪 Input soil and climate parameters like N, P, K, Temperature, Humidity, pH, and Rainfall

🌾 Get the most suitable crop for your field based on KMeans clustering

💻 Simple and intuitive web interface for easy usage

🚀 Deployed using Flask and supports local hosting

📂 Project Structure
graphql
Copy
Edit
├── app.py                # Main Flask application
├── KMeans_model.lb       # Pre-trained KMeans model (loaded via joblib)
├── farmer.csv            # Dataset used for training/testing
├── p_1.ipynb             # Notebook for data preprocessing and model training
├── templates/
│   ├── home.html         # Homepage of the web app
│   ├── input_page.html   # Form to collect user inputs
│   └── predicted_page.html # Displays crop prediction
🔧 Requirements
To run the project locally, you need:

Python 3.7+

Flask

scikit-learn

joblib

pandas

numpy

Install all dependencies using:

bash
Copy
Edit
pip install -r requirements.txt
🚀 How to Run the Application
Clone the repository

bash
Copy
Edit
git clone https://github.com/yourusername/crop-recommendation.git
cd crop-recommendation
Ensure the model file (KMeans_model.lb) is present

Run the Flask app

bash
Copy
Edit
python app.py
Open your browser and go to

cpp
Copy
Edit
http://127.0.0.1:2525/
🖥️ Web Pages
1. Home Page
URL: /

Basic landing page with navigation

2. Input Page
URL: /input_page

Form to enter soil and climate details

3. Predicted Page
URL: /predicted_page

Receives POST request, performs prediction, and displays the suggested crop

🧠 Machine Learning Model
Model Used: KMeans clustering from sklearn

Input Features:

K (Potassium)

N (Nitrogen)

P (Phosphorus)

Temperature

Humidity

pH

Rainfall

Target Output: Crop name (mapped from cluster centers)

The model is trained in p_1.ipynb and saved using joblib.

📊 Dataset
The dataset farmer.csv contains various crop data including essential soil nutrients and climatic conditions.

It is preprocessed and used to train the KMeans model.

Make sure this file is available in the working directory if re-training is needed.

✨ Future Enhancements
Add more ML models for comparison (Random Forest, SVM)

Use dynamic data from weather APIs

Integrate soil health card data

Mobile-friendly interface
