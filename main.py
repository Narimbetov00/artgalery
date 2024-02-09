import tkinter as tk
from data import add_datas_to_artists,add_data_to_arts,searchdb1,price,view_all_artists,view_all_arts
from tkinter import *

root=tk.Tk()
root.geometry("1200x700")
root.title("Example")
root.config(bg="#d6cdcb")

lbl= tk.Label(root,text="Entry new Details")
lbl.place(x=15,y=15)

#def 
def delate():
    ent_name.delete(0,tk.END)
    ent_addr.delete(0,tk.END)
    ent_town.delete(0,tk.END)
    ent_cont.delete(0,tk.END)
    ent_PC.delete(0,tk.END)   
def oshir():

    ent_ArtID.delete(0,tk.END)    
    ent_Title.delete(0,tk.END)
    ent_price.delete(0,tk.END)
def add_artist():
    name=ent_name.get()  
    adress = ent_addr.get()
    town = ent_town.get()
    country = ent_cont.get()
    post = ent_PC.get()
    add_datas_to_artists(name,adress,town,country,post)
def add_arts():
    artid = ent_ArtID.get()
    title = ent_Title.get()
    va = var.get()  
    price = ent_price.get()
    add_data_to_arts(artid,title,va,price)
def search():
    listbox.insert(tk.END,searchdb1(entSearch.get()))
def maxmin():
    min=int(entMIN.get())
    max=int(entMAX.get())
    s=price(min,max)
    listbox.insert(tk.END,str(s[0]))
def qoss():
    s =view_all_artists()
    listbox.insert(tk.END,str(s))
def qoss2():
    s = view_all_arts()
    listbox.insert(tk.END,str(s))
#lbl
lbl_name = tk.Label(root,text="Name:")
lbl_name.place(x=25,y=45)
lbl_addr = tk.Label(root,text="Address:")
lbl_addr.place(x=250,y=45)
lbl_town = tk.Label(root,text="Town:")
lbl_town.place(x=475,y=45)
lbl_cont = tk.Label(root,text="Country:")
lbl_cont.place(x=690,y=45)
lbl_PC = tk.Label(root,text="Past Code:")
lbl_PC.place(x=920,y=45)
lbl_ArtID = tk.Label(root,text="Artist ID:")
lbl_ArtID.place(x=20,y=125)
lbl_Title = tk.Label(root,text="Title:")
lbl_Title.place(x=260,y=125)
lbl_price = tk.Label(root,text="Price:")
lbl_price.place(x=700,y=125)
lbl_MINMAX = tk.Label(root,text="MIN:                   MAX:")
lbl_MINMAX.place(x=970,y=375)

#ent
ent_name = tk.Entry(root,font="arial",width=15)
ent_name.place(x=70,y=45)
ent_addr = tk.Entry(root,font="Arial",width=15)
ent_addr.place(x=300,y=45)
ent_town = tk.Entry(root,font="Arial",width=15)
ent_town.place(x=515,y=45)
ent_cont = tk.Entry(root,font="Arial",width=15)
ent_cont.place(x=745,y=45)
ent_PC = tk.Entry(root,font="Arial",width=15)
ent_PC.place(x=985,y=45)
ent_ArtID = tk.Entry(root,font="Arial",width=15)
ent_ArtID.place(x=70,y=120)
ent_Title = tk.Entry(root,font="Arial",width=19)
ent_Title.place(x=300,y=120)
ent_price = tk.Entry(root,font="Arial",width=15)
ent_price.place(x=747,y=120)
entSearch = tk.Entry(root,font="Arial",width=10)
entSearch.place(x=970,y=300)
entMIN = tk.Entry(root,font="Arial",width=7)
entMIN.place(x=970,y=400)
entMAX = tk.Entry(root,font="Arial",width=7)
entMAX.place(x=1070,y=400)
entSold = tk.Entry(root,font="Arial",width=7)
entSold.place(x=970,y=480)

#btn
btn_Art = tk.Button(root,text="Add Artist",width=20,bd=1,command=add_artist)
btn_Art.place(x=80,y=80)

btn_Clear = tk.Button(root,text="Clear Artist",width=20,bd=1,command=delate)
btn_Clear.place(x=315,y=80)

btn_Addprice = tk.Button(root,text="Add Piece",width=23,bd=1,command=add_arts)
btn_Addprice.place(x=70,y=160)

btn_CLSprice = tk.Button(root,text="Clear Piece",width=23,bd=1,command=oshir)
btn_CLSprice.place(x=300,y=160)

btn_COP = tk.Button(root,text="Clear output",width=25,bd=1)
btn_COP.place(x=970,y=200)
btn_VAA = tk.Button(root,text="View All Artists",width=25,bd=1,command=qoss)
btn_VAA.place(x=970,y=235)
btn_VA = tk.Button(root,text="View All Arts",width=25,bd=1,command=qoss2)
btn_VA.place(x=970,y=270)
btnSearch = tk.Button(root,text="Search",width=8,bd=1,command=search)
btnSearch.place(x=1090,y=300)

btnSearch2 = tk.Button(root,text="Search",width=8,bd=1)
btnSearch2.place(x=1090,y=335)
btnSearch3 = tk.Button(root,text="Search",width=25,bd=1,command=maxmin)
btnSearch3.place(x=970,y=440)
btnSold = tk.Button(root,text="Sold",width=11,bd=1)
btnSold.place(x=1070,y=480)
#listbox

listbox = tk.Listbox(root,width=148,height=25,bd=2)
listbox.place(x=25,y=200)

# spin = Spinbox(root,bd=0,width=10)
# spin.place(x=15,y=650)

options_list = ["oil","WaterColor","Neon"] 
var = tk.StringVar(root) 
var.set("saylan") 
omenu = tk.OptionMenu(root, var, *options_list) 
omenu.place(x=560,y=120) 

options_list1 = ["Oil","WaterColor","Neon"] 
value_inside1 = tk.StringVar(root) 
value_inside1.set("saylan") 
question_menu1 = tk.OptionMenu(root, value_inside1, *options_list1) 
question_menu1.place(x=970,y=335) 


if __name__=='__main__':

    root.mainloop()





