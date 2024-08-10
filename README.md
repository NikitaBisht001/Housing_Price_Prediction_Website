# Housing_Price_Prediction_Website
# House Price Prediction Web Application

This repository contains a simple web application for predicting house prices based on area using a linear regression model. The app is built using Flask and scikit-learn.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**

    ```bash
    git clone https://github.com/YOUR_USERNAME/house-price-prediction.git
    cd house-price-prediction
    ```

2. **Create and activate a virtual environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Download or create the dataset**

    Ensure you have a dataset named `house_prices.csv` with columns `Area` and `Price`. Place this file in the project directory.

5. **Train the model**

    Run the `train_model.py` script to train the model and save it as `model.pkl`.

    ```bash
    python train_model.py
    ```

6. **Run the Flask app**

    ```bash
    python app.py
    ```

7. **Open your browser and navigate to**

    ```
    http://127.0.0.1:5000/
    ```

## Usage

Once the app is running, enter the area of the house in the input field and click on the "Predict" button. The predicted price will be displayed.

## Contributing

Contributions are welcome! Please open an issue to discuss what you would like to change.

1. Fork the repository
2. Create a new branch (`git checkout -b feature-foo`)
3. Commit your changes (`git commit -am 'Add foo feature'`)
4. Push to the branch (`git push origin feature-foo`)
5. Create a new Pull Request


