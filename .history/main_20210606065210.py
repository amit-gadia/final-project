import codecs
from random import random
import calendar
import re
from flask import *
from flask.app import setupmethod
import mysql.connector
import datetime
import os
conn=mysql.connector.connect(host="localhost",user="root",password="Root",database="cms",auth_plugin="mysql_native_password")
cur=conn.cursor(buffered=True)
app = Flask(__name__)
app.secret_key="abc"
app.config['UPLOAD_FOLDER'] = 'C:\\Users\\safezone\\Desktop\\finalprj\\templates\\notice\\files'
DOWNLOAD_DIRECTORY = 'C:\\Users\\safezone\\Desktop\\finalprj\\templates\\notice\\cfiles'
@app.route('/logout')
def logout():
    session.pop('userid')
    session.pop('user')
    session.pop('userrole')
    
    return main.login()
@app.route('/downloadnotice/<file>')
def down(file):
    print(file)
    return send_from_directory(DOWNLOAD_DIRECTORY, file, as_attachment=True)
class adminnotice:
    @app.route("/tnotice")
    def notice():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/noticeicon")
    @app.route("/noticeicon")
    def show_noticemain():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template("notice/addnotice.html")
    @app.route("/addnewnote",methods=['POST'])
    def add_notice():
        date=request.form['date']
        title=request.form['title']
        description=request.form['description']
        eventtype=request.form['eventtype']
        timing=str(datetime.datetime.now())
        sql="insert into notice(date,name,details,category,timestamp)values(%s,%s,%s,%s,%s);"
        val=(date,title,description,eventtype,timing)
        cur.execute(sql,val)
        conn.commit()
        return view_notice.show_notice()
class hostel:
    @app.route("/addhroom")
    def addroom():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/addroomicon")
    @app.route("/addroomicon")
    def addroomicon():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template("facilities/addroom.html")
    @app.route("/addnewroom",methods=['POST'])
    def adnewroom():
        addroom=request.form['addroom']
        sql="insert into hroom(room_no,status) values(%s,'no');"
        val=(addroom,)
        cur.execute(sql,val)
        conn.commit()
        return hostel.addroomicon()
    
    @app.route("/addhmess")
    def addmess():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/addmessicon")
    @app.route("/addmessicon")
    def addmessicon():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template("facilities/addmess.html")
    @app.route("/addmessroom",methods=['POST'])
    def admessroom():
        breakfast=request.form['breakfast']
        print(breakfast.split(','))
        lunch=request.form['lunch']
        print(lunch.split(','))
        dinner=request.form['dinner']
        print(dinner.split(','))
        sql="delete from mess;" 
        cur.execute(sql)
        sql="insert into mess(breakfast,lunch,dinner) values(%s,%s,%s);"
        val=(breakfast,lunch,dinner)   
        cur.execute(sql,val)
        conn.commit()     
        return render_template("tome.html",text="Mess Menu Added Successfully",id=1)
class adminacc:
    @app.route("/Accounts")
    def acc():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/acco")
    @app.route("/acco")
    def show_Acc():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template("accounts/fee.html")
    @app.route("/fee_det",methods=['POST'])
    def feee_det(regno=''):
        if(regno==''):
            regno=request.form['Registration_Number']
        sql="select course,branch,frname,lname from student where reg_no=%s;"
        val=(regno,)
        cur.execute(sql,val)
        cb=cur.fetchall()
        print(cb)
        sql="select fess from coursereg where course_name=%s and branch=%s;"
        val=(cb[0][0],cb[0][1])
        cur.execute(sql,val)
        cf=cur.fetchall()
        print("pp",cf)
        data=[cb[0][0],cb[0][1],cb[0][2]+cb[0][3],regno]
        print(data)
        sql="select * from fees where regno=%s;"
        val=(regno,)
        cur.execute(sql,val)
        fees=cur.fetchall()
        
        t=[]
        h=[]
        a=[]
        for i in fees:
            if(i[3]=='t'):
                t.append(int(i[2]))
            elif(i[3]=='h'):
                h.append(int(i[2]))
            elif(i[3]=='a'):
                a.append(int(i[2]))
        print(sum(t),sum(h),sum(a))
        sa=sum(a)
        ha=sum(h)
        ta=sum(t)
        icf=int(cf[0][0])
        print(icf)
        return render_template("accounts/viewfees.html",cf=icf,a=sa,h=ha,t=ta,dataa=data)
    @app.route("/TAccounts")
    def tacc():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/tacc")
    @app.route("/tacc")
    def show_tAcc():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template("accounts/feet.html")
    @app.route("/HAccounts")
    def hacc():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/hacc")
    @app.route("/hacc")
    def show_hcc():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template("accounts/feeh.html")
    @app.route("/AAccounts")
    def aacc():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/aacc")
    @app.route("/aacc")
    def show_aAcc():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template("accounts/feea.html")
    
