from flask import Flask, render_template, request, redirect
import csv
import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    current_year = datetime.datetime.now().year
    return render_template('index.html', year=current_year)

@app.route("/<string:page_name>")
def html_page(page_name):
    current_year = datetime.datetime.now().year
    return render_template(page_name, year=current_year)


def write_to_csv(data):
  with open('database.csv', newline='', mode='a') as database2:
    name = data["name"]
    email = data["email"]
    message = data["message"]
    csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([name,email,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("thankyou.html")
        except:
            return "did not save to database"
    else:
        return "something went wrong. Try again!"