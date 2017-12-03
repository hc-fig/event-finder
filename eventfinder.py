from flask import Flask  # IN A PYTHON web app you need to specify the data type if its not a string
app = Flask(__name__) #help it determine the route path
# @ symbol= decorator -wrap a function and modify its behavior. route a URL to a return value
@app.route('/') # connecting to a python function(homepage of website)
def index():
    return 'This is the homepage' # this is tying a a URL to a function, ned a return statement. They will see this when you
#launch web server

@app.route('/anotherpage')
def anotherpage():
    return '<h2> you can write html in here <h2>' # to get to this other page you need to use/anotherpage
#from mainpage

@app.route('/profile/<username>') # if you want pages that depend on a variable(particular user). VAriable is
#signified by <>
def profile(username):
    return "Hello %s" % username #returns name if you insert into URL site/profile/name

@app.route('/post/<int:post_id>')#website/post/type in integer (how to use integer)
def post(post_id):
    return '<h2> post ID is %s <h2>' % post_id

if __name__ == "__main__": #only run app if this file is called directly
    app.run(debug=True) #start the app
    # when you run this the site is live
