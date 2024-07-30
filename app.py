from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import json
import os
import mysql.connector as MySQLdb


import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_respons(promp,question):
    moldel= genai.GenerativeModel('gemini-pro')
    response= moldel.generate_content([promp,question])
    print("*******************",response,"get response********")
    return response.text
def check_que(question,test):
    moldel1= genai.GenerativeModel('gemini-pro')
    response1=moldel1.generate_content([question,test])
    print("******************",response1,"***************")
    # response2=json.loads(response1)
    ans= response1.candidates[0].content.parts[0].text
    print("***********ans=",ans)
    return ans

    

def read_sql(sql,db):
    conn = MySQLdb.connect(host="localhost",    # your host, usually localhost
                    user="root",         # your username
                    passwd="Logesh@121!",  # your password
                    db=db) 
    curr=conn.cursor()
    curr.execute(sql)
    rows=curr.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


prompt=[""" 
        you are an expert in converting english question to sql query!
        the sql databasse has the name mytable and hass the following colums-NAME,
        age,phone,edu 'edu' was his education \n\n For example,\nExample 1- how many entries of record are present?,
        the sql command will be somethhig like this SELET COUNT(*) FROM MYTABLE;
        \nExample 2- tell me all the students studing in the data science class?,
        the sql command will be something like this SELECT * FROM MYTABLE
        where CLASS = "data science";
        also the sql  code should not have '''in beginning or end and sql word in the output'''
        
        
        """,
        """
        just write a genetal content about the topic also this words  not have 'in beginning or end and  word in the output'
        """]
test="""
      cheack the queasion is related to the database and in that database i have deatial about the students like name,age,phone,edu;
      check the question is  related to database, if question not related to my database give responce as 1 if it related to my database give responce as 2 give just  response as 1 or 2 not give any otheer text
      """


st.set_page_config(page_title="AI&Database")
st.header("Ask something.....")

question =  st.text_input("Input: ",key="inpur")

submit=st.button("Get form my data base")

if submit:
    q_type= check_que(question,test)
    print("**************q tupe=",q_type,'**********')
    if q_type=='2':
        response=get_respons(prompt[0],question)
        print(response)
        data=read_sql(response,"gemini")
        st.subheader("From my data ")
        for row in data:
            print(row)
            st.header(row)
    else:
        print("**********",prompt[1],"*********")
        response=get_respons(prompt[1], question)
        st.header(response)
        print("***************",response)
        
 
    