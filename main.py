from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
import sklearn

app = Flask(__name__)

# Load the pre-trained model
with open('model_1.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/')
def index():
    # Render the HTML form
    return render_template('House_Pricing.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve form data
    area = float(request.form['area'])
    bedroom = float(request.form['bedroom'])
    bathroom = float(request.form['bathroom'])
    stories = float(request.form['stories'])
    mainroad = 1 if request.form['mainroad'] == 'YES' else 0
    guestroom = 1 if request.form['guestroom'] == 'YES' else 0
    basement = 1 if request.form['basement'] == 'YES' else 0
    hotwaterheating = 1 if request.form['hotwaterheating'] == 'YES' else 0
    airconditioning = 1 if request.form['airconditioning'] == 'YES' else 0
    parking = float(request.form['parking'])
    prefarea = 1 if request.form['prefarea'] == 'YES' else 0

    # Map furnishing status to numeric values
    furnishingstatus = request.form['furnishingstatus'].lower()
    if furnishingstatus == 'furnished':
        furnishingstatus_encoded = 0
    elif furnishingstatus == 'semifurnished':
        furnishingstatus_encoded = 1
    elif furnishingstatus == 'unfurnished':
        furnishingstatus_encoded = 2
    else:
        return jsonify({'error': 'Invalid furnishing status'}), 400

    # Prepare the input array for the model
    input_features = np.array([[area, bedroom, bathroom, stories, mainroad, guestroom, basement,
                                hotwaterheating, airconditioning, parking, prefarea, furnishingstatus_encoded]])

    # Make the prediction using the model
    prediction = model.predict(input_features)

    # Return the prediction as JSON
    return jsonify({'prediction': prediction[0]})


if __name__ == '__main__':
    app.run(debug=True)
