from flask import Flask
from flask import Flask, render_template, Response, redirect, request, session, abort, url_for
import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from PIL import Image
from datetime import datetime
from datetime import date
import datetime
import random
from random import seed
from random import randint
from werkzeug.utils import secure_filename
from flask import send_file
import numpy as np
import threading
import time
import shutil
import hashlib
import urllib.request
import urllib.parse
from urllib.request import urlopen
import webbrowser

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  charset="utf8",
  database="certificate_locker"
)


app = Flask(__name__)
##session key
app.secret_key = 'abcdef'
UPLOAD_FOLDER = 'static/upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#####

@app.route('/',methods=['POST','GET'])
def index():
    cnt=0
    act=""
    msg=""

    
    
    if request.method == 'POST':
        username1 = request.form['uname']
        password1 = request.form['pass']
        mycursor = mydb.cursor()
        mycursor.execute("SELECT count(*) FROM nt_register where uname=%s && pass=%s",(username1,password1))
        myresult = mycursor.fetchone()[0]
        if myresult>0:
            session['username'] = username1
            result=" Your Logged in sucessfully**"
            return redirect(url_for('userhome')) 
        else:
            msg="Invalid Username or Password!"
            result="Your logged in fail!!!"
        

    return render_template('index.html',msg=msg,act=act)

@app.route('/login',methods=['POST','GET'])
def login():
    cnt=0
    act=""
    msg=""
    if request.method == 'POST':
        
        username1 = request.form['uname']
        password1 = request.form['pass']
        mycursor = mydb.cursor()
        mycursor.execute("SELECT count(*) FROM nt_login where username=%s && password=%s",(username1,password1))
        myresult = mycursor.fetchone()[0]
        if myresult>0:
            session['username'] = username1
            #result=" Your Logged in sucessfully**"
            return redirect(url_for('admin')) 
        else:
            msg="Your logged in fail!!!"
        

    return render_template('login.html',msg=msg,act=act)


@app.route('/login_cca',methods=['POST','GET'])
def login_cca():
    cnt=0
    act=""
    msg=""
    if request.method == 'POST':
        
        username1 = request.form['uname']
        password1 = request.form['pass']
        mycursor = mydb.cursor()
        mycursor.execute("SELECT count(*) FROM nt_cca where uname=%s && pass=%s && status=1",(username1,password1))
        myresult = mycursor.fetchone()[0]
        if myresult>0:
            session['username'] = username1
            #result=" Your Logged in sucessfully**"
            return redirect(url_for('home_cca')) 
        else:
            msg="Incorrect Username/Password or wait for approval"
        

    return render_template('login_cca.html',msg=msg,act=act)





@app.route('/register',methods=['POST','GET'])
def register():
    result=""
    act=request.args.get('sid')
    mycursor = mydb.cursor()
    
 
    
    if request.method=='POST':
        
        name=request.form['name']
        mobile=request.form['mobile']
        email=request.form['email']
        address=request.form['address']
        uname=request.form['uname']
        pass1=request.form['pass']

        
        now = datetime.datetime.now()
        rdate=now.strftime("%d-%m-%Y")
        mycursor = mydb.cursor()

        mycursor.execute("SELECT count(*) FROM nt_register where uname=%s",(uname, ))
        cnt = mycursor.fetchone()[0]
        if cnt==0:
            mycursor.execute("SELECT max(id)+1 FROM nt_register")
            maxid = mycursor.fetchone()[0]
            if maxid is None:
                maxid=1

            result = hashlib.md5(uname.encode())
            key=result.hexdigest()
            pbkey=key[0:8]
            prkey=key[8:16]
            
            sql = "INSERT INTO nt_register(id, name, mobile, email, address,  uname, pass,private_key,public_key) VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s)"
            val = (maxid, name, mobile, email, address, uname, pass1,pbkey,prkey)
            act="success"
            mycursor.execute(sql, val)
            mydb.commit()            
            print(mycursor.rowcount, "record inserted.")
            ##BC##
            '''sdata="ID:"+str(maxid)+",Student:"+name+",RegNo.:"+regno+",Department:"+dept+",RegDate:"+rdate
            result = hashlib.md5(sdata.encode())
            key=result.hexdigest()

            mycursor1 = mydb.cursor()
            mycursor1.execute("SELECT max(id)+1 FROM sb_blockchain")
            maxid1 = mycursor1.fetchone()[0]
            if maxid1 is None:
                maxid1=1
                pkey="00000000000000000000000000000000"
            else:
                mid=maxid1-1
                mycursor1.execute('SELECT * FROM sb_blockchain where id=%s',(mid, ))
                pp = mycursor1.fetchone()
                pkey=pp[3]
            sql2 = "INSERT INTO sb_blockchain(id,block_id,pre_hash,hash_value,sdata) VALUES (%s, %s, %s, %s, %s)"
            val2 = (maxid1,maxid,pkey,key,sdata)
            mycursor1.execute(sql2, val2)
            mydb.commit()  ''' 
            ####
            act="success"
            #return redirect(url_for('index',act=act)) 
        else:
            act="wrong"
            result="Already Exist!"
    return render_template('register.html',act=act)

