from tkinter import *
from tkinter.messagebox import *
from PIL import ImageTk
from tkinter.scrolledtext import *
from sqlite3 import *
import requests
import matplotlib.pyplot as plt
import bs4


root= Tk()
root.title("Login")


root.geometry("600x600+400+200")
root.resizable(0,0)
root.config()
#root.config(bg='images/745989.png')
bg_icon=PhotoImage(file="745989.png")
bg_lbl=Label(root,image=bg_icon)
bg_lbl.pack(fill=BOTH, expand=TRUE)


def f1():
	if userent.get()=="" or passent.get()=="":
        	showwarning("Error","All fields are required")
	
	elif userent.get()=="admin" and passent.get()=="admin":

		
	#--------------main menu---------------#

		
		tf=Toplevel(root)
		root.withdraw()
		tf.deiconify
		tf.title("S.M.S")
		tf.config(bg='PaleGreen3')
		tf.geometry("600x700+425+100")
		tf.resizable(0,0)
		tf.config()
		

		def add():
			tf.withdraw()
			add_st.deiconify()

		def back():
			add_st.withdraw()
			tf.deiconify()


		#---------db view record----------#
			

		def view():
			tf.withdraw()
			view_st.deiconify()
			view_st.config(bg='khaki')
			view_st.resizable(0,0)
			view_st_data.delete(1.0,END)
			con= None
	
			try:
				con= connect("girish.db")
				sql= "select * from student"	
				cursor = con.cursor()
				cursor.execute(sql)
				data= cursor.fetchall()
				info=""	
				for d in data:
					info= info + " rno : " + str(d[0])+ "  name : "  +  str(d[1]) + "  marks : " + (str(d[2]) + "\n")
				view_st_data.insert(INSERT,info)
			except Exception as e:
				showerror("issue",e)
			finally:
				if con is not None:
					con.close()

		def chart():
			con= None
	
			try:
				con= connect("girish.db")
				sql= "select name,marks from student"	
				cursor = con.cursor()
				cursor.execute(sql)
				data= cursor.fetchall()
				
				names=[]
				marks=[]
				for d in data:
					
					names.append(d[0])
					marks.append(d[1])

				plt.bar(names,marks,color='r')
				plt.xlabel("Names")
				plt.ylabel("Marks")
				plt.title("Batch Information !")
				plt.show()
			
	

			except Exception as e:
				showerror("issue",e)
			finally:
				if con is not None:
					con.close()

				



		
		def viewback():
			view_st.withdraw()
			tf.deiconify()

		def update():
			tf.withdraw()
			update_st.deiconify()
		
		def updateback():
			update_st.withdraw()
			tf.deiconify()
		
		
			


   
			#----------------db update record-----------#	

		def save():
			con= None
			try:
				con= connect("girish.db")
				sql= "update student set name ='%s',marks='%d' where rno= '%d' "
				cursor= con.cursor()
				
	
				rno=int(update_st_entrno.get())
				name=update_st_entname.get()
				marks=int(update_st_entmarks.get())
				if rno < 1:
					showerror("Failed","Rno should not be in negative")			

				elif name == "":
					showerror("Failed","Name should not be empty")
					
				

				elif (len(name)) <2:
					showerror("Failed","Name should contain more than 2 letters")

				elif marks == 0 :
					
					showerror("Failed","Marks should not be empty")
				

				elif (marks < 0 or marks > 100):
					showerror("Failed","Marks should be in range of 0 to 100")

				else:
	


			
					cursor.execute(sql % (name,marks,rno))
					if cursor.rowcount == 1:
			
						con.commit()
						showinfo("Success","record updated")
					else:
						showerror("issue","record does not exist")
	
			except Exception as e:

				if update_st_entrno.get()=="" and update_st_entmarks.get()=="" and update_st_entname.get()=="":
					showerror("Failure","All the Fields are required")

				elif update_st_entrno.get() =="":
					showerror("Failure","rno should not be empty")
					#con.rollback()

				elif rno < 1:
					showerror("Failed","Rno should not be in negative")


				elif update_st_entname.get()=="":
					showerror("Failed","Name should not be empty")

				elif (len(name)) <2:
					showerror("Failed","Name should contain more than 2 letters")



				elif update_st_entmarks.get()=="":
					showerror("Failure","marks should not be empty")
					
				

			
				else:
			
					showerror("Failure",e)		
					con.rollback()

			finally:
				if con is not None:
					con.close()
				update_st_entrno.delete(0,END)
				update_st_entname.delete(0,END)
				update_st_entmarks.delete(0,END)
				update_st_entrno.focus()
				update_st_entname.focus()
				update_st_entmarks.focus()

				
					

		def delete():
			tf.withdraw()
			delete_st.deiconify()

		#------------db delete record-----------#

		def f6():
			con= None
			try:
				con= connect("girish.db")
				sql= " delete from student where rno= '%d' "
				cursor = con.cursor()
				rno=int(delete_st_entrno.get())
				cursor.execute(sql % (rno))
				if cursor.rowcount == 1:
					con.commit()
					showinfo("Success","record deleted")
				else:
					showerror("Failed","record does not exist")
				
	
			except Exception as e:
				if delete_st_entrno.get()=="":
					showerror("Failed","Rno should not be empty")
				
				else:	
					showerror("issue",e)
					con.rollback()

			finally:
				if con is not None:
					con.close()
				delete_st_entrno.delete(0,END)		
				delete_st_entrno.focus()

		def deleteback():
			delete_st.withdraw()
			tf.deiconify()
		

		#---------------db add record-------------#


		def f5():
			con= None
			try:
				con= connect("girish.db")
				sql="insert into student values('%d', '%s','%d')"
				cursor= con.cursor()
				rno=int(add_st_entrno.get())
				name=add_st_entname.get()
				marks=int(add_st_entmarks.get())
				
				#if rno =="":
					#showerror("Failed","Rno should not be empty")


				if rno < 1:
					showerror("Failed","Rno should not be in negative")

				elif name == "":
					showerror("Failed","Name should not be empty")
					
				

				elif (len(name)) <2:
					showerror("Failed","Name should contain more than 2 letters")

				elif marks == 0 :
					
					showerror("Failed","Marks should not be empty")
				

				elif (marks < 0 or marks > 100):
					showerror("Failed","Marks should be in range of 0 to 100")

				else:
					
					cursor.execute(sql % (rno,name,marks))
					con.commit()	
					showinfo("Success","record added")
				
			
			

			except Exception as e:

				if add_st_entrno.get()=="" and add_st_entmarks.get()=="" and add_st_entname.get()=="":
					showerror("Failure","All the Fields are required")



				elif add_st_entrno.get() =="":
					showerror("Failure","rno should not be empty")
					#con.rollback()

				elif rno < 1:
					showerror("Failed","Rno should not be in negative")


				elif add_st_entname.get()=="":
					showerror("Failed","Name should not be empty")

				elif (len(name)) <2:
					showerror("Failed","Name should contain more than 2 letters")


				elif add_st_entmarks.get()=="":
					showerror("Failure","marks should not be empty")
					
				else:
			
					showerror("Failure",e)		
					con.rollback()


			
			finally:
				if con is not None:
					con.close()
				add_st_entrno.delete(0,END)
				add_st_entname.delete(0,END)
				add_st_entmarks.delete(0,END)
				add_st_entrno.focus()
				add_st_entname.focus()
				add_st_entmarks.focus()

		

		btnAdd= Button(tf,text="Add",width=10,font=("arial",18,"bold"),command=add)
		btnView= Button(tf,text="View",widt=10,font=("arial",18,"bold"),command=view)
		btnUpdate= Button(tf,text="Update",width=10,font=("arial",18,"bold"),command=update)
		btnDelete= Button(tf,text="Delete",widt=10,font=("arial",18,"bold"),command=delete)
		btnCharts= Button(tf,text="Charts",width=10,font=("arial",18,"bold"),command=chart)		
		#lbllocation= Label(tf,text="Location",font=("times new roman",18,"bold"))

				
		
		btnAdd.pack(pady=20)
		btnView.pack(pady=20)
		btnUpdate.pack(pady=20)
		btnDelete.pack(pady=20)
		btnCharts.pack(pady=20)
		#lbllocation.pack(padx=5,pady=10)
		
	
		frame1= Frame(tf,bd=4,relief=RIDGE,bg="light grey")
		frame1.place(x=0,y=540,width=600,height=150)
		frame1.config(bg='PaleGreen3')

		try:
			
			web_address= "https://ipinfo.io/"
			res= requests.get(web_address)
			data= res.json()
			loc= data['city']
			locationdisplay=Label(frame1,text=loc,font=("times new roman",16,"bold"))  
			locationdisplay.place(x=120,y=10)

		except Exception as e:
			showerror("Error",e)



		lbllocation= Label(frame1,text="Location:",font=("times new roman",16,"bold"))
		lbllocation.place(x=10,y=10)

		

	
		
		lbltemp= Label(frame1,text="Temp:",font=("times new roman",16,"bold"))
		lbltemp.place(x=400,y=10)



		try:
			city_name= 'Mumbai'
			a1= "http://api.openweathermap.org/data/2.5/weather?units=metric"
			a2= "&q=" + city_name
			a3= "&appid=c6e315d09197cec231495138183954bd"
			web_addr= a1 + a2 + a3
			resp= requests.get(web_addr)
			dataa= resp.json()
			m= dataa['main']
			t=m['temp']
			
			locationtemp=Label(frame1,text=t,font=("times new roman",14,"bold"))  
			locationtemp.place(x=480,y=10)
		except Exception as e:
			showerror("Error",e)
	

		lblqotd= Label(frame1,text="QOTD:",font=("times new roman",16,"bold"))
		lblqotd.place(x=10,y=60)
		

		try:
			web_addre= "https://www.brainyquote.com/quotes/benjamin_franklin_103731?src=t_motivational"
			respp= requests.get(web_addre)
			
			data1= bs4.BeautifulSoup(respp.text,"html.parser")

			#tag    #class
			info= data1.find('img',{"class":"bqPhotoFullDesktop"})					
			quote= info['alt']
			quotelabel=Label(frame1,text=quote,font=("times new roman",15,"bold"))  
			quotelabel.place(x=120,y=60)
		

		except Exception as e:
			showerror("Error",e)


		
		#---------------add student-----------------#


		add_st= Toplevel(tf)
		add_st.title("Add stu.")
		add_st.config(bg='cornflower blue')
		add_st.geometry("600x700+425+100")
		add_st.resizable(0,0)
		
		
		add_st_lblrno= Label(add_st,text="Enter Rno",font=("arial",18,"bold"))
		add_st_entrno= Entry(add_st,bd=5,font=("arial",18,"bold"))
		add_st_lblname= Label(add_st,text="Enter Name",font=("arial",18,"bold"))
		add_st_entname= Entry(add_st,bd=5,font=("arial",18,"bold"))
		add_st_lblmarks= Label(add_st,text="Enter Marks",font=("arial",18,"bold"))
		add_st_entmarks= Entry(add_st,bd=5,font=("arial",18,"bold"))

		add_st_btnsave= Button(add_st,text="save",font=("arial",18,"bold"),command=f5)
		add_st_btnback= Button(add_st,text="back",font=("arial",18,"bold"),command=back)

		add_st_lblrno.pack(pady=10)
		add_st_entrno.pack(pady=10)
		add_st_lblname.pack(pady=10)
		add_st_entname.pack(pady=10)
		add_st_lblmarks.pack(pady=10)
		add_st_entmarks.pack(pady=10)

		add_st_btnsave.pack(pady=10)
		add_st_btnback.pack(pady=10)
		
		add_st.withdraw()

		view_st= Toplevel(tf)
		view_st.title("View stu.")
		view_st.geometry("600x700+425+100")

		view_st_data= ScrolledText(view_st,width=38,height=12,font=("arial",18,"bold"))
		view_st_btnback= Button(view_st,text="Back",font=("arial",18,"bold"),command=viewback)
	
		view_st_data.pack(pady=10)
		view_st_btnback.pack(pady=10)
		view_st.withdraw()



		#------------------update--------------#


		update_st= Toplevel(tf)
		update_st.title("Update stu.")
		update_st.config(bg='peach puff')
		update_st.resizable(0,0)
		update_st.geometry("600x700+425+100")
		
		update_st_lblrno= Label(update_st,text="Enter Rno",font=("arial",18,"bold"))
		update_st_entrno= Entry(update_st,bd=5,font=("arial",18,"bold"))
		update_st_lblname= Label(update_st,text="Enter Name",font=("arial",18,"bold"))
		update_st_entname= Entry(update_st,bd=5,font=("arial",18,"bold"))
		update_st_lblmarks= Label(update_st,text="Enter Marks",font=("arial",18,"bold"))
		update_st_entmarks= Entry(update_st,bd=5,font=("arial",18,"bold"))

		update_st_btnsave= Button(update_st,text="save",font=("arial",18,"bold"),command=save)
		update_st_btnback= Button(update_st,text="back",font=("arial",18,"bold"),command=updateback)

		update_st_lblrno.pack(pady=10)
		update_st_entrno.pack(pady=10)
		update_st_lblname.pack(pady=10)
		update_st_entname.pack(pady=10)
		update_st_lblmarks.pack(pady=10)
		update_st_entmarks.pack(pady=10)

		update_st_btnsave.pack(pady=10)
		update_st_btnback.pack(pady=10)
		update_st.withdraw()



		#-------------------delete---------------#
	

		delete_st= Toplevel(tf)
		delete_st.title("Delete stu.")
		delete_st.config(bg='IndianRed1')
		delete_st.resizable(0,0)
		delete_st.geometry("500x600+425+200")
		
		delete_st_lblrno= Label(delete_st,text="Enter Rno",font=("arial",18,"bold"))
		delete_st_entrno= Entry(delete_st,bd=5,font=("arial",18,"bold"))
		
		delete_st_btnsave= Button(delete_st,text="save",font=("arial",18,"bold"),command=f6)
		delete_st_btnback= Button(delete_st,text="back",font=("arial",18,"bold"),command=deleteback)

		delete_st_lblrno.pack(pady=10)
		delete_st_entrno.pack(pady=10)

		delete_st_btnsave.pack(pady=10)
		delete_st_btnback.pack(pady=10)
		delete_st.withdraw()

		

	
	else:
		showerror("Error","Username or Password is incorrect")
		userent.delete(0,END)
		passent.delete(0,END)
		userent.focus()
		passent.focus()
		
		
	
	


loginlbl= Label(root,text="Login",font=("times new roman",35,"bold"))
userlbl= Label(root,text="Enter Username",font=("arial",18,"bold"))
userent= Entry(root,bd=5,font=("arial",18,"bold"))
passlbl= Label(root,text="Enter Password",font=("arial",18,"bold"))
passent= Entry(root,show="*",bd=5,font=("arial",18,"bold"))
btnsubmit= Button(root,text="Submit",font=("arial",18,"bold"),command=f1)

	

loginlbl.pack(pady=35,in_=bg_lbl)
userlbl.pack(pady=10,in_=bg_lbl)
userent.pack(pady=10,in_=bg_lbl)
passlbl.pack(pady=10,in_=bg_lbl)
passent.pack(pady=10,in_=bg_lbl)
btnsubmit.pack(pady=10,in_=bg_lbl)



root.mainloop()