class adminplacement:
    @app.route("/Addcompany")
    def Addcompany():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/Addcompanyicon")
    @app.route("/Addcompanyicon")
    def show_Addcompanymain():
        st="maintemp/"+session['userrole']+"_main.html"
        sql="select branch from coursereg;"
        cur.execute(sql)
        es=cur.fetchall()
        lenes=len(es)
        return render_template("placement/addcompany.html",es=lenes,dataes=es)
    @app.route("/addnewcmp",methods=['POST'])
    def adcmp():
        cmpname=request.form['cmpname']
        role=request.form['role']
        abc=request.form.getlist('eligiblestream')
        ten=request.form['ten']
        twl=request.form['twl']
        diploma=request.form['diploma']
        description=request.form['description']
        stre=str(abc)
        sql="insert into company(name,es,ten,tw,diploma,descc,role) values(%s,%s,%s,%s,%s,%s,%s);"
        val=(cmpname,stre,ten,twl,diploma,description,role)
        cur.execute(sql,val)
        conn.commit()
        return render_template("tome.html",text="Company Added Successfully",id=1)

    @app.route("/adddrive")
    def adddrive():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/adddriveicon")
    @app.route("/adddriveicon")
    def show_adddrivemain():
        st="maintemp/"+session['userrole']+"_main.html"
        sql="select name from company;"
        cur.execute(sql)
        es=cur.fetchall()
        lenes=len(es)
        return render_template("placement/adddrive.html",es=lenes,dataes=es)
    @app.route("/addnewdrive",methods=['POST'])
    def addrivecmp():
        abc=request.form['eligiblestream']
        sql="select id from company where name=%s;"
        val=(abc,)
        cur.execute(sql,val)
        a=cur.fetchall()
        print(a[0][0])
        date=request.form['date']
        time=request.form['time']
        venue=request.form['venue']
        strr=a[0][0]
        sql="insert into companydrive(cid,eventdate,eventtime,venue) values(%s,%s,%s,%s);"
        val=(strr,date,time,venue)
        cur.execute(sql,val)
        conn.commit()
        print(a[0][0],date,time,venue)
        return render_template("tome.html",text="Drive Added Successfully",id=1)

    @app.route("/eligible_stu")
    def eligible():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/eligibleicon")
    @app.route("/eligibleicon")
    def eligiblemain():
        st="maintemp/"+session['userrole']+"_main.html"
        sql="select name from company;"
        cur.execute(sql)
        es=cur.fetchall()
        lenes=len(es)
        return render_template("placement/eligible.html",es=lenes,dataes=es)
    
    @app.route("/listecmp",methods=['POST'])
    def eligiblelistmain():
        st="maintemp/"+session['userrole']+"_main.html"
        eligiblestream=request.form['eligiblestream']
        sql="select * from company where name=%s;"
        val=(eligiblestream,)
        cur.execute(sql,val)
        a=cur.fetchall()
        c=list(a[0][2])
        b="select reg_no,frname,lname,gender,course,branch from student "
        d=[]
        for i in c:
            if(i.isalpha()):
                d.append(i)
        for i in range(len(d)):
            
            if(i==0 and len(d)==1):
                b=b+"where branch='"+d[i]+"' "
            elif(i==0):
                b=b+"where branch='"+d[i]+"' or "
            elif(i!=len(d)-1):
                b=b+"branch='"+d[i]+"' or "
            else:
                b=b+"branch='"+d[i]+"' "
        
        b=b+"AND ten >= "+str(a[0][3])+" AND tw >= "+str(a[0][4])+" AND dip >= "+str(a[0][5])+" order by branch;"
        b=str(b)
        cur.execute(b)
        stu=cur.fetchall()
        print(b)
        lstu=len(stu)

        return render_template("placement/list.html",stud=stu,lstud=lstu)
class att:
    @app.route("/Attendance")
    def att():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/course_attt")
    @app.route("/course_attt")
    def add_course_attt():

        sql="select course_name,branch,sem from coursereg;"
        cur.execute(sql)
        cr=cur.fetchall()
        print(cr)
        return render_template("academics/attselcourse.html",course=cr,lenc=len(cr))
    @app.route("/Yr_attt",methods=["POST"])
    def add_yr_attt():
        course=request.form.to_dict('bg')
        course_br=(course['bg'])
        course=course_br.split("'")
        print(course[1])
        print(course[3])
        print(course[5])
        return render_template("academics/attselsem.html",sem=int(course[5]),course=course[1],branch=course[3])
   
    @app.route("/Generate_attt",methods=["POST"])
    def add_attt():
        cours=request.form['course']
        branc=request.form['branch']
        semi=request.form['sem']
        sem=int(semi)
        tem=0
        if(sem==1 or sem==2):
            tem=(datetime.date.today().year)
        if(sem==3 or sem==4):
            tem=(datetime.date.today().year-1)
        if(sem==5 or sem==6):
            tem=(datetime.date.today().year-2)
        if(sem==7 or sem==8):
            tem=(datetime.date.today().year-3)
        if(sem==9 or sem==10):
            tem=(datetime.date.today().year-4)
        sql="select frname,lname,reg_no from student where jy=%s and course=%s and branch=%s;"
        val=(tem,cours,branc)
        cur.execute(sql,val)
        cb=cur.fetchall()
        print(cb)
        return render_template("academics/atttendance.html",sem=sem,data=cb,lend=len(cb))
    
    @app.route("/addpa",methods=['POST'] )
    def pa():
        date=request.form['date']
        time=request.form['time']
        lenno=request.form['lenno']
        sem=request.form['sem']
        abbs=[]
        rns=[]
        for i in range(0,int(lenno)):
            semi="att["+str(i)+"]"
            att=request.form[semi]
            semio="rno["+str(i)+"]"
            rno=request.form[semio]
            sql="insert into ap(regno,ap,sem,date,time) value(%s,%s,%s,%s,%s)"
            val=(att,rno,sem,date,time)
            cur.execute(sql,val)
            if(att=='a'):
                abbs.append(att)
                rns.append(rno)
        conn.commit()
        return render_template('academics/viewatt.html',abbs=abbs,rns=rns,lena=len(abbs))

    @app.route("/ATt_set")
    def attset():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/set_attt")
    @app.route("/set_attt")
    def add_atttser():
        b=['','08:00-09:00','09:00-10:00','10:00-11:00','11:00-12:00','12:00-13:00','13:00-14:00','14:00-15:00']
        a=['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday']
        return render_template("academics/ex.html",day=a,time=b)

