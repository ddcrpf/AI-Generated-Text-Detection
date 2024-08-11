from flask import Flask, render_template, request, jsonify, send_file
from keras.models import load_model
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from preprocess import *
from plot_prediction import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def make_prediction():
    if request.method == "POST":
        # Get data from form input
        input_data = request.form.get('inputData')
        print(f"Received input data: {input_data}")  # Debugging statement
        
        # Make a prediction using the model
        predict_prob = predictions(input_data)  # Get the prediction probabilities
        print(f"Prediction probabilities: {predict_prob}")  # Debugging statement
        
        prediction = classify(predict_prob[0])  # Classify the prediction (assuming single prediction)
        print(f"Classified prediction: {prediction}")  # Debugging statement
        
        # Generate and save the plot
        plot_prediction(predict_prob[0][0])
        generate_wordcloud(input_data)
        
        # Render the result on the prediction page
        return render_template("predict.html", prediction=prediction, prediction_plot_path="static/prediction_plot.png", wordcloud_path = "static/word_cloud.png")
    
    return render_template("predict.html", prediction=None, image_path=None)

if __name__ == '__main__':
    app.run(debug=True)
