from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 1) creating db
# config is dict-like object where flask stores settings
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///travel.db"

# creating db object
db = SQLAlchemy(app)

class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    #method to convert data to dict (for json convenience)
    def to_dict(self):
        return{
            "id": self.id,
            "destination": self.destination,
            "country": self.country,
            "rating": self.rating
        }

with app.app_context():
    db.create_all()


# 2) creating routes

# home route
@app.route("/")
def home():
    return jsonify({"message":"Welcome to the Travel API"})

# receive info through api
# /destination route
@app.route("/destinations",methods=["GET"])
def get_destinations():
    destinations = Destination.query.all()              #fetch all rows from db
    return jsonify([destination.to_dict() for destination in destinations])

# /destination/id
@app.route("/destinations/<int:destination_id>", methods=["GET"])
def get_destination(destination_id):
    #query to db
    destination = Destination.query.get(destination_id)
    if destination:
        return jsonify(destination.to_dict())
    else:
        return jsonify({"error":"Destination not found!"}), 404


# send info through api
@app.route("/destinations",methods=["POST"])
def add_destination():
    data = request.get_json()

    new_destination = Destination(destination=data["destination"],
                                  country=data["country"],
                                  rating=data["rating"]) 
    
    db.session.add(new_destination) #SQLAlchemy stages the new row 
    db.session.commit() #actual saving of row

    return jsonify(new_destination.to_dict()), 201 


# Update info through api
@app.route("/destinations/<int:destination_id>",methods=["PUT"])
def update_destination(destination_id):
    data = request.get_json()

    destination = Destination.query.get(destination_id)
    if destination:
        destination.destination = data.get("destination", destination.destination)
        destination.country = data.get("country", destination.country)
        destination.rating = data.get("rating", destination.rating)

        db.session.commit()

        return jsonify(destination.to_dict())
    
    else:
        return jsonify({"error":"Destination not found!"}), 404


# delete info through api
@app.route("/destinations/<int:destination_id>",methods=["DELETE"])
def delete_destination(destination_id):
    destination = Destination.query.get(destination_id)
    if destination:
        db.session.delete(destination)
        db.session.commit()

        return jsonify({"message":"destination was deleted!"})
    
    else:
        return jsonify({"error":"Destination not found!"}), 404


if __name__ == "__main__":
    app.run(debug=True) #constantly refreshing
