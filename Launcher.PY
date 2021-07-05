from Nebula import *
import tkinter as tk
from tkinter import messagebox
def add_text(mw,st,imsg):
    message_send_by_bot=''
    message_send_by_human=''
    if(imsg.get().strip()==''):
        pass
    else:

        message_send_by_human=str(imsg.get())
        message_to_be_displayed = 'User:\t\n\t'+message_send_by_human+'\t\n'
        res = str(message_send_by_human) 
        result = str(chatbot(res))
        if (result=='None'):
            message_send_by_bot='Nebula:\n\t'+'Sorry but I need some updates'+'\n'
        else: 
            message_send_by_bot='Nebula:\n\t'+result+'\n'
        mw.config(state='normal')
        mw.insert('end',message_to_be_displayed)
        mw.insert('end',message_send_by_bot)
        imsg.set("")
        mw.see('end')
        mw.config(state='disabled')

# def show_author():
#     messagebox.showinfo("complain","sorry there is no information")
window = tk.Tk()
input_message=tk.StringVar(window)
input_message.set("")
window.bind('<Return>',lambda x:add_text(message_window,input_entry,input_message))
window.title('Chatbot')
window.geometry('600x600')
window['bg'] = 'black'
fram1 = tk.Frame(height=60, width=100, bg='white')
fram2 = tk.Frame(height=400, width=100, bg='white')
fram3 = tk.Frame(height=80, width=100, bg='white')

bot_name = tk.Label(fram1,
                    text='Nebula',
                    bg='white',
                    font=('Times New Roman', 45),
                    width=19, height=2
                    )
bot_name.pack(side='left')

# about_button = tk.Button(fram1,
#                          text='complain',
#                          width=10, height=2,
#                          relief='groove',
#                          bg='white',
#                          command=show_author)
# about_button.pack(side='right')

input_entry=tk.Entry(fram3,width=10,
                     bg='white',textvariable=input_message)
input_entry.pack(side='right',expand='YES',fill='both')

message_window=tk.Text(fram2,bg='white',yscrollcommand='YES')
message_window.insert('end','Nebula:Only one sentence can be understood.\n\t'+'\n')
message_window.config(state='disabled')
message_window.pack(side='top',expand='YES',fill='both')

send_button = tk.Button(fram3,text='Enter',
                        width=10,
                        height=4,
                        relief='groove',
                        bg='white',
                        state='active',
                        command=lambda :add_text(message_window,input_entry,input_message)
                        )
send_button.pack(side='right')
fram1.pack(fill='x', side='top')
fram2.pack(fill='both', expand='YES')
fram3.pack(fill='x', side='bottom')
window.mainloop()

