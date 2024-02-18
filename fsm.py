from tkinter import * 
evm=Tk() 
evm.geometry('455x333')
evm.title('e.v.m. (electronic voting machine)')
f1=Frame(evm,borderwidth=8,bg='green',relief=SUNKEN) 
f1.pack(side=TOP,fill=X,pady=40)
f2=Frame(evm,bg='sky blue',borderwidth=8,relief=SUNKEN) 
f2.pack(side=TOP)
# photo =PhotoImage(file='C:\\Users\\LENOVO\\Downloads\\election comm.png') 
# y=Label(f1,image=photo) 
# y.pack()
x=Label(f1,text='Election Commission of India',fg='black',bg='green')
x.pack()
d={'bjp':0,'con':0,'aap':0,'spa':0,'nota':0} 
def result():
    s=sorted(d.items(),key=lambda x:x[1])  
    print('the winner is',s[-1][0],'get votes',s[-1][1])
def bjp():
    d['bjp']+=1  
def con():
    d['con']+=1 
def aap():
    d['aap']+=1 
def spa():
    d['spa']+=1
def nota(): 
    d['nota']+=1 
def data():
    s=sorted(d.items(),key=lambda x:x[1]) 
    for i in range(len(s)):
        print(i+1,s[i]) 
def reset():
    for i in d.keys():
        d[i]=0

lin1=Label(f2,text='S NO.',bg='sky blue').grid(row=0,column=1)     
lin1=Label(f2,text='Name of candidate',bg='sky blue').grid(row=0,column=3) 
lin1=Label(f2,text='party',bg='sky blue').grid(row=0,column=5) 
lin1=Label(f2,text='SIGN',bg='sky blue').grid(row=0,column=7)
lin2=Label(f2,text='1.',bg='sky blue').grid(row=1,column=1)     
lin2=Label(f2,text='Narendra Modi',bg='sky blue').grid(row=1,column=3) 
lin2=Label(f2,text='BJP',bg='sky blue').grid(row=1,column=5) 
# photobjp =PhotoImage(file='C:\\Users\\LENOVO\\Downloads\\bjp2.png') 
# lin2=Label(f2,image=photobjp,bg='sky blue').grid(row=1,column=7) 
b1=Button(f2,fg='black',bg='grey',text='bjp',command=bjp).grid(row=1,column=9)
lin2=Label(f2,text='2.',bg='sky blue').grid(row=2,column=1)     
lin2=Label(f2,text='Rahul Gandhi',bg='sky blue').grid(row=2,column=3) 
lin2=Label(f2,text='Congress',bg='sky blue').grid(row=2,column=5) 
# photocong =PhotoImage(file='C:\\Users\\LENOVO\\Downloads\\cong2.png') 
# lin2=Label(f2,image=photocong,bg='sky blue').grid(row=2,column=7) 
b2=Button(f2,fg='black',bg='grey',text='cong',command=con).grid(row=2,column=9)
lin3=Label(f2,text='3.',bg='sky blue').grid(row=3,column=1)     
lin3=Label(f2,text='Arvind Kejriwal',bg='sky blue').grid(row=3,column=3) 
lin3=Label(f2,text='AAP',bg='sky blue').grid(row=3,column=5) 
# photoaap =PhotoImage(file='C:\\Users\\LENOVO\\Downloads\\aap2.png') 
# lin3=Label(f2,image=photoaap,bg='sky blue').grid(row=3,column=7) 
b3=Button(f2,fg='black',bg='grey',text='AAP',command=aap).grid(row=3,column=9)
lin4=Label(f2,text='4.',bg='sky blue').grid(row=4,column=1)     
lin4=Label(f2,text='Akhilesh Yadav',bg='sky blue').grid(row=4,column=3) 
lin4=Label(f2,text='SPA',bg='sky blue').grid(row=4,column=5) 
# photospa =PhotoImage(file='C:\\Users\\LENOVO\\Downloads\\spa2.png') 
# lin4=Label(f2,image=photospa,bg='sky blue').grid(row=4,column=7) 
b4=Button(f2,fg='black',bg='grey',text='spa',command=spa).grid(row=4,column=9) 
lin5=Label(f2,text='5.',bg='sky blue').grid(row=5,column=1)     
lin5=Label(f2,text='---',bg='sky blue').grid(row=5,column=3) 
lin5=Label(f2,text='NOTA',bg='sky blue').grid(row=5,column=5) 
# photonota =PhotoImage(file='C:\\Users\\LENOVO\\Downloads\\nota2.png') 
# lin5=Label(f2,image=photonota,bg='sky blue').grid(row=5,column=7) 
b5=Button(f2,fg='black',text='nota',bg='grey',command=nota).grid(row=5,column=9) 
b6=Button(f2,fg='white',text='data',bg='black',command=data).grid(row=6,column=2) 
b7=Button(f2,fg='white',text='result',bg='black',command=result).grid(row=6,column=4)  
b8=Button(f2,fg='white',text='reset',bg='black',command=reset).grid(row=6,column=7) 
evm.mainloop()