class tt:
    @app.route("/Generate_tt")
    def tt():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/tt_s1")
    @app.route("/tt_s1")
    def tt_s1():
        st="maintemp/"+session['userrole']+"_main.html"
        sql="select distinct * from coursereg;"
        cur.execute(sql)
        value=cur.fetchall()
        return render_template("academics/timecourse.html",lena=len(value),value=value)
    @app.route("/tt_s2",methods=['POST'])
    def tt_s2():
        sem=request.form['bg']
        aa=(sem.split('+'))
        sql="select sem from coursereg where course_name=%s and branch=%s;"
        val=(aa[0],aa[-1])
        cur.execute(sql,val)
        valuer=cur.fetchall()
        print(valuer)
        return render_template("academics/timesem.html",value=int(valuer[0][0]),course=aa[0],branch=aa[-1])

    @app.route("/Generate_tttt",methods=['POST'])
    def add_ttt():
        sem=request.form['bg']
        course=request.form['course']
        branch=request.form['branch']
        ac=[]
        ac.append(sem)
        ac.append(course)
        ac.append(branch)
        b=['','08:00-09:00','09:00-10:00','10:00-11:00','11:00-12:00','12:00-13:00','13:00-14:00','14:00-15:00']
        a=['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday']
        return render_template("academics/timetable.html",day=a,time=b,ac=ac)


@app.route("/issuebook")
def issuebook():
    st="maintemp/"+session['userrole']+"_main.html"
    return render_template(st,temp="/vbok")
@app.route("/vbok")
def vbok():
    sql1="select publication from book_publication;"
    cur.execute(sql1)
    datap=cur.fetchall()
    lendataA=len(datap)
    sql1="select author from book_author;"
    cur.execute(sql1)
    dataa=cur.fetchall()
    lendataB=len(dataa)
    sql1="select bname,code from library;"
    cur.execute(sql1)
    bname=cur.fetchall()
    lenBname=len(bname)
    return render_template('library/issueviewbook.html',datapp=datap,dataaa=dataa,bdata=bname,lenBnamep=lenBname,lendataAp=lendataA,lendataBa=lendataB)

@app.route("/searchingbook",methods=['POST'])
def searching():
    bname=request.form['bname']
    bauthor=request.form['bauthor']
    bpublisher=request.form['bpublisher']
    bcode=request.form['bcode']
    print(len(bname),len(bauthor),len(bpublisher),len(bcode))
    c="select * from library "
    b="where "
    a=""
    e=0
    if(len(bname)!=0):
        e=1
        a=a+"bname = '"+bname+"' "
    if(len(bauthor)!=0):
        e=1
        a=a+"bauthor = '"+bauthor+"' "
    if(len(bpublisher)!=0):
        e=1
        a=a+"bpublisher = '"+bpublisher+"' "
    if(len(bcode)!=0):
        e=1
        a=a+"code = '"+bcode+"' "

    dd=""
    if(e==1):
        dd=(c+b+a+";")
    else:
        dd=(c+";")
    cur.execute(dd)
    data=cur.fetchall()
    print(data)
    return render_template("library/vvshowbook.html",t=len(data),c=data)

@app.route("/issue/<idd>",methods=['GET'])
def isb(idd):
    return render_template("result/vrmissue.html",idd=idd)
@app.route("/badd",methods=['POST'])
def badd():
    idd=request.form['idd']
    rno=request.form['rno']
    sql="select * from library where id=%s;"
    val=(idd,)
    cur.execute(sql,val)
    aa=cur.fetchall()
    if(int(aa[0][5])==int(aa[0][6])):
        return"Out Of Stock"
    sql="select * from issued_book where issue_book_code=%s;"
    val=(aa[0][-1],)
    cur.execute(sql,val)
    ab=cur.fetchall()
    noo=""
    aun=[]
    if(len(ab)==0):
        noo=str(aa[0][-1])+str(1)
    else:
        for i in range(len(ab)):
            aun.append(ab[i][1])
    aaa=0
    while(True):
        aaa=aaa+1
        if(str(aa[0][-1])+str(aaa) not in aun):
            noo=str(aa[0][-1])+str(aaa)
            break
    print(noo)
    dtr=aa[0][-2]+1
    sql="update library SET issue=%s where id=%s;"
    val=(dtr,idd)
    cur.execute(sql,val)
    issudate=datetime.date.today()
    return_date = issudate + datetime.timedelta(15)
    sql="insert into issued_book(issue_book_no,issue_book_code,regno,issue_date,return_date,book_id) values(%s,%s,%s,%s,%s,%s);"
    val=(noo,aa[0][-1],rno,issudate,return_date,aa[0][0])
    cur.execute(sql,val)
    conn.commit()
    return render_template("tome.html",text="Book Issued Successfully",id=1)

@app.route("/stuissuebook")
def stuissuebook():
    st="maintemp/"+session['userrole']+"_main.html"
    return render_template(st,temp="/sttbok")
@app.route("/sttbok")
def sttbok():
    sql="select * from issued_book where regno=%s;"
    val=(session['userid'],)
    cur.execute(sql,val)
    fsrs=cur.fetchall()
    return render_template("library/stushow.html",t=len(fsrs),c=fsrs)

@app.route("/removebook")
def removebook():
    st="maintemp/"+session['userrole']+"_main.html"
    return render_template(st,temp="/rmbok")
@app.route("/rmbok")
def rmbok():
    return render_template("result/vrmrem.html")
@app.route("/rbadd",methods=['POST'])
def rbadd():
    rno=request.form['rno']
    sql="select * from issued_book where regno=%s;"
    val=(rno,)
    cur.execute(sql,val)
    aa=cur.fetchall()
    return render_template("library/vvtshowbook.html",t=len(aa),c=aa,rno=rno)


@app.route("/rmissue/<rno>/<idd>/<bno>",methods=['GET'])
def rsb(rno,idd,bno):
    print(idd)
    sql="select * from library where id=%s;"
    val=(idd,)
    cur.execute(sql,val)
    aa=cur.fetchall()
    print(aa)
    
    dtr=aa[0][-2]-1
    sql="update library SET issue=%s where id=%s;"
    val=(dtr,idd)
    cur.execute(sql,val)
    sql="delete from issued_book where issue_book_no=%s;"
    val=(bno,)
    cur.execute(sql,val)
    conn.commit()
    return render_template("result/vrmissue.html",idd=idd)


