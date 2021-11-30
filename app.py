from flask import Flask, request

app = Flask(__name__)

# Contants
default_route_text = "Go to the route '/the_mean&the_list=X' where X is a list of integer. Exemple : /the_mean&the_list=1,2,3" 
mean_route_text = "The mean of the input list is : {}"

# Defining the default page 
@app.route("/")
def home():
	return default_route_text

# Defining the mean calculator page
@app.route("/the_mean")
def the_mean():
    the_list = request.args.get('the_list').split(",")
    the_list_integer = [int(i) for i in the_list]
    mean = meanCalculator(the_list_integer)
    return mean_route_text.format(mean)

# Defining the mean calculator function
def meanCalculator(the_list):
    mean =  sum(the_list) / len(the_list)
    return mean

# Main
if __name__ == "__main__":
    app.run()