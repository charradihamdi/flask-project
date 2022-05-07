import flask
from flask import render_template, jsonify ,request
import requests
import json
import pickle
import numpy as np
from models import Articles,articles_schema,article_schema



# with open('modelsML/model_DT_ML_prediction.pickle', 'rb') as f:
#     clf_lr = pickle.load(f)



# app = flask.Flask(__name__, template_folder='src')

# @app.route('/', methods=['POST'])
# def index():


#         genders_type = flask.request.form['genders_type']
#         #marriage status as boolean YES: 1 , NO: 0
#         marital_status = flask.request.form['marital_status']
#         #Dependents: No. of people dependent on the applicant (0,1,2,3+)
#         dependents = flask.request.form['dependents']
        
#         #dependents = dependents_to_int[dependents.upper()]
        
#         #education status as boolean Graduated, Not graduated.
#         education_status = flask.request.form['education_status']
#         #Self_Employed: If the applicant is self-employed or not (Yes, No)
#         self_employment = flask.request.form['self_employment']
#         #Applicant Income
#         applicantIncome = float(flask.request.form['applicantIncome'])
#         #Co-Applicant Income
#         coapplicantIncome = float(flask.request.form['coapplicantIncome'])
#         #loan amount as integer
#         loan_amnt = float(flask.request.form['loan_amnt'])
#         #term as integer: from 10 to 365 days...
#         term_d = int(flask.request.form['term_d'])
#         # credit_history
#         credit_history = int(flask.request.form['credit_history'])
#         # property are
#         property_area = flask.request.form['property_area']
#         #property_area = property_area_to_int[property_area.upper()]

#         #create original output dict
#         output_dict= dict()
#         output_dict['Applicant Income'] = applicantIncome
#         output_dict['Co-Applicant Income'] = coapplicantIncome
#         output_dict['Loan Amount'] = loan_amnt
#         output_dict['Loan Amount Term']=term_d
#         output_dict['Credit History'] = credit_history
#         output_dict['Gender'] = genders_type
#         output_dict['Marital Status'] = marital_status
#         output_dict['Education Level'] = education_status
#         output_dict['No of Dependents'] = dependents
#         output_dict['Self Employment'] = self_employment
#         output_dict['Property Area'] = property_area
        


#         x = np.zeros(21)
    
#         x[0] = applicantIncome
#         x[1] = coapplicantIncome
#         x[2] = loan_amnt
#         x[3] = term_d
#         x[4] = credit_history

#         print('------this is array data to predict-------')
#         print('X = '+str(x))
#         print('------------------------------------------')

#         pred = clf_lr.predict([x])[0]
        
#         if pred==1:
#             res = '🎊🎊Congratulations! your Loan Application has been Approved!🎊🎊'
#         else:
#                 res = '😔😔Unfortunatly your Loan Application has been Denied😔😔'
        

 
#         #render form again and add prediction
#         return flask.render_template('index.html', 
#                                      original_input=output_dict,
#                                      result=res,)
# #    # req = requests.get('http://localhost:3000/page')
# #    # data = json.loads(req.content)    
# #     return render_template('index.html')



app = flask.Flask(__name__, template_folder='src')

@app.route('/', methods=['POST'])
def index():
    genderClient = request.json['genderClient']
	marriedStatus = request.json['marriedStatus']
    dependentsClient = request.json['dependentsClient']
	educationClient = request.json['educationClient']
	self_EmployedClient = request.json['self_EmployedClient']
	property_AreaClient = request.json['property_AreaClient']
	loan_Amount_TermClient = request.json['loan_Amount_TermClient']
	Applicant_Income = request.json['Applicant_Income']
	CoApplicantIncome = request.json['CoApplicantIncome']
	LoanAmount = request.json['LoanAmount']




	client = Client(
    
	   genderClient=genderClient,
       marriedStatus=marriedStatus ,
       dependentsClient=dependentsClient,
       educationClient=educationClient,
       self_EmployedClient=self_EmployedClient,
       property_AreaClient=property_AreaClient,
       loan_Amount_TermClient=loan_Amount_TermClient,
       Applicant_Income=Applicant_Income,
       CoApplicantIncome=CoApplicantIncome,
       LoanAmount=LoanAmount
		)
    return jsonify(client)
    #return render_template('index.html')
    #return article_schema.jsonify(article)


if __name__ == "__main__":
    app.run(port=4000, debug=True)