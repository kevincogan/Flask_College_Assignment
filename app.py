from flask import Flask, render_template, request, redirect, url_for, Response, jsonify
import csv, json

app = Flask(__name__)

#End point that takes you to the homepage on the flask server.
@app.route("/")
def home():
    return render_template("index.html") #Renders the template and launches it on the flask server.

#Receives information from the form then redirects to display it in a table.
@app.route("/formtest", methods=["POST", "GET"])
def form():

    # If the method we receive is a POST method then we redirect the inputed name in the form and build a table with the inputed information.
    if request.method == "POST":
        info = request.form["Name"]
        return redirect(url_for("user", usr=info)) #This redirects to a different endpoint.
    else:
        return render_template("form.html") #Opens the form webpage.

#This takes the last path value and passses it in as a value.
@app.route("/<usr>")
def user(usr):
    return render_template("user.html", Name=usr) #Passes the values from the form to new wepage with the and display the information in a table.


# This take the information from the CSV file and formats the information into a JSON Format.
@app.route("/allegiances")
def conversion2():
    csvFilePath = "allegiance.csv" # Input file.
    jsonFilePath = "converted_books.json" # Converted to JSON file.

    data = [] #reformated style.
    with open(csvFilePath) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for csvRow in csvReader:
            data.append(csvRow)

    #Writing file in JSOM format.
    with open(jsonFilePath, "w") as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))

    data = None
    with open("converted_books.json", "r") as file:
        data = json.load(file)
        return jsonify(data) # Ensure it is in the JSON format.

#This display the JSON file as a table on a webpage on the Flask server.
@app.route("/allegiancedashboard")
def api():
    return render_template("api_call.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8082)
################################################################################
