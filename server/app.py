existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']
from flask import Flask

# 1. Initialize the application
app = Flask(__name__)

# 2. Set up the '/' route
@app.route('/')
def home():
    return "Welcome to Flatiron Cars"

# 3. Set up the '/<model>' route
@app.route('/<model>')
def check_model(model):
    # Check if the requested model exists in the array
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"

# 4. Run the server locally
if __name__ == '__main__':
    app.run(debug=True)