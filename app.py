from flask import Flask, request, render_template
#from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import numpy as np 
# Load the Random Forest CLassifier model
file_name = "model_file.p"
with open(file_name, 'rb') as pickled:
    data = pickle.load(pickled)
    model = data['model']

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')
	
@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()    
    if request.method == 'POST':
        CreditScore = int(request.form['CreditScore'])
        Age = int(request.form['Age'])
        Tenure = int(request.form['Tenure'])
        Balance = float(request.form['Balance'])
        EstimatedSalary = float(request.form['EstimatedSalary'])
        
        country2=request.form['country']
        if(country2=='Geography_France'):
            temp_array = temp_array + [1,0,0]     
        elif (country2=='Geography_Germany'):
            temp_array = temp_array + [0,1,0] 
        elif (country2=='Geography_Spain'):
            temp_array = temp_array + [0,0,1] 


        gender2=request.form['gender']
        if(gender2=='Gender_Female'):
            temp_array = temp_array + [1,0]        
        elif (gender2=='Gender_Male'):
            temp_array = temp_array + [0,1]   
  
			
        #temp_array = temp_array + [Minimum_Nights, Availability,Host_Listing, Reviews,Reviews_by_Month ]
        
        temp_array = [CreditScore, Age, Tenure, Balance, EstimatedSalary]+ temp_array 
        
        data = np.array([temp_array])
 
        my_prediction = int((model.predict(data).reshape(1,-1))[0])
        my_prediction = np.where(my_prediction==1,'likely to Churn.', 'likely to stay with the bank.')
    #    reviews_per_month, calculated_host_listings_count,
    #    availability_365, Bronx, Brooklyn, Manhattan, Queens,
    #    Staten Island, Entire home/apt, Private room, Shared room]])
        return render_template("result.html", my_prediction=my_prediction ,data = data)#lower_limit = my_prediction-5, upper_limit = my_prediction+5,data=data)
if __name__ == "__main__":
    app.run(debug=True)
