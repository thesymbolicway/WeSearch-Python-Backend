from flask import Flask, jsonify

app = Flask(__name__)

users = [
         {"id":1,"name":"Ben"},
         {"id":2,"name":"Alex"},
         {"id":3,"name":"Ashley"},
         {"id":4,"name":"Rachel"}
         ]

places = [
    {
        "id": 1,
        "name": "Punch Bowl Social Atlanta",
        "category": "Entertainment",
        "price": 150,
        "location": "875 Battery Ave SE Ste 720, Atlanta, GA 30339",
        "image_url": "https://i.ibb.co/vYbCyy0/huge.jpg",
    }, 
    {"id":2,
     "name":"Illuminarium",
     "category":"Entertainment",
     "price":52,
     "location":"550 Somerset Terrace NE, Atlanta, GA 30306",
     "image_url":"https://i.ibb.co/5vkHDZP/illuminarium-atlanta.jpg",
     "reviews":[{"id":2,"user_id":1,"place_id":2,"review":" What's an adults-only movie theater without some adult-only snacks?","star_rating":4,"user":{"id":1,"name":"Ben"}}]
    },
    {"id":3,
     "name":"Truist Park",
     "category":"Venues",
     "price":123,
     "location":"755 Battery Ave SE, Atlanta, GA 30339",
     "image_url":"https://i.ibb.co/KKNB1m9/Atlanta-Braves-Truist-Park-at-Night-scaled-e1625510805812.jpg",
     "reviews":[{"id":3,"user_id":3,"place_id":3,"review":"Love the reclining and heated seats?","star_rating":5,"user":{"id":3,"name":"Ashley"}}]},
    {"id":4,
     "name":"State Farm Arena",
     "category":"Venues",
     "price":104,
     "location":"1 State Farm Dr, Atlanta, GA 30303",
     "image_url":"https://i.ibb.co/BCfFn7T/philips-arena-1.jpg",
     "reviews":[{"id":4,"user_id":3,"place_id":4,"review":"Nice and spacious","star_rating":3,"user":{"id":4,"name":"Rachel"}}]},
    {"id":5,
     "name":"All Star Mobile Detailing",
     "category":"Auto",
     "price":196,
     "location":"210 Sandy Springs Pl NE, Atlanta, GA 30328",
     "image_url":"https://i.ibb.co/8DkL5P2/Gold-Logo.jpg",
     "reviews":[{"id":5,"user_id":3,"place_id":4,"review":"Ripped me off, dudes are a scam","star_rating":1,"user":{"id":4,"name":"Rachel"}}]},
    {"id":6,
     "name":"Express Oil Change & Tire Engineers",
     "category":"Auto",
     "price":92,
     "location":"5811 Roswell Rd NE, Sandy Springs, GA 30328",
     "image_url":"https://i.ibb.co/ZL1JZH3/761187.jpg",
     "reviews":[{"id":6,"user_id":1,"place_id":6,"review":"My car was looking like Fred Flinstones afterwards","star_rating":2,"user":{"id":1,"name":"Ben"}}]},
    {"id":7,
     "name":"Copelands",
     "category":"Restaurants",
     "price":145,
     "location":"3101 Cobb Pkwy SE #220, Atlanta, GA 30339",
     "image_url":"https://i.ibb.co/D16fB84/cumberland-exterior.jpg",
     "reviews":[{"id":7,"user_id":2,"place_id":7,"review":"Best tequila in town","star_rating":4,"user":{"id":1,"name":"Ben"}}]},
    {"id":8,
     "name":"Volcano Steak & Sushi",
     "category":"Restaurants",
     "price":87,
     "location":"1985 Cobb Pkwy NW, Kennesaw, GA 30152",
     "image_url":"https://i.ibb.co/QvqR2mx/1540009565299-w2880-bb.jpg",
     "reviews":[{"id":8,"user_id":2,"place_id":7,"review":"A boozy time to remember, or not","star_rating":4,"user":{"id":3,"name":"Ashley"}}]}
]

reviews = [
    {
        "id": 1,
        "review": "Beers too expensive",
        "user_id": 1,
        "place_id": 1,
        "star_rating": 3
    }
]

@app.route('/users')
def get_all_users():
    response = jsonify(users)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/users/<int:user_id>')
def get_user_by_id(user_id):
    user = next((x for x in users if x['id'] == user_id), None)
    if user:
        response = jsonify(user)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/places')
def get_all_places():
    response = jsonify(places)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/places/<int:place_id>')
def get_place_by_id(place_id):
    place = next((x for x in places if x['id'] == place_id), None)
    if place:
        return jsonify(place)
    else:
        return jsonify({"error": "Place not found"}), 404

@app.route('/reviews')
def get_all_reviews():
    return jsonify(reviews)

@app.route('/reviews/<int:review_id>')
def get_review_by_id(review_id):
    review = next((x for x in reviews if x['id'] == review_id), None)
    if review:
        user = next((x for x in users if x['id'] == review['user_id']), None)
        place = next((x for x in places if x['id'] == review['place_id']), None)
        review_data = {
            "id": review['id'],
            "review": review['review'],
            "star_rating": review['star_rating'],
            "user": user,
            "place": place
        }
        return jsonify(review_data)
    else:
        return jsonify({"error": "Review not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9292)


