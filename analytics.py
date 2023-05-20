from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from user_agents import parse
import IP2Location
import os

app = Flask(__name__)

# Configure your database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/dbname'

# Initialize a database instance
db = SQLAlchemy(app)

# Load the IP2Location database
database = IP2Location.IP2Location(os.path.join("path_to_your_bin_file", "IP2LOCATION-LITE-DB1.BIN"))

# Define a model for your analytics data
class AnalyticsData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String)
    page = db.Column(db.String)
    user_agent_string = db.Column(db.String)
    user_ip = db.Column(db.String)
    location_country = db.Column(db.String)
    location_region = db.Column(db.String)
    location_city = db.Column(db.String)

@app.route('/analytics', methods=['POST'])
def analytics():
    data = request.json
    user_id = data.get('user_id')
    page = data.get('page')
    user_agent_string = data.get('user_agent')
    user_agent = parse(user_agent_string)
    
    user_ip = request.remote_addr

    # Look up the location information in the IP2Location database
    location = database.get_all(user_ip)
    
    # Store the analytics data in the database
    analytics_data = AnalyticsData(
        user_id=user_id,
        page=page,
        user_agent_string=user_agent_string,
        user_ip=user_ip,
        location_country=location.country_long,
        location_region=location.region,
        location_city=location.city
    )
    db.session.add(analytics_data)
    db.session.commit()

    return {}, 200

@app.route('/analytics_data', methods=['GET'])
def analytics_data():
    # Fetch all the analytics data from the database
    data = AnalyticsData.query.all()

    # Convert the data to a list of dictionaries, then jsonify it
    data_as_dicts = [item.__dict__ for item in data]
    return jsonify(data_as_dicts)

if __name__ == '__main__':
    # Create all database tables
    db.create_all()
    app.run(host='0.0.0.0', port=5000)