@app.route('/reg',methods=['POST','GET'])
def reg():
    result=""
    act=request.args.get('act')
    mycursor = mydb.cursor()
    
 
    
    if request.method=='POST':
        
        name=request.form['name']
        mobile=request.form['mobile']
        email=request.form['email']
        address=request.form['address']
        uname=request.form['uname']
        pass1=request.form['pass']
        

        
        now = datetime.datetime.now()
        rdate=now.strftime("%d-%m-%Y")
        mycursor = mydb.cursor()

        
        mycursor.execute("SELECT max(id)+1 FROM nt_cca")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1

        
    
        sql = "INSERT INTO nt_cca(id, name, mobile, email, address,  uname, pass) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (maxid, name, mobile, email, address, uname, pass1)
        act="success"
        mycursor.execute(sql, val)
        mydb.commit()            
        print(mycursor.rowcount, "record inserted.")
        
        act="success"
        return redirect(url_for('reg',act=act)) 

    
        
    return render_template('reg.html',act=act)

@app.route('/admin',methods=['POST','GET'])
def admin():
    result=""
    
    mycursor = mydb.cursor()
    
    act=request.args.get("act") 
   
    mycursor.execute("SELECT * FROM nt_cca")
    data = mycursor.fetchall()

    if act=="yes":
        rid=request.args.get("rid")
        mycursor.execute("update nt_cca set status=1 where id=%s",(rid,))
        return redirect(url_for('admin')) 
        
        
    return render_template('admin.html',act=act,data=data)



@app.route('/view_user',methods=['POST','GET'])
def view_user():
    result=""
    
    mycursor = mydb.cursor()
    
    mycursor.execute("SELECT * FROM nt_register")
    data = mycursor.fetchall()
    return render_template('view_user.html',data=data)