@app.route("/rsearchingbook",methods=['POST'])
def rsearching():
    bname=request.form['bname']
    bauthor=request.form['bauthor']
    bpublisher=request.form['bpublisher']
    bcode=request.form['bcode']
    print(len(bname),len(bauthor),len(bpublisher),len(bcode))
    c="select * from library "
    b="where "
    a=""
    e=0
    if(len(bname)!=0):
        e=1
        a=a+"bname = '"+bname+"' "
    if(len(bauthor)!=0):
        e=1
        a=a+"bauthor = '"+bauthor+"' "
    if(len(bpublisher)!=0):
        e=1
        a=a+"bpublisher = '"+bpublisher+"' "
    if(len(bcode)!=0):
        e=1
        a=a+"code = '"+bcode+"' "

    dd=""
    if(e==1):
        dd=(c+b+a+";")
    else:
        dd=(c+";")
    cur.execute(dd)
    data=cur.fetchall()
    print(data)
    return render_template("library/rrshowbook.html",t=len(data),c=data)

class rms:
    @app.route("/AResult")
    def rsm():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/rsm")
    @app.route("/rsm")
    def show_rsm(a=''):
        b=''
        if(a!=''):
            b=True
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template("result/rm.html",ab=a,b=b)
    @app.route("/rms",methods=['POST'])
    def show_rms():
        regno=request.form['Registration_Number']
        sql="select branch,course,frname,lname from student where reg_no=%s;"
        val=(regno,)
        cur.execute(sql,val)
        cb=cur.fetchall()
        print(cb)
        
        sql="select sem,id from coursereg where branch=%s and course_name=%s;"
        val=(cb[0][0],cb[0][1])
        cur.execute(sql,val)
        cf=cur.fetchall()
        print(cf)
        sem=int(cf[0][0])
        id=int(cf[0][1])
        return render_template("result/rms.html",a=sem,r=regno,idd=id)
    
    @app.route("/rmrs",methods=['POST'])
    def show_rmrs():
        
        sem=request.form['Registration_Number']
        regno=request.form['regno']
        idd=request.form['id']
        
        sql="select * from codereg where crid=%s and sem=%s;"
        val=(idd,sem)
        cur.execute(sql,val)
        cb=cur.fetchall()
        lencbb=(len(cb))
        print(cb)
        return render_template("result/rmrs.html",a=sem,r=regno,lencb=lencbb,sb=cb)
    @app.route("/addrmrs",methods=['POST'])
    def addrmrs():
        regno=request.form['reggno']
        sem=request.form['sem']
        cbkilen=request.form['cbkilen']
        mode=request.form['mode']
        for i in range(int(cbkilen)):
            summ="sb"+str(i)
            summm="sb"+str(i)+"n"
            a=request.form[summ]
            c=request.form[summm]
            print(a,c)
            sql="insert into result(regno,sem,subject,mode,marks) values(%s,%s,%s,%s,%s);"
            val=(regno,sem,a,mode,c)
            cur.execute(sql,val)
            conn.commit()
        k="Result Added Successfully"
        return render_template("tome.html",text=k,id=1)
class vrms:
    @app.route("/VResult")
    def vrsm():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/vrsm")
    @app.route("/vrsm")
    def vshow_rsm(a=''):
        b=''
        if(a!=''):
            b=True
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template("result/vrm.html",ab=a,b=b)
    @app.route("/vrms",methods=['POST'])
    def vshow_rms():
        regno=request.form['Registration_Number']
        sql="select course,branch,frname,lname from student where reg_no=%s;"
        val=(regno,)
        cur.execute(sql,val)
        cb=cur.fetchall()
        print(cb)
        
        sql="select sem,id from coursereg where course_name=%s and branch=%s;"
        val=(cb[0][0],cb[0][1])
        cur.execute(sql,val)
        cf=cur.fetchall()
        print(cf)
        sem=int(cf[0][0])
        id=int(cf[0][1])
        return render_template("result/vrms.html",a=sem,r=regno,idd=id)

    
    @app.route("/vrmrs",methods=['POST'])
    def vshow_rmrs():
        
        sem=request.form['Registration_Number']
        regno=request.form['regno']
        idd=request.form['id']
        
        sql="select * from result where regno=%s and sem=%s;"
        val=(regno,sem)
        cur.execute(sql,val)
        cb=cur.fetchall()
        lencbb=(len(cb))
        print(cb)
        b=[]
        c=[]
        for i in cb:
            if i[3] in b:
                d=b.index(i[3])
                e=c[d]
                c.pop(d)
                c.insert(d,e+int(i[5]))
                print(e)
            else:
                b.append(i[3])
                c.append(int(i[5]))

        print(b,c)
        gg=len(b)
        return render_template("result/vrmrs.html",a=sem,r=regno,lenb=gg,b=b,c=c)
class Student:
    @app.route("/add_student")  
    def addStudent():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/stu")

    @app.route("/stu")
    def add_stu():
        sql="select distinct branch,course_name from coursereg;"
        cur.execute(sql)
        cb=cur.fetchall()
        print(cb)
        conn.commit()
        return render_template('adduser/addstu_form.html',cblen=len(cb),cbb=cb)

    
class Placement:
    @app.route("/add_placement")  
    def addPlacement():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/pla")

    @app.route("/pla")
    def add_pla():
        return render_template('adduser/addpla_form.html')

class Faculty:
    @app.route("/add_faculty")  
    def addFaculty():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/fac")

    @app.route("/fac")
    def add_fac():
        return render_template('adduser/addfac_form.html')
        
class viewwuser:
    @app.route("/view_users")  
    def vu():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/vuu")

    @app.route("/vuu")
    def show_vu():
        sql="select * from users;"
        cur.execute(sql)
        cb=cur.fetchall()
        print(cb)
        return render_template('adduser/viewuser.html',cblen=len(cb),cbb=cb)
class Warden:
    @app.route("/add_warden")  
    def addWarden():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/war")
        
    @app.route("/war")
    def add_war():
        return render_template('adduser/addwar_form.html')
