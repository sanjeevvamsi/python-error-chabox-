# Importing everything needed
from tkinter import *
from chatbot import *

# Defining colours
BG_GREY = '#ABB2B9'
BG_COLOR = '#17202A'
TEXT_COLOR = '#EAECEE'

# Defining fonts
FONT = 'Helvetica 14'
FONT_BOLD = 'helvetica 13 bold'

#starting of gui
class chatbot_gui:
    
    def __init__(self):
        self.window = Tk()
        self.layout_window()
        
    def run(self):
        self.window.mainloop()
        
    def layout_window(self):
        self.window.title('Python error solver')
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

        # top label
        top_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome", font=FONT_BOLD, pady=10)
        top_label.place(relwidth=1)

        # chat area
        self.chat_area = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.chat_area.place(relheight=0.745, relwidth=1, rely=0.08)
        self.chat_area.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrollbar = Scrollbar(self.chat_area)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.chat_area.yview)
        
        # bottom label
        bottom_label = Label(self.window, bg=BG_GREY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
        # message entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GREY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        
        
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        msg = msg.lower()
        self._insert_message(msg, "You")
        
    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)

        # linking process
        you = f"{'you'}: {msg}\n\n"
        self.chat_area.configure(state=NORMAL)
        self.chat_area.insert(END, you)
        self.chat_area.configure(state=DISABLED)
        
        response = chatting(msg)
        if response=='terminate':
            exit(0)
        
        bot = f"{bot_name}: {response}\n\n"
        self.chat_area.configure(state=NORMAL)
        self.chat_area.insert(END, bot)
        self.chat_area.configure(state=DISABLED)

        self.chat_area.see(END)
    

if __name__ == "__main__":
    app = chatbot_gui()
    app.run()