@app.route('/userhome', methods=['GET', 'POST'])
def userhome():
    uname=""
    msg=""
    act = request.args.get('act')
    if 'username' in session:
        uname = session['username']
    name=""
    message=""
    print(uname)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM nt_register where uname=%s",(uname, ))
    value = mycursor.fetchone()
    prk=value[7]
    pbkey=value[8]
    name=value[1]
    email=value[3]

    now = datetime.datetime.now()
    rdate=now.strftime("%d-%m-%Y")
    mm=now.strftime("%m")
    yy=now.strftime("%y")
    if request.method=='POST':
        
        detail=request.form['detail']
        
        mycursor.execute("SELECT max(id)+1 FROM nt_certificate")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1

        cno="CN"+mm+yy+str(maxid)


        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        
        file_type = file.content_type
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            fname = "EF"+str(maxid)+file.filename
            filename = secure_filename(fname)
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        

        result = hashlib.md5(cno.encode())
        key=result.hexdigest()
        ckey=key[0:8]
        
        ##encryption
        password_provided = prk # This is input in the form of a string
        password = password_provided.encode() # Convert to type bytes
        salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))

        input_file = 'static/upload/'+fname
        output_file = 'static/upload/'+fname
        with open(input_file, 'rb') as f:
            data = f.read()

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)

        with open(output_file, 'wb') as f:
            f.write(encrypted)
            
        
        message="Certificate Owner:"+uname+", KYC Code:"+cno+", Public Key:"+pbkey
        act="yes"
        ##store
        sql = "INSERT INTO nt_certificate(id,uname,ctype,filename,detail,rdate,canno,ckey) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (maxid,uname,'',filename,detail,rdate,cno,ckey)
        mycursor.execute(sql,val)
        mydb.commit()
        ##BC##
        sdata="ID:"+str(maxid)+",User:"+name+", KYC Code:"+cno+", Key:"+ckey+", RegDate:"+rdate
        result = hashlib.md5(sdata.encode())
        key=result.hexdigest()

        mycursor1 = mydb.cursor()
        mycursor1.execute("SELECT max(id)+1 FROM nt_blockchain")
        maxid1 = mycursor1.fetchone()[0]
        if maxid1 is None:
            maxid1=1
            pkey="00000000000000000000000000000000"
        else:
            mid=maxid1-1
            mycursor1.execute('SELECT * FROM nt_blockchain where id=%s',(mid, ))
            pp = mycursor1.fetchone()
            pkey=pp[3]
        sql2 = "INSERT INTO nt_blockchain(id,block_id,pre_hash,hash_value,sdata) VALUES (%s, %s, %s, %s, %s)"
        val2 = (maxid1,maxid,pkey,key,sdata)
        mycursor1.execute(sql2, val2)
        mydb.commit()   
        ####
        
        msg="Upload success"
        
        
    data=[]
    mycursor.execute("SELECT * FROM nt_certificate where uname=%s",(uname,))
    data = mycursor.fetchall()
    
    '''x=0
    for rd in data1:
        dt=[]
        x+=1
        dss=[]
        dt.append(rd[0])
        dt.append(rd[1])
        dt.append(rd[2])
        dt.append(rd[3])
        dt.append(rd[4])
        dt.append(rd[5])
        dt.append(rd[7])
        
        mycursor.execute("SELECT * FROM nt_require where cid=%s",(rd[0],))
        dd = mycursor.fetchall()
        for rd1 in dd:
            ds=[]
            ds.append(rd1[3])
            ds.append(rd1[4])
            dss.append(ds)
        dt.append(dss)
    data.append(dt)'''
            
    print(data)
    if act=="del":
        did = request.args.get('did')
        mycursor.execute("delete from nt_certificate where id=%s", (did))
        mydb.commit()
        return redirect(url_for('userhome'))

    if act=="re":
        cid = request.args.get('cid')
        mycursor.execute("update nt_certificate set c_status=0 where id=%s", (cid,))
        mydb.commit()
        return redirect(url_for('userhome',act='rev'))
    
    
    return render_template('userhome.html',value=value,msg=msg,data=data,act=act,email=email,message=message)

@app.route('/user_certificate', methods=['GET', 'POST'])
def user_certificate():
    uname=""
    msg=""
    act = ""
    cid = request.args.get('cid')
    if 'username' in session:
        uname = session['username']
    name=""
    print(uname)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM nt_register where uname=%s",(uname, ))
    value = mycursor.fetchone()
    prk=value[7]
    pbkey=value[8]
    name=value[1]

    mycursor.execute("SELECT * FROM nt_certificate where uname=%s && id=%s",(uname,cid))
    data = mycursor.fetchone()
    k=data[12]
    efile=""+data[3]
    dfile=data[3]
    if request.method=='POST':
        
        key=request.form['key']
        if k==key:
            act="yes"
            #Decrypt
            password_provided = k # This is input in the form of a string
            password = password_provided.encode() # Convert to type bytes
            salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
            )
            key = base64.urlsafe_b64encode(kdf.derive(password))
            input_file = 'static/upload/'+efile
            output_file = 'static/decrypted/'+dfile
            with open(input_file, 'rb') as f:
                data = f.read()

            fernet = Fernet(key)
            encrypted = fernet.decrypt(data)

            with open(output_file, 'wb') as f:
                f.write(encrypted)
        else:
            act="no"
        

    return render_template('user_certificate.html',act=act,value=value,msg=msg,data=data,fname=dfile)


