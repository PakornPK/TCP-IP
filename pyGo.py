from tkinter import *
from tkinter import ttk 


class Application(Frame):
    def __init__(self, master):
        """ Initialize frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):

        ip_addr = StringVar()
        ip_port = StringVar()

        self.mainFrame = Frame(self,width=500, height=500)
        self.mainFrame.grid()

        lb_title = Label(self.mainFrame,text='This is Programe DEMO TCP/IP by Python',font=('Angsana New',18))
        lb_title.place(x=100,y=10)
        
        lb_ip = Label(self.mainFrame,text='IP Address :',font=('Angsana New',14))
        lb_ip.place(x=10,y=50)
        tb_ip = ttk.Entry(self.mainFrame,textvariable = ip_addr)
        tb_ip.place(x=77,y=55)

        lb_port = Label(self.mainFrame,text='Port :',font=('Angsana New',14))
        lb_port.place(x=45,y=80)
        tb_port = ttk.Entry(self.mainFrame,textvariable = ip_port)
        tb_port.place(x=77,y=85)

        btn_start = ttk.Button(self.mainFrame,text= 'Start',command= self.start_server)
        btn_start.place(x=210,y=52)

        self.tb_status = Text(self.mainFrame,width=60,height=15)
        self.tb_status.place(x=7,y=125)
        
        

    def start_server(self):
        self.tb_status.insert(END, "Starting Server.....\r\n")
        

        

root=Tk()
#alter window
root.title("TEST Server")
root.geometry("500x500")
app=Application(root)
root.mainloop()
