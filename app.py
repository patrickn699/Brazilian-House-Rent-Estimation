# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:44:00 2020

@author: Prathmesh
"""

import pickle
import numpy as np
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

pik = open('ready.p','rb')
model = pickle.load(pik)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods = ['POST', 'GET'] )
def predict():
    if request.method ==  'POST':
        ar = request.form['area']
        rm = request.form['room']
        ba = request.form['bath']
        ps = request.form['park']
        ho = request.form['hoa']
        re = request.form['rent']
        ta = request.form['tax']
        fi = request.form['fire']
        pe = request.form['pet']
        fu = request.form['fur']
        se = request.form['sel']
        
        if pe == 1:
            pe1 = 0
        else:
            pe1 = 1
            
        if fu == 1:
            fu1 = 0
        else:
            fu1 = 1
        

            
        if se == 'Campinas':
            se0 = 1
            se1 = 0
            se2 = 0
            se3 = 0
            
        elif se == 'Porto Alegre':
            se0 = 0
            se1 = 1
            se2 = 0
            se3 = 0
        
        elif se == 'Rio de Janeiro':
            se0 = 0
            se1 = 0
            se2 = 1
            se3 = 0
        
        elif se == 'Sao Paulo':
            se0 = 0
            se1 = 0
            se2 = 0
            se3 = 1
        
        else:
            se0 = 0
            se1 = 0
            se2 = 0
            se3 = 0
            
            
        ar  = np.log(int(ar))
        ho  = np.log(int(ho))
        re  = np.log(int(re))
        ta  = np.log(int(ta))
        fi  = np.log(int(fi))
         
            
        result = model.predict([[ar,rm,ba,ps,ho,re,ta,fi,se0,se1,se2,se3,pe1,fu1]])
            
            
        
            
            
        
        
        #return ar
        return render_template("index1.html", op = ' Your estimated rent  will be:'+' '+str(result[0])+'$')
        
        



if __name__ == "__main__":
    app.run(debug=True)