@app.route('/certificate', methods=['GET', 'POST'])
def certificate():
    uname=""
    msg=""
    act = ""
    cid = request.args.get('cid')

    
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM nt_certificate where id=%s",(cid,))
    data = mycursor.fetchone()
    uname=data[1]
    cno=data[7]
    c_status=data[13]

    
    
    mycursor.execute("SELECT * FROM nt_register where uname=%s",(uname, ))
    value = mycursor.fetchone()
    prk=value[7]
    pbkey=value[8]
    name=value[1]

    now = datetime.datetime.now()
    rdate=now.strftime("%d-%m-%Y")
    
    k=data[12]
    efile="E"+data[3]
    dfile=data[3]
    if request.method=='POST':
        
        key=request.form['key']
        if c_status==1:
            if pbkey==key:
                act="yes"

                ##BC##
                sdata="ID:"+cid+",User:"+name+", KYC Code:"+cno+", RegDate:"+rdate
                result = hashlib.md5(sdata.encode())
                key=result.hexdigest()

                mycursor1 = mydb.cursor()
                mycursor1.execute("SELECT max(id)+1 FROM nt_blockchain")
                maxid1 = mycursor1.fetchone()[0]
                if maxid1 is None:
                    maxid1=1
                    pkey="00000000000000000000000000000000"
                else:
                    mid=maxid1-1
                    mycursor1.execute('SELECT * FROM nt_blockchain where id=%s',(mid, ))
                    pp = mycursor1.fetchone()
                    pkey=pp[3]
                sql2 = "INSERT INTO nt_blockchain(id,block_id,pre_hash,hash_value,sdata) VALUES (%s, %s, %s, %s, %s)"
                val2 = (maxid1,cid,pkey,key,sdata)
                mycursor1.execute(sql2, val2)
                mydb.commit()   
                ####
                
                #Decrypt
                password_provided = prk # This is input in the form of a string
                password = password_provided.encode() # Convert to type bytes
                salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
                kdf = PBKDF2HMAC(
                    algorithm=hashes.SHA256(),
                    length=32,
                    salt=salt,
                    iterations=100000,
                    backend=default_backend()
                )
                key = base64.urlsafe_b64encode(kdf.derive(password))
                input_file = 'static/upload/'+efile
                output_file = 'static/decrypted/'+dfile
                with open(input_file, 'rb') as f:
                    data = f.read()

                fernet = Fernet(key)
                encrypted = fernet.decrypt(data)

                with open(output_file, 'wb') as f:
                    f.write(encrypted)
            else:
                act="no"
                ##BC##
                sdata="ID:"+cid+",User:"+name+", KYC Code:"+cno+", RegDate:"+rdate+", Access by unauthorized"
                result = hashlib.md5(sdata.encode())
                key=result.hexdigest()

                mycursor1 = mydb.cursor()
                mycursor1.execute("SELECT max(id)+1 FROM nt_blockchain")
                maxid1 = mycursor1.fetchone()[0]
                if maxid1 is None:
                    maxid1=1
                    pkey="00000000000000000000000000000000"
                else:
                    mid=maxid1-1
                    mycursor1.execute('SELECT * FROM nt_blockchain where id=%s',(mid, ))
                    pp = mycursor1.fetchone()
                    pkey=pp[3]
                sql2 = "INSERT INTO nt_blockchain(id,block_id,pre_hash,hash_value,sdata) VALUES (%s, %s, %s, %s, %s)"
                val2 = (maxid1,cid,pkey,key,sdata)
                mycursor1.execute(sql2, val2)
                mydb.commit()   
                ####
        else:
            act="denied"
        

    return render_template('certificate.html',act=act,value=value,msg=msg,data=data,fname=dfile)