class libaaaa:
    @app.route("/add_library")  
    def addlibrary():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/libb")
        
    @app.route("/libb")
    def add_bil():
        return render_template('adduser/addlib_form.html')
class Accounts:
    @app.route("/add_accounts")  
    def addAccounts():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/acc")
        
    @app.route("/acc")
    def add_acc():
        return render_template('adduser/addacc_form.html')
class Transport:
    @app.route("/add_transport")    
    def addTransport():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/tra")
        
    @app.route("/tra")
    def add_tra():
        return render_template('adduser/addtra_form.html')
class Library:
    @app.route("/addbook")  
    def addLibrary():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/abook")
    @app.route("/abook")
    def addbook():
        sql1="select publication from book_publication;"
        cur.execute(sql1)
        datap=cur.fetchall()
        lendataA=len(datap)
        sql1="select author from book_author;"
        cur.execute(sql1)
        dataa=cur.fetchall()
        lendataB=len(dataa)
        return render_template('library/addbook.html',datapp=datap,dataaa=dataa,lendataAp=lendataA,lendataBa=lendataB)
    @app.route("/addbookk",methods=['POST'])
    def addbookk():
        bname=request.form['bname']
        bauthor=request.form['bauthor']
        bedition=request.form['bedition']
        bpublisher=request.form['bpublisher']
        stock=10
        issue=0
        sql1="select * from library;"
        cur.execute(sql1)
        data=cur.fetchall()
        code=0
        if(len(data)==0):
            code=1001
        else:
            code=(data[-1][-1]+1)
        sql="insert into library(bname,bauthor,bedition,bpublisher,book_stock,issue,code) values(%s,%s,%s,%s,%s,%s,%s);"
        val=(bname,bauthor,bedition,bpublisher,stock,issue,code)
        cur.execute(sql,val)
        conn.commit()
        return render_template("tome.html",text="Book Added Successfully",id=1)
    @app.route("/viewbook")  
    def viewLibrary():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/vbook")
    @app.route("/vbook")
    def viewbook():
        sql1="select publication from book_publication;"
        cur.execute(sql1)
        datap=cur.fetchall()
        lendataA=len(datap)
        sql1="select author from book_author;"
        cur.execute(sql1)
        dataa=cur.fetchall()
        lendataB=len(dataa)
        sql1="select bname,code from library;"
        cur.execute(sql1)
        bname=cur.fetchall()
        lenBname=len(bname)
        return render_template('library/viewbook.html',datapp=datap,dataaa=dataa,bdata=bname,lenBnamep=lenBname,lendataAp=lendataA,lendataBa=lendataB)
    
    @app.route("/searchbook",methods=['POST'])
    def searchbook():
        bname=request.form['bname']
        bauthor=request.form['bauthor']
        bpublisher=request.form['bpublisher']
        bcode=request.form['bcode']
        print(len(bname),len(bauthor),len(bpublisher),len(bcode))
        c="select * from library "
        b="where "
        a=""
        e=0
        if(len(bname)!=0):
            e=1
            a=a+"bname = '"+bname+"' "
        if(len(bauthor)!=0):
            e=1
            a=a+"bauthor = '"+bauthor+"' "
        if(len(bpublisher)!=0):
            e=1
            a=a+"bpublisher = '"+bpublisher+"' "
        if(len(bcode)!=0):
            e=1
            a=a+"code = '"+bcode+"' "

        dd=""
        if(e==1):
            dd=(c+b+a+";")
        else:
            dd=(c+";")
        cur.execute(dd)
        data=cur.fetchall()
        print(data)
        return render_template("library/showbook.html",t=len(data),c=data)
    @app.route("/addauthor")  
    def addauthor():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/aauthor")
    @app.route("/aauthor")
    def aauthor():
        sql1="select author from book_author;"
        cur.execute(sql1)
        data=cur.fetchall()
        print(data)
        lendataA=len(data)
        return render_template('library/bookauthor.html',dataa=data,lendata=lendataA)
    @app.route("/addingauthor",methods=['POST'])
    def addingauthor():
        bauthor=request.form['bauthor']
        sql="insert into book_author(author) values(%s);"
        val=(bauthor,)
        cur.execute(sql,val)
        conn.commit()
        return render_template("tome.html",text="Author Added Successfully",id=1)
    @app.route("/addpublisher")  
    def addpublisher():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/apublisher")
    @app.route("/apublisher")
    def apublisher():
        sql1="select publication from book_publication;"
        cur.execute(sql1)
        data=cur.fetchall()
        print(data)
        lendataA=len(data)
        return render_template('library/bookpublisher.html',dataa=data,lendata=lendataA)
    @app.route("/addingpublisher",methods=['POST'])
    def addingpublisher():
        bauthor=request.form['bpublisher']
        sql="insert into book_publication(publication) values(%s);"
        val=(bauthor,)
        cur.execute(sql,val)
        conn.commit()
        return render_template("tome.html",text="Publisher Added Successfully",id=1)
    @app.route("/stockviewbook")  
    def stockviewLibrary():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/stockvbook")
    @app.route("/stockvbook")
    def stockviewbook():
        return render_template('library/viewstock.html')
    @app.route("/stockaddbook")  
    def stockaddLibrary():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/stockabook")
    @app.route("/stockabook")
    def stockaddbook():
        return render_template('library/addstock.html')
