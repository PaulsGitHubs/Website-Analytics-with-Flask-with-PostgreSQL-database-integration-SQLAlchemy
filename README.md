# Website Analytics with Flask with PostgreSQL database integration & SQLAlchemy

This repository contains a simple website analytics system implemented in Flask and JavaScript. It allows you to track user visits to your website and gather basic information about your users, including:

- The page they're visiting
- Their browser and operating system
- Their device type (mobile or PC)
- Their approximate location (based on IP address)

## Requirements

- Python 3.6 or later
- Flask
- Flask-CORS
- user-agents
- IP2Location
- flask_sqlalchemy 
- psycopg2-binary

## Setup

1. Install the necessary Python packages:

    ```
    pip install flask flask-cors user-agents IP2Location flask_sqlalchemy psycopg2-binary
    ```

2. Download the IP2Location LITE database in BIN format from the [IP2Location website](https://lite.ip2location.com/). Unzip the downloaded file and place the BIN file in the same directory as your Flask app.

3. Replace `'path_to_your_bin_file'` in the Flask app (`analytics.py`) with the correct path to the BIN file.

4. Start the Flask server:

    ```
    python analytics.py
    ```

## Usage

Include the JavaScript code (`analytics.js`) in your website. This code will send a POST request to the Flask server every time a user visits your website. The server will log the user's information and print it to the console.

You can also modify the JavaScript code to suit your needs. For example, you can change the server URL, add additional data fields, or adjust the tracking behavior.

## Privacy

This analytics system respects the "Do Not Track" setting in the user's browser. If this setting is enabled, no analytics data will be sent.

Please ensure that your use of this system complies with all relevant privacy laws and regulations. This may include informing your users about the data you're collecting and giving them the option to opt out.