@app.route('/certificate1', methods=['GET', 'POST'])
def certificate1():
    uname=""
    msg=""
    act = ""
    cid = request.args.get('cid')

    
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM nt_certificate where id=%s",(cid,))
    data = mycursor.fetchone()
    uname=data[1]
    cno=data[7]
    c_status=data[13]
    
    mycursor.execute("SELECT * FROM nt_register where uname=%s",(uname, ))
    value = mycursor.fetchone()
    prk=value[7]
    pbkey=value[8]
    name=value[1]

    now = datetime.datetime.now()
    rdate=now.strftime("%d-%m-%Y")
    
    k=data[12]
    efile=""+data[3]
    dfile=data[3]
    if request.method=='POST':

        #mycursor.execute("update nt_certificate set c_status=0 where id=%s",(cid,))
        #mydb.commit()
        
        key=request.form['key']
        if c_status==1:
            if pbkey==key:
                act="yes"

                ##BC##
                sdata="ID:"+cid+",User:"+name+", KYC Code:"+cno+", RegDate:"+rdate+", Access by "+uname
                result = hashlib.md5(sdata.encode())
                key=result.hexdigest()

                mycursor1 = mydb.cursor()
                mycursor1.execute("SELECT max(id)+1 FROM nt_blockchain")
                maxid1 = mycursor1.fetchone()[0]
                if maxid1 is None:
                    maxid1=1
                    pkey="00000000000000000000000000000000"
                else:
                    mid=maxid1-1
                    mycursor1.execute('SELECT * FROM nt_blockchain where id=%s',(mid, ))
                    pp = mycursor1.fetchone()
                    pkey=pp[3]
                sql2 = "INSERT INTO nt_blockchain(id,block_id,pre_hash,hash_value,sdata) VALUES (%s, %s, %s, %s, %s)"
                val2 = (maxid1,cid,pkey,key,sdata)
                mycursor1.execute(sql2, val2)
                mydb.commit()   
                ####

                
                #Decrypt
                password_provided = prk # This is input in the form of a string
                password = password_provided.encode() # Convert to type bytes
                salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
                kdf = PBKDF2HMAC(
                    algorithm=hashes.SHA256(),
                    length=32,
                    salt=salt,
                    iterations=100000,
                    backend=default_backend()
                )
                key = base64.urlsafe_b64encode(kdf.derive(password))
                input_file = 'static/upload/'+efile
                output_file = 'static/decrypted/'+dfile
                with open(input_file, 'rb') as f:
                    data = f.read()

                fernet = Fernet(key)
                encrypted = fernet.decrypt(data)

                with open(output_file, 'wb') as f:
                    f.write(encrypted)
            else:
                act="no"

        else:
            act="denied"
        

    return render_template('certificate1.html',act=act,value=value,msg=msg,data=data,fname=dfile)



@app.route('/user_status', methods=['GET', 'POST'])
def user_status():
    uname=""
    msg=""
    act = request.args.get('act')
    if 'username' in session:
        uname = session['username']
    name=""
    print(uname)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM nt_register where uname=%s",(uname, ))
    value = mycursor.fetchone()
    prk=value[7]
    pbkey=value[8]
    name=value[1]

    mycursor.execute("SELECT * FROM nt_certificate where uname=%s",(uname, ))
    data = mycursor.fetchall()

    return render_template('user_status.html',value=value,msg=msg,data=data)



@app.route('/user_verify', methods=['GET', 'POST'])
def user_verify():
    fn1=""
    fn=""
    msg=""
    uname=""
    if 'username' in session:
        uname = session['username']
    data3=[]
    act=""
    mycursor = mydb.cursor()
    if request.method=='POST':
        
        cno=request.form['cno']
        #key=request.form['key']

        mycursor.execute("SELECT count(*) FROM nt_certificate where canno=%s",(cno,))
        cnt = mycursor.fetchone()[0]
        if cnt>0:
            mycursor.execute("SELECT * FROM nt_certificate where canno=%s",(cno,))
            data = mycursor.fetchone()
            usr=data[1]
            did=data[0]
            mycursor.execute("SELECT * FROM nt_register where uname=%s",(usr,))
            dd = mycursor.fetchone()
            pbkey=dd[8]

            #if pbkey==key:
            fn=data[3]
            fnn="ER"+fn
            fn1="R"+fn

            mycursor.execute("SELECT * FROM nt_blockchain where block_id=%s",(did,))
            data3 = mycursor.fetchall()
            act="yes"
            #else:
            #    msg="Wrong key!!"
        else:
            msg="Wrong CA Number!!"
            
    
    return render_template('user_verify.html',data3=data3,msg=msg,fname=fn,act=act)

@app.route('/share', methods=['GET', 'POST'])
def share():
    
    act=""
    uname=""
    email=""
    message=""
    fid = request.args.get('fid')
    if 'username' in session:
        uname = session['username']
    data3=[]

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM nt_register where uname=%s",(uname, ))
    value = mycursor.fetchone()
    prk=value[7]
    pbkey=value[8]
    name=value[1]

    
    mycursor.execute("SELECT * FROM nt_certificate where id=%s",(fid,))
    data = mycursor.fetchone()
    fname=data[3]
    cn=data[7]
    key=data[12]
    link="http://localhost:5000/certificate?cid="+fid

    if request.method=='POST':

        mycursor.execute("update nt_certificate set status=1,c_status=1 where id=%s",(fid,))
        mydb.commit()
        email=request.form['email']
        message="Certificate send by "+uname+", KYC Code: "+cn+", Key:"+pbkey+", Link:"+link
        #url="http://iotcloud.co.in/testmail/sendmail.php?email="+email+"&message="+message
        #webbrowser.open_new(url)
        act="1"
        
    return render_template('share.html',act=act,link=link,fid=fid,message=message,email=email)