class add_sturoles:
    @app.route("/addsturole",methods=['POST'])
    def add_stu_role():
        f_n=request.form['f_n']
        l_n=request.form['l_n']
        date=request.form['date']
        fatn=request.form['fatn']  
        fatnum=request.form['fatnum']
        focc=request.form['focc']
        mname=request.form['mname']
        mnum=request.form['mnum']
        mocc=request.form['mocc']
        address=request.form['address']
        city=request.form['city']
        State=request.form['state']
        phno=request.form['phno']
        customRadio=request.form['customRadio']
        aano=request.form['aano']
        course=request.form['course']
        branch=request.form['branch']
        bg=request.form['bg']
        ten=request.form['ten']
        tenb=request.form['tenb']
        tw=request.form['tw']
        twb=request.form['twb']
        diploma=request.form['diploma']
        du=request.form['du']
        Bachelor=request.form['Bachelor']
        bu=request.form['bu']
        role=request.form['role']
        year=request.form['year']
        sql="select id from users;"
        cur.execute(sql)
        id=cur.fetchall()
        userid=role+"@"+f_n+l_n+str(id[-1][0]+1)
        sql="insert into parents(stuis,Fathername,father_occ,mothername,motherocc,mobno) values(%s,%s,%s,%s,%s,%s);"
        val=(userid,fatn,focc,mname,mocc,fatnum)
        cur.execute(sql,val)
        conn.commit()
        name=f_n+l_n
        rolec="Parent"
        sql="insert into users(name,user_id,passwd,role)values(%s,%s,%s,%s);"
        val=(name,fatnum,date,rolec)
        cur.execute(sql,val)
        conn.commit()
        
        sql="select idparents from parents where stuis=%s;"
        val=(userid,)
        cur.execute(sql,val)
        pid=cur.fetchall()
        parid=(pid[-1][0])
        sql="insert into student(frname,lname,dob,p_id,address,city,state,mob_no,gender,aadhar,course,branch,bg,reg_no,ten,tenb,tw,twb,dip,dm,bd,buc,jy) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        val=(f_n,l_n,date,parid,address,city,State,phno,customRadio,aano,course,branch,bg,userid,ten,tenb,tw,twb,diploma,du,Bachelor,bu,year)
        cur.execute(sql,val)
        conn.commit()
        pas=role+"@123"
        sql="insert into users(name,user_id,passwd,role)values(%s,%s,%s,%s);"
        val=(name,userid,pas,role)
        cur.execute(sql,val)
        conn.commit()
        return render_template("tome.html",text="Student Role User Added Successfully",id=1)


@app.route('/admin_tt',methods=['POST'])
def admin_add_time():
   
   note00=request.form['note00']
   note01=request.form['note01']
   note02=request.form['note02']
   note03=request.form['note03']
   note04=request.form['note04']
   note05=request.form['note05']
   note06=request.form['note06']
   note07=request.form['note07']
   note10=request.form['note10']
   note11=request.form['note11']
   note12=request.form['note12']
   note13=request.form['note13']
   note14=request.form['note14']
   note15=request.form['note15']
   note16=request.form['note16']
   note17=request.form['note17']
   note20=request.form['note20']
   note21=request.form['note21']
   note22=request.form['note22']
   note23=request.form['note23']
   note24=request.form['note24']
   note25=request.form['note25']
   note26=request.form['note26']
   note27=request.form['note27']
   note30=request.form['note30']
   note31=request.form['note31']
   note32=request.form['note32']
   note33=request.form['note33']
   note34=request.form['note34']
   note35=request.form['note35']
   note36=request.form['note36']
   note37=request.form['note37']   
   note40=request.form['note40']
   note41=request.form['note41']
   note42=request.form['note42']
   note43=request.form['note43']
   note44=request.form['note44']
   note45=request.form['note45']
   note46=request.form['note46']
   note47=request.form['note47']
   note50=request.form['note50']
   note51=request.form['note51']
   note52=request.form['note52']
   note53=request.form['note53']
   note54=request.form['note54']
   note55=request.form['note55']
   note56=request.form['note56']
   note57=request.form['note57']
   subnote00=request.form['subnote00']
   subnote01=request.form['subnote01']
   subnote02=request.form['subnote02']
   subnote03=request.form['subnote03']
   subnote04=request.form['subnote04']
   subnote05=request.form['subnote05']
   subnote06=request.form['subnote06']
   subnote07=request.form['subnote07']
   subnote10=request.form['subnote10']
   subnote11=request.form['subnote11']
   subnote12=request.form['subnote12']
   subnote13=request.form['subnote13']
   subnote14=request.form['subnote14']
   subnote15=request.form['subnote15']
   subnote16=request.form['subnote16']
   subnote17=request.form['subnote17']
   subnote20=request.form['subnote10']
   subnote21=request.form['subnote11']
   subnote22=request.form['subnote12']
   subnote23=request.form['subnote13']
   subnote24=request.form['subnote14']
   subnote25=request.form['subnote15']
   subnote26=request.form['subnote16']
   subnote27=request.form['subnote17']
   subnote30=request.form['subnote10']
   subnote31=request.form['subnote11']
   subnote32=request.form['subnote12']
   subnote33=request.form['subnote13']
   subnote34=request.form['subnote14']
   subnote35=request.form['subnote15']
   subnote36=request.form['subnote16']
   subnote37=request.form['subnote17']
   subnote40=request.form['subnote10']
   subnote41=request.form['subnote11']
   subnote42=request.form['subnote12']
   subnote43=request.form['subnote13']
   subnote44=request.form['subnote14']
   subnote45=request.form['subnote15']
   subnote46=request.form['subnote16']
   subnote47=request.form['subnote17']
   subnote50=request.form['subnote10']
   subnote51=request.form['subnote11']
   subnote52=request.form['subnote12']
   subnote53=request.form['subnote13']
   subnote54=request.form['subnote14']
   subnote55=request.form['subnote15']
   subnote56=request.form['subnote16']
   subnote57=request.form['subnote17']
   subcode=request.form['sub_code']
   print(subcode)
   sql="delete from timetable where classcode=%s;"
   val=(subcode,)
   cur.execute(sql,val)
   sql="insert into timetable(sub_name,fac_name,ab,classcode) values(%s,%s,%s,%s);"
   val=[(note00,subnote00,'subnote00',subcode),
        (note01,subnote01,'subnote01',subcode),
        (note02,subnote02,'subnote02',subcode),
        (note03,subnote03,'subnote03',subcode),
        (note04,subnote04,'subnote04',subcode),
        (note05,subnote05,'subnote05',subcode),
        (note06,subnote06,'subnote06',subcode),
        (note07,subnote07,'subnote07',subcode),
        (note10,subnote10,'subnote10',subcode),
        (note11,subnote11,'subnote11',subcode),
        (note12,subnote12,'subnote12',subcode),
        (note13,subnote13,'subnote13',subcode),
        (note14,subnote14,'subnote14',subcode),
        (note15,subnote15,'subnote15',subcode),
        (note16,subnote16,'subnote16',subcode),
        (note17,subnote17,'subnote17',subcode),
        (note20,subnote20,'subnote20',subcode),
        (note21,subnote21,'subnote21',subcode),
        (note22,subnote22,'subnote22',subcode),
        (note23,subnote23,'subnote23',subcode),
        (note24,subnote24,'subnote24',subcode),
        (note25,subnote25,'subnote25',subcode),
        (note26,subnote26,'subnote26',subcode),
        (note27,subnote27,'subnote27',subcode),
        (note30,subnote30,'subnote30',subcode),
        (note31,subnote31,'subnote31',subcode),
        (note32,subnote32,'subnote32',subcode),
        (note33,subnote33,'subnote33',subcode),
        (note34,subnote34,'subnote34',subcode),
        (note35,subnote35,'subnote35',subcode),
        (note36,subnote36,'subnote36',subcode),
        (note37,subnote37,'subnote37',subcode),
        (note40,subnote40,'subnote40',subcode),
        (note41,subnote41,'subnote41',subcode),
        (note42,subnote42,'subnote42',subcode),
        (note43,subnote43,'subnote43',subcode),
        (note44,subnote44,'subnote44',subcode),
        (note45,subnote45,'subnote45',subcode),
        (note46,subnote46,'subnote46',subcode),
        (note47,subnote47,'subnote47',subcode),
        (note50,subnote50,'subnote50',subcode),
        (note51,subnote51,'subnote51',subcode),
        (note52,subnote52,'subnote52',subcode),
        (note53,subnote53,'subnote53',subcode),
        (note54,subnote54,'subnote54',subcode),
        (note55,subnote55,'subnote55',subcode),
        (note56,subnote56,'subnote56',subcode),
        (note57,subnote57,'subnote57',subcode)]
   cur.executemany(sql,val)
   ab.commit()
   return admin_add_timetable()
