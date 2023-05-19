from flask import Flask, request
from user_agents import parse
import IP2Location

app = Flask(__name__)

# Load the IP2Location database
database = IP2Location.IP2Location(os.path.join("path_to_your_bin_file", "IP2LOCATION-LITE-DB1.BIN"))

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
    
    print(f"User ID: {user_id} Page: {page} User Agent: {user_agent_string} User IP: {user_ip}")
    print(f"Browser: {user_agent.browser.family} {user_agent.browser.version_string}")
    print(f"OS: {user_agent.os.family} {user_agent.os.version_string}")
    print(f"Device: {'Mobile' if user_agent.is_mobile else 'PC'}")
    print(f"Location: {location.country_long}, {location.region}, {location.city}")
    return {}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000