@app.route('/add_proof', methods=['GET', 'POST'])
def add_proof():
    uname=""
    if 'username' in session:
        uname = session['username']
    name=""
    cid = request.args.get('cid')
    act = request.args.get('act')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM nt_register where uname=%s",(uname, ))
    value = mycursor.fetchone()
    name=value[1]

    mycursor.execute("SELECT * FROM nt_certificate where id=%s",(cid,))
    data = mycursor.fetchone()

    prk=value[7]
    pbkey=value[8]

    now = datetime.datetime.now()
    rdate=now.strftime("%d-%m-%Y")
    
    if request.method=='POST':
        
        detail=request.form['detail']

        mycursor.execute("SELECT max(id)+1 FROM nt_proof")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
            
        

        
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        
        file_type = file.content_type
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            fname = "P"+str(maxid)+file.filename
            filename = secure_filename(fname)
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        

        ##encryption
        password_provided = pbkey # This is input in the form of a string
        password = password_provided.encode() # Convert to type bytes
        salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))

        input_file = 'static/upload/'+fname
        output_file1 = 'static/upload/E'+fname
        with open(input_file, 'rb') as f:
            data = f.read()

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)

        with open(output_file1, 'wb') as f:
            f.write(encrypted)
            
        
        
        ##store
        sql = "INSERT INTO nt_proof(id,uname,cid,filename,detail,rdate) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (maxid,uname,cid,filename,detail,rdate)
        mycursor.execute(sql,val)
        mydb.commit()
        
        msg="Upload success"
        return redirect(url_for('add_proof'))
            
    mycursor.execute("SELECT * FROM nt_proof where cid=%s",(cid,))
    data2 = mycursor.fetchall()

    if act=="apply":
        print("")
        mycursor.execute("update nt_certificate set status=1 where id=%s", (cid,))
        mydb.commit()
        
        

    
    return render_template('add_proof.html',value=value,cid=cid,data=data,data2=data2)



@app.route('/home_cca', methods=['GET', 'POST'])
def home_cca():
    uname=""
    sid=""
    if 'username' in session:
        uname = session['username']
    name=""
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM nt_require where verifier=%s && status=1",(uname,))
    data = mycursor.fetchall()
    
    
        
    return render_template('home_cca.html',data=data)


@app.route('/add_require', methods=['GET', 'POST'])
def add_require():
    uname=""
    if 'username' in session:
        uname = session['username']
    name=""
    cid = request.args.get('cid')
    act = request.args.get('act')
    mycursor = mydb.cursor()
    #mycursor.execute("SELECT * FROM nt_register where uname=%s",(uname, ))
    #value = mycursor.fetchone()
    #name=value[1]

    mycursor.execute("SELECT * FROM nt_certificate where id=%s",(cid,))
    data2 = mycursor.fetchone()

    now = datetime.datetime.now()
    rdate=now.strftime("%d-%m-%Y")
    
    if request.method=='POST':
        
        detail=request.form['detail']

        mycursor.execute("SELECT max(id)+1 FROM nt_require")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
            
        
        
        ##store
        sql = "INSERT INTO nt_require(id,uname,cid,detail,rdate) VALUES (%s, %s, %s, %s, %s)"
        val = (maxid,uname,cid,detail,rdate)
        mycursor.execute(sql,val)
        mydb.commit()
        
        msg="Upload success"
        return redirect(url_for('add_require',cid=cid,act=act))
            
    mycursor.execute("SELECT * FROM nt_proof where cid=%s",(cid,))
    data = mycursor.fetchall()
    
    return render_template('add_require.html',act=act,cid=cid,data=data,data2=data2)


@app.route('/send_req', methods=['GET', 'POST'])
def send_req():
    uname=""
    if 'username' in session:
        uname = session['username']
    name=""
    act=request.args.get('act')
    mycursor = mydb.cursor()
    

    now = datetime.datetime.now()
    rdate=now.strftime("%d-%m-%Y")
    
    if request.method=='POST':
        
        userid=request.form['userid']
        detail=request.form['detail']

        mycursor.execute("SELECT max(id)+1 FROM nt_require")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
            
        
        
        ##store
        sql = "INSERT INTO nt_require(id,uname,detail,rdate,verifier) VALUES (%s, %s, %s, %s, %s)"
        val = (maxid,userid,detail,rdate,uname)
        mycursor.execute(sql,val)
        mydb.commit()
        act="1"
        msg="success"
        return redirect(url_for('send_req',act=act))
        
    
    return render_template('send_req.html',act=act)

