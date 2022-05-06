from tkinter import *
import time
import webbrowser
from tkHyperLink import *
from functools import partial
import get_response as response
import trial
import os



BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# chatbot class for designing and implementing chatbot
class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()



    def run(self):
        self.window.mainloop()

    def show_hand_cursor(self,a):
        self.text_widget.config(cursor="hand")

    def hide_hand_cursor(self,a):
        self.text_widget.config(cursor='')

    def _setup_main_window(self):
        self.window.title("CoVBOT by Drunk Bits")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=570, height=750, bg=BG_COLOR)

        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="CoVBOT", font=(FONT_BOLD,20), pady=10)
        head_label.place(relwidth=1)





        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # text widget
        self.text_widget = Text(self.window, width=20, height=13, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5,wrap=WORD)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.tag_config('you',foreground='red')

        self.hl = HyperlinkManager(self.text_widget)
        #self.text_widget.tag_bind("link", "<1>", self.callback())

        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.pack(side=RIGHT)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(bottom_label, text="ASK", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)


    # function to perform when ENTER key is pressed, the input is displayed in chatbot
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        if msg in ['clear','del','delete','new']:
            self.msg_entry.delete(0, END)
            return self.text_widget.delete('1.0', END)
        self.msg_entry.delete(0, END)
        msg1 = f"\n{'You'}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1,'you')
        self.window.update()
        
        time.sleep(1)


        # function call for response
        self._insert_message(msg, "You")


    # function to return the output of the by calling response function
    def _insert_message(self, msg, sender):

        if not msg:
            return
        if msg in ['quit','exit','stop','bye']:

            self.text_widget.insert(END, "BOT: Thank you for talking to me. Good Bye !")
            self.text_widget.see(END)
            self.window.update()
            time.sleep(2)
            self.window.destroy()
        elif msg.isnumeric():
            bot_response = response.get_response(msg)
            if type(bot_response) == dict:
                cnam = trial.nam(msg)
                mm = f"\nCOVID-19 cases for {cnam} county: \n"
                self.text_widget.config(state=NORMAL)
                self.text_widget.insert(END,mm)
                self.text_widget.see(END)
                self.window.update()

                for k,v in bot_response.items():
                    msg2 = f"\n-{k} {v}\n"
                    self.text_widget.config(state=NORMAL)
                    self.text_widget.insert(END, msg2)
                    self.text_widget.see(END)
                    self.window.update()
            if type(bot_response) == str:
                msg4 = f"\n{'BOT: '}{bot_response}\n"
                self.text_widget.insert(END, msg4)
                self.window.update()

        else:
            bot_response = response.get_response(msg)
            if type(bot_response) == str:
                msg4 = f"\n{'BOT: '}{bot_response}\n"
                self.text_widget.insert(END, msg4)
                self.window.update()

            elif type(bot_response) == list:
                ct=0
                mg = f"\n{'BOT: '}{'I can help you with following things !'}\n"
                self.text_widget.insert(END, mg)
                self.window.update()
                for i in bot_response:
                    ct +=1
                    self.text_widget.insert(END,f"\n{ct}. {i} \n")
                    self.window.update()



            elif type(bot_response) == dict:
                count = 0
                for k,v in bot_response.items():
                    count += 1
                    msg2 = f"\n{'H'}{count}{' '}:{' '}{v}\n"

                    self.text_widget.config(state=NORMAL)
                    self.text_widget.insert(END,msg2)
                    self.text_widget.see(END)
                    linkk = f"{k} \n"
                    self.window.update()
                    self.text_widget.config(state=NORMAL)
                    self.text_widget.insert(END,'\nClick to Read More \n', self.hl.add(partial(webbrowser.open, k)))
                    self.text_widget.insert(END, "------------------------------------------------------------------------------------------------------------------\n")
                    self.window.update()
                    self.text_widget.see(END)
                    # pyttsx3.speak(msg2)
                    time.sleep(3)
                    self.text_widget.see(END)



                    if count==8:
                        break



            self.text_widget.see(END)




if __name__ == "__main__":
    app = ChatApplication()
    app.run()
