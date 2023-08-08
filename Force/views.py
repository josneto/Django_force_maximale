# Import necessary libraries and modules
import logging
import os
import pandas as pd
from django.contrib import messages
from django.shortcuts import render
from joblib import load
from .forms import PredictionForm

# Set up a logger for logging events
logger = logging.getLogger(__name__)

# Get the absolute path of the current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load the saved trained model and scaler from joblib files
MDL = load(os.path.join(BASE_DIR, 'model.joblib'))
SCALER = load(os.path.join(BASE_DIR, 'scaler.joblib'))

# Define the view function for the prediction form
def predict(request):
    # Check if the request method is POST, meaning the form has been submitted
    if request.method == 'POST':
        # Create an instance of PredictionForm with the submitted data
        form = PredictionForm(request.POST)
        # Check if the form data is valid
        if form.is_valid():
            # Extract cleaned form data
            largeur = form.cleaned_data['Largeur']
            rm = form.cleaned_data['RM']
            thickness = form.cleaned_data['Thickness']

            # Preprocess input data for prediction
            input_data = pd.DataFrame({'largeur  (mm)': [largeur], 'RESISTANCE MAXIMARE': [rm], 'Epaisseur (mm)': [thickness]})
            input_data_scaled = SCALER.transform(input_data)

            try:
                # Make prediction using the trained model
                prediction = MDL.predict(input_data_scaled)
                force_max = int(prediction[0])
                
                # Check if force_max is in the range
                if 18000 <= force_max <= 40000:
                    error_message = 'Force Maximale is out of range (18000 - 40000). Please check the input values'
                    logger.warning(error_message)
                    messages.warning(request, error_message)
                else:

                    # Log the prediction result
                    logger.info(f'Prediction result - Force Maximale (N): {force_max}')

                    # Display the prediction result to the user using Django messages
                    messages.success(request, f'Force Maximale: {force_max} N')

                # Render the form template with the form instance to show the form again
                return render(request, 'form.html', {'form': form})
            except ValueError as ve:
                # Log and display an error message for invalid input data
                logger.exception(f'Error while making prediction: {str(ve)}')
                messages.error(request, 'Invalid input data. Please check the input values.')
            except Exception as e:
                # Log and display a generic error message for prediction failures
                logger.exception(f'Error while making prediction: {str(e)}')
                messages.error(request, 'An error occurred while making the prediction. Please try again.')
    else:
        # If the request method is not POST, create a new instance of the form
        form = PredictionForm()
    
    # Render the form template with the form instance for initial rendering or after form submission
    return render(request, 'form.html', {'form': form})