@app.route('/TIME_TABLE')
def admin_add_timetable():
   sql="select name from users where role='faculty'";
   cur.execute(sql)
   note=cur.fetchall()
   sql="select * from code;";
   cur.execute(sql)
   code=cur.fetchall()
   sql="select sub_name from subject;"
   cur.execute(sql)
   subnote=cur.fetchall()
   sql="select distinct classcode from timetable;"
   cur.execute(sql)
   classnote=cur.fetchall()
   return render_template('admin_timetable.html',b=['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday'],notee=note,classnotee=classnote,codee=code,lencode=len(code),lenclassnotee=len(classnote),lenote=len(note),subnotee=subnote,sublenote=len(subnote))

@app.route('/STU_TIME_TABLE')
def view_timetable():
   code=session.get('code')
   print(code)
   
   sql="select * from timetable where classcode=%s;"
   val=(code,)
   cur.execute(sql,val)
   tt=cur.fetchall()
   ff=tt[0][4]
   print(ff)
   c={}
   for i in tt:
      c[i[3]+"a"]=i[1]
      c[i[3]+"b"]=i[2]
   return render_template('stu_time.html',dataa=c,b=['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday'],kke=ff)

@app.route('/stu_tt',methods=['POST'])
def stu_data(code):   
   code=request.form['code']
   print(code)
   
   sql="select * from timetable where classcode=%s;"
   val=(code,)
   cur.execute(sql,val)
   tt=cur.fetchall()
   ff=tt[0][4]
   print(ff)
   b={}
   for i in tt:
      b[i[3]+"a"]=i[1]
      b[i[3]+"b"]=i[2]
   return view_timetable(b,ff)
@app.route('/FAC_TIME_TABLE')
def fac_view_timetable(data={},kk=""):
   sql="select distinct sub_name from timetable;"
   cur.execute(sql)
   classcode=cur.fetchall()
   print(classcode)
   print(data,kk)
   return render_template('fac_time.html',dataa=data,b=['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday'],classcodee=classcode,lenclasscode=len(classcode),kke=kk)

@app.route('/stu_fac',methods=['POST'])
def fac_data():   
   fac=request.form['fac']
   
   sql="select * from timetable where sub_name=%s;"
   val=(fac,)
   cur.execute(sql,val)
   tt=cur.fetchall()
   kk=fac
   print(tt)
   b={}
   for i in tt:
      b[i[3]+"a"]=i[1]
      b[i[3]+"b"]=i[2]
      b[i[3]+"c"]=i[4]
   print(b)
   return fac_view_timetable(b,kk)

@app.route('/HELLO',methods=['POST'])
def adview_timetable():
   codr=request.form['ame']
   return "HELLo"

class add_roles:
    @app.route("/addnewrole",methods=['POST'])
    def add_role():
        f_n=request.form['f_n']
        l_n=request.form['l_n']
        date=request.form['date']
        Qualification=request.form['Qualification']
        salary=request.form['salary']
        customRadio=request.form['customRadio']
        aano=request.form['aano']
        bg=request.form['bg']
        role=request.form['role']
        sql="select id from users;"
        cur.execute(sql)
        id=cur.fetchall()
        sql="insert into role(fname,lname,dob,qualification,salary,gender,aano,bg,role)values(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        val=(f_n,l_n,date,Qualification,salary,customRadio,aano,bg,role)
        cur.execute(sql,val)
        userid=role+"@"+f_n+l_n+str(id[-1][0]+1)
        password=role+"@123"
        name=f_n+l_n
        sql="insert into users(name,user_id,passwd,role)values(%s,%s,%s,%s);"
        val=(name,userid,password,role)
        cur.execute(sql,val)
        conn.commit()
        if(role=="Warden"):
            return render_template("tome.html",text="Warden Role User Added Successfully",id=1)
        elif(role=="Placement"):
            return render_template("tome.html",text="Placement Role User Added Successfully",id=1)
        elif(role=="Accounts"):
            return render_template("tome.html",text="Accounts Role User Added Successfully",id=1)
        elif(role=="Transport"):
            return render_template("tome.html",text="Transport Role User Added Successfully",id=1)
        elif(role=="Library"):
            return render_template("tome.html",text="Library Role User Added Successfully",id=1)
        elif(role=="Faculty"):
            return render_template("tome.html",text="Faculty Role User Added Successfully",id=1)

