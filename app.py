from flask import Flask, render_template, request

from mbta_finder import find_stop_near

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/find/', methods=['GET', 'POST'])
def find():
    # modify this function so it renders different templates for POST and GET method.
    # aka. it displays the form when the method is 'GET'; it displays the results when
    # the method is 'POST' and the data is correctly processed.
    if request.method == 'POST':
        place = str(request.form["place"])
        route_type=str(request.form["route_type"])
        station_name, wheelchair_boarding = find_stop_near(place,route_type)

        if station_name:
            return render_template(
                "result.html",place=place,route_type=route_type,station_name=station_name, wheelchair_boarding=wheelchair_boarding
            )
        else:
            return render_template("index.html",error=True)
    return render_template("index.html",error=None)




