### Do imports ###
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

### Set up Database connection ###
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
measurement = Base.classes.measurement
station = Base.classes.station

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
     # Create our session (link) from Python to the DB
    session = Session(engine)

    #Query prcp data.
    results = session.query(measurement.date, measurement.prcp).\
    filter(measurement.date <= '2017-08-23').\
    filter(measurement.date >= '2016-08-23').\
    order_by(measurement.date.desc()

    session.close()
    
    #Create dictionary from the query
    precipitation = []

    for date, prcp in results:
        precipt= {}
        precipt["date"] = date
        precipt["prcp"] = prcp
        precipitation.append(precipt)

    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
    station_results = session.query(station.station, station.name).all()

    session.close()

    #create dictionary from the query
    stations = []

    for station, name in station_results:
        stns= {}
        stns["station"] = station
        stns["name"] = name
        stations.append(stns)

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
    temps = session.query(measurement.tobs).\
    filter(measurement.date <= '2017-08-23').\
    filter(measurement.date >= '2016-08-23').\
    filter(measurement.station == 'USC00519281').all()

    session.close()

    #create dictionary from the query
    temperatures = []

    for tobs in temps:
        temp= {}
        temp["date"] = date
        temp["tobs"] = tobs
        temperatures.append(temp)

    return jsonify(temperatures)

@app.route("/api/v1.0/<start>")
    start_results = session.query(func.avg(measurement.tobs)).\
    func.max(measurement.tobs)).\
    func.min(measurement.tobs)).\
    filter(measurement.date >= start).\
    group_by(measurement.date).all()

    session.close()

    #create dictionary from the query
    start_date = []

    for date, min, avg, max in start_results:
        start= {}
        start["date"] = date
        start["avg"] = avg
        start["min"] = min
        start["max"] = max
        start_date.append(start)

    return jsonify(start_date)

@app.route("/api/v1.0/<start>/<end>")
    start_end_results = session.query(func.avg(measurement.tobs)).\
    func.max(measurement.tobs)).\
    func.min(measurement.tobs)).\
    filter(measurement.date >= start).\
    filter(measurement.date <= end).\
    group_by(measurement.date).all()

    #create dictionary from the query
    start_end_dates = []

    for date, min, avg, max in start_end_results:
        start_end= {}
        start_end["date"] = data
        start_end["avg"] = avg
        start_end["min"] = min
        start_end["max"] = max
        start_end_dates.append(start_end)

    return jsonify(start_end_dates)


if __name__ == "__main__":
    app.run(debug=True)