@app.route('/sharereq', methods=['GET', 'POST'])
def sharereq():
    uname=""
    act=request.args.get('act')
    rid=request.args.get('rid')
    sid=""
    if 'username' in session:
        uname = session['username']
    name=""
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM nt_certificate where uname=%s",(uname,))
    cdata = mycursor.fetchall()

    mycursor.execute("SELECT * FROM nt_register where uname=%s",(uname, ))
    value = mycursor.fetchone()
    name=value[1]
    prk=value[7]
    pbkey=value[8]
    

    if request.method=='POST':
        
        cid=request.form['cid']
        mycursor.execute("SELECT * FROM nt_certificate where id=%s",(cid,))
        cdd = mycursor.fetchone()

        cno=cdd[7]
        ckey=cdd[12]

        mycursor.execute("update nt_certificate set c_status=1 where id=%s",(cid,))
        mydb.commit()

        mycursor.execute("update nt_require set cid=%s,cno=%s,ckey=%s,status=1 where id=%s",(cid,cno,pbkey,rid))
        mydb.commit()
        return redirect(url_for('sharereq',act='1'))
        
    
        
    return render_template('sharereq.html',cdata=cdata,act=act)

@app.route('/view_req', methods=['GET', 'POST'])
def view_req():
    uname=""
    sid=""
    if 'username' in session:
        uname = session['username']
    name=""
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM nt_require where uname=%s order by id desc",(uname,))
    data = mycursor.fetchall()
    
    
        
    return render_template('view_req.html',data=data)


@app.route('/verify_cca', methods=['GET', 'POST'])
def verify_cca():
    uname=""
    if 'username' in session:
        uname = session['username']
    name=""
    cid = request.args.get('cid')
    act = request.args.get('act')
    mycursor = mydb.cursor()
    
    mycursor.execute("SELECT * FROM nt_certificate where id=%s && status=0",(cid,))
    data = mycursor.fetchone()
    fn=data[3]
    fnn="R"+fn
    usr=data[1]
    mycursor.execute("SELECT * FROM nt_register where uname=%s",(usr, ))
    value = mycursor.fetchone()
    pbkey=value[8]
    
    mycursor.execute("SELECT * FROM nt_proof where cid=%s",(cid,))
    data2 = mycursor.fetchall()

    now = datetime.datetime.now()
    rdate=now.strftime("%d-%m-%Y")
    
    if act=="transfer":
        mycursor.execute("update nt_certificate set status=2,transfer_cca=%s where id=%s", (rdate,cid))
        mydb.commit()

        ################
        
        filepath = "static/upload/"+fn
        '''img = Image.open(filepath)
          
        # get width and height
        width = img.width
        height = img.height
        w=width-140
        h=height-120
        w2=width-200
        h2=height-80

        # Opening the primary image (used in background)
        img1 = Image.open(filepath)
          
        # Opening the secondary image (overlay image)
        img2 = Image.open("static/images/seal2.png")
        img3 = Image.open("static/images/sign3.png")
          
        # Pasting img2 image on top of img1 
        # starting at coordinates (0, 0)
        img1.paste(img2, (w,h), mask = img2)
        img1.paste(img3, (w2,h2), mask = img3)
        img1.save("static/upload/"+fnn)'''
        ###
        ##encryption
        password_provided = pbkey # This is input in the form of a string
        password = password_provided.encode() # Convert to type bytes
        salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))

        input_file = 'static/upload/'+fnn
        output_file = 'static/upload/E'+fnn
        with open(input_file, 'rb') as f:
            data11 = f.read()

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data11)

        with open(output_file, 'wb') as f:
            f.write(encrypted)
        ###############################
        ##BC##
        sdata="ID:"+cid+", Verifier:"+uname+", Verified, RegDate:"+rdate
        result = hashlib.md5(sdata.encode())
        key=result.hexdigest()

        mycursor1 = mydb.cursor()
        mycursor1.execute("SELECT max(id)+1 FROM nt_blockchain")
        maxid1 = mycursor1.fetchone()[0]
        if maxid1 is None:
            maxid1=1
            pkey="00000000000000000000000000000000"
        else:
            mid=maxid1-1
            mycursor1.execute('SELECT * FROM nt_blockchain where id=%s',(mid, ))
            pp = mycursor1.fetchone()
            pkey=pp[3]
        sql2 = "INSERT INTO nt_blockchain(id,block_id,pre_hash,hash_value,sdata) VALUES (%s, %s, %s, %s, %s)"
        val2 = (maxid1,cid,pkey,key,sdata)
        mycursor1.execute(sql2, val2)
        mydb.commit()   
        ####
        return redirect(url_for('transfer_cca'))
    elif act=="reject":
        mycursor.execute("update nt_certificate set status=3,transfer_cca=%s where id=%s", (rdate,cid))
        mydb.commit()
        ##BC##
        sdata="ID:"+cid+", Verifier:"+uname+", Rejected, RegDate:"+rdate
        result = hashlib.md5(sdata.encode())
        key=result.hexdigest()

        mycursor1 = mydb.cursor()
        mycursor1.execute("SELECT max(id)+1 FROM nt_blockchain")
        maxid1 = mycursor1.fetchone()[0]
        if maxid1 is None:
            maxid1=1
            pkey="00000000000000000000000000000000"
        else:
            mid=maxid1-1
            mycursor1.execute('SELECT * FROM nt_blockchain where id=%s',(mid, ))
            pp = mycursor1.fetchone()
            pkey=pp[3]
        sql2 = "INSERT INTO nt_blockchain(id,block_id,pre_hash,hash_value,sdata) VALUES (%s, %s, %s, %s, %s)"
        val2 = (maxid1,cid,pkey,key,sdata)
        mycursor1.execute(sql2, val2)
        mydb.commit()   
        ####
        return redirect(url_for('transfer_cca'))
    
    
    return render_template('verify_cca.html',act=act,cid=cid,data=data,data2=data2)