class view_notice:
    @app.route("/notice")
    def view_notice():
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template(st,temp="/shownotice")
    @app.route("/shownotice")
    def show_notice():
        sql="select id,date,name,details,category,file from notice order by id desc;"
        cur.execute(sql)
        data=cur.fetchall()
        print(data)
        st="maintemp/"+session['userrole']+"_main.html"
        return render_template("notice/viewnotice.html",t=len(data),c=data)

@app.route("/view_mess")
def view_mess():
    st="maintemp/"+session['userrole']+"_main.html"
    return render_template(st,temp="/viewmess")
@app.route("/viewmess")
def viewmess():
    sql="select * from mess;"
    cur.execute(sql)
    data=cur.fetchall()
    print(data)
    b=data[0][1].split(',')
    l=data[0][2].split(',')
    d=data[0][3].split(',')
    a=0
    if(len(b)>len(l) and len(b)>len(d)):
        a=len(b)
    elif(len(l)>len(d) and len(l)>len(b)):
        a=len(l)
    elif(len(d)>len(l) and len(d)>len(b)):
        a=len(d)
    elif(len(l)==len(d) and len(l)==len(b)):
        a=len(l)
    return render_template("notice/showmess.html",t=a,b=b,l=l,d=d)

@app.route("/viewatt")
def viewatt():
    st="maintemp/"+session['userrole']+"_main.html"
    return render_template(st,temp="/view_att")
@app.route("/view_att")
def view_att():
    sql="select * from ap where ap=%s;"
    val=(session['userid'],)
    cur.execute(sql,val)
    data=cur.fetchall()
    print(data)
    a=0
    return render_template("notice/showviewatt.html",t=len(data),c=data)

class addcourse:

    @app.route("/courseadd")
    def course():
        dst="maintemp/"+session['userrole']+"_main.html"
        return render_template(dst,temp="/coursevie")
        
    @app.route("/coursevie")
    def coursevie():
        return render_template('course/course.html')

    @app.route("/addcoursesem",methods=['POST'])
    def addcoursesem():
        coursename=request.form['cname']
        year=request.form['year']
        sem=request.form['sem']
        branchname=request.form['branchname']
        yff=request.form['yf']
        print(coursename,year,sem,branchname)
        sql="insert into coursereg(course_name,year,sem,branch,fess)values(%s,%s,%s,%s,%s);"
        val=(coursename,year,sem,branchname,yff)
        cur.execute(sql,val)
        conn.commit()
        sql="select id from coursereg where course_name=%s and year=%s and sem=%s and branch=%s and fess=%s;"
        val=(coursename,year,sem,branchname,yff)
        cur.execute(sql,val)
        ages=(cur.fetchall()[-1][0])
        dst="maintemp/"+session['userrole']+"_main.html"
        return render_template('course/coursesem.html',crid=ages,semm=int(sem))
    @app.route("/addnosem",methods=['POST'])
    def addcoursenosem():
        g=[]
        sem=request.form['sem']
        crid=request.form['cridd']
        seem=int(sem)
        for i in range(1,seem+1):
            semi="sem"+str(i)
            semi=request.form[semi]
            g.append(int(semi))
        print(crid)
        return render_template('course/courseseem.html',tg=g,slen=g,semm=seem,cridd=crid)
    @app.route("/addsubsem",methods=['POST'])
    def addcoursesubsem():
        tt=request.form['tt']
        crid=request.form['crid']
        print(crid)
        a=list(tt)
        print(a)
        b=[]
        for i in a:
            if(ord(i)>=48 and ord(i)<=57):
                b.append(i)
        for i in range(len(b)):
            for j in range(int(b[i])):
                semm="sem"+str(i+1)
                summ="sem"+str(i+1)+"sub"+str(j+1)
                a=request.form[semm]
                c=request.form[summ]
                sql="insert into codereg(crid,subject,sem) values(%s,%s,%s);"
                val=(crid,c,a)
                cur.execute(sql,val)
                conn.commit()

        return render_template("tome.html",text="Course Added Successfully",id=1)
    
@app.route("/home")
def home():
    dst="maintemp/"+session['userrole']+"_main.html"
    return render_template(dst,temp="/ho")
        
@app.route("/ho")
def hoo():
    return ""

class main():
    @app.route("/")
    def index():
        if('userrole' not in session):
            return render_template('welcomescreen.html')
        else:
            return home()
    @app.route("/login")
    def login():
        return render_template('login.html',error="All Fields are Manodatry")
    @app.route('/addlogin',methods=['POST'])
    def hello_world():
        if(request.method=='POST'):
            a=request.form['userid']
            b=request.form['passcode']
            sql="select role,name,user_id from users where user_id=%s and passwd=%s;"
            val=a,b
            cur.execute(sql,val)
            gg=cur.fetchall()
            print(len(gg))
            if(len(gg)==1):
                print(gg)
                session['userid']=gg[0][2]
                session['user']=gg[0][1]
                session['userrole']=gg[0][0]
                print(session)
                st="maintemp/"+gg[0][0]+"_main.html"
                print(st)
                return render_template(st)
                    
            else:
                erro="The User Id and Password is Incorrect"
                return render_template('login.html',error=erro)
            
        return "Hello"

app.run(debug=True,host="0.0.0.0")