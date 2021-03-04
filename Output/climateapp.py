### Import Flash and jsonify ###
from flask import Flask, jsonify

### Create dictionaries ###
precipitation = []

### Set up Flask ###
app = Flask(__name__)

### Flask Routes ###
@app.route("/")
def home():
    return(
     f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return precipitation data as json"""

    return jsonify(precipitation)