@app.route('/approve_cca', methods=['GET', 'POST'])
def approve_cca():
    uname=""
    sid=""
    if 'username' in session:
        uname = session['username']
    name=""
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM nt_certificate where status=2")
    data = mycursor.fetchall()
    
    
        
    return render_template('approve_cca.html',data=data)

@app.route('/cca_verify', methods=['GET', 'POST'])
def cca_verify():
    uname=""
    sid=""
    if 'username' in session:
        uname = session['username']
    name=""
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM nt_certificate where status=1")
    data = mycursor.fetchall()
    
    
        
    return render_template('cca_verify.html',data=data)


@app.route('/verify', methods=['GET', 'POST'])
def verify():
    fn1=""
    msg=""
    data3=[]
    act=""
    mycursor = mydb.cursor()
    if request.method=='POST':
        
        cno=request.form['cno']
        key=request.form['key']

        mycursor.execute("SELECT count(*) FROM nt_certificate where canno=%s",(cno,))
        cnt = mycursor.fetchone()[0]
        if cnt>0:
            mycursor.execute("SELECT * FROM nt_certificate where canno=%s",(cno,))
            data = mycursor.fetchone()
            usr=data[1]
            did=data[0]
            mycursor.execute("SELECT * FROM nt_register where uname=%s",(usr,))
            dd = mycursor.fetchone()
            pbkey=dd[8]

            if pbkey==key:
                fn=data[3]
                fnn="ER"+fn
                fn1="R"+fn

                mycursor.execute("SELECT * FROM nt_blockchain where block_id=%s",(did,))
                data3 = mycursor.fetchall()
                act="yes"
            else:
                msg="Wrong key!!"
        else:
            msg="Wrong KYC Code!!"
            
    
    return render_template('verify.html',data3=data3,msg=msg,fname=fn1,act=act)

@app.route('/view_block', methods=['GET', 'POST'])
def view_block():
    msg=""
    sid = request.args.get('sid')
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM sb_blockchain where block_id=%s",(sid, ))
    data = mycursor.fetchall()
       
    
    return render_template('view_block.html', data=data)





@app.route('/down', methods=['GET', 'POST'])
def down():
    fname = request.args.get('fname')
    path="static/decrypted/"+fname
    return send_file(path, as_attachment=True)



@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    #session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=5000)
