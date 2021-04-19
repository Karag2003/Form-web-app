from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response", methods=['POST'])
def render_response():
    number = request.form['num'] 
    food = request.form['food']
    sport = request.form['sport']
    end = 3
    end1 = 2
    #The request object stores information about the request sent to the server.
    #args is an ImmutableMultiDict (like a dictionary but can have mutliple values for the same key and can't be changed)
    #The information in args is visible in the url for the page being requested. ex. .../response?color=blue
    reply = sport + number + food
    reply1 = sport[:end] + number[:end] + food[:end] + number[end:]
    reply2 = food[:end1] + number[:end1] + sport[:end] + number[end1:end] + sport[end1:] + food[end1:] + number[-3:]
    return render_template('response.html', response = reply, response1 = reply1, response2 = reply2)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
