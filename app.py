from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from dbconnect import DBconnect
import random


class Quiz:

    def __init__(self):


        self._db = DBconnect()
        self.login_window()
    def login_window(self):

        self._root = Tk()
        self._root.title("QUIZADDA")
        self._root.maxsize(600,800)
        self._root.minsize(600,800)
        self._root.config(background= "#660033")

        self._open= Label(self._root,text="QUIZADDA",fg="#ffd11a",bg="#660033")
        self._open.config(font=("Algerian",45,"bold"))
        self._open.pack(pady=(35,20))

        imageurl = "images\logo2.png"
        load = Image.open(imageurl)
        load = load.resize((200, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(image=render, bg="#660033")
        img.image = render
        img.pack(pady=(10,20))

        self._name_entry = Label(self._root,text= "ENTER YOUR NAME",fg= "#ffd11a",bg="#660033")
        self._name_entry.config(font=("Times New Roman",18))
        self._name_entry.pack(pady=(10,15))

        self._name_entryInput = Entry(self._root)
        self._name_entryInput.pack(pady=(10,15),ipadx = 70,ipady= 10)

        self._email_entry = Label(self._root,text="ENTER YOUR EMAIL",fg= "#ffd11a",bg="#660033")
        self._email_entry.config(font=("Times New Roman",18))
        self._email_entry.pack(pady=(10,15))

        self._email_entryInput = Entry(self._root)
        self._email_entryInput.pack(pady=(10,15),ipadx=70,ipady=10)

        self._enter = Button(self._root,text="START",fg = "#ffffff",bg = "#1a1aff",width= 15,height= 2,command= lambda : self.enter_user())
        self._enter.config(font=("Times New Roman",18))
        self._enter.pack(pady=(10,15))

        self._root.mainloop()

    def clear(self):
        for i in self._root.pack_slaves():
            i.destroy()

    def enter_user(self):
        self._name = self._name_entryInput .get()
        self._email = self._email_entryInput.get()
        self.participant_answer = []

        if len(self._name) > 0 and len(self._email) > 0:
            flag = self._db.enter_user(self._name, self._email)

            if flag == 1:
                self.clear()
                self.load_quiz_window()
            else:
                messagebox.showerror("ERROR", "SORRY SOMETHING WENT WRONG. PLEASE TRY AGAIN")
        else:
            messagebox.showerror("ERROR", "PLEASE GIVE A NAME & EMAIL TO PLAY")

    def calculation(self):
        self.clear()
        self.marks = 0
        x = 0


        for i in self.index:
            if self.participant_answer[x] == self.correct_ans[i]:
                self.marks= self.marks + 10
            x = x + 1
        print(self.marks)
        self.score_entry()

    def replay(self):
        self.clear()
        self.load_quiz_window()

    def total_marks(self):

        self._marks_lbl = Label(self._root, text="GAME OVER", fg="#66F607", bg="#660033")
        self._marks_lbl.config(font=("Algerian", 45, 'bold',"underline"), justify="center")
        self._marks_lbl.pack(pady=(50, 50))

        self._marks_lbl = Label(self._root,text=str(self._name),fg="#FFFFFF",bg="#660033")
        self._marks_lbl.config(font=("Times New Roman",35,"bold"),)
        self._marks_lbl.pack(pady=(20,10))
        self._marks_lbl =Label(self._root,text ="YOUR FINAL SCORE IS ", fg="#FFFFFF", bg="#660033", wraplength=500)
        self._marks_lbl.config(font=("Times New Roman",25,"bold"), justify="center")
        self._marks_lbl.pack(pady=(0, 2))
        self._marks_lbl = Label(self._root,text=str(self.marks),fg="#FBFA0C", bg="#660033")
        self._marks_lbl.config(font=("Times New Roman",35,"bold"))
        self._marks_lbl.pack(pady=(0,10))



        if self.marks >= 80:


            self._marks_lbl = Label(self._root, text="YOU ARE  EXCELLENT!", fg="#FFFFFF",
                                       bg="#660033")
            self._marks_lbl.config(font=("Eras Bold ITC", 18, 'bold'), justify="center")
            self._marks_lbl.pack(pady=(10, 40))

        elif self.marks < 80 and self.marks >= 40:

            self._marks_lbl= Label(self._root, text="WELL DONE!.YOU DID WELL",
                                       fg="#FFFFFF", bg="#660033", wraplength=500)
            self._marks_lbl.config(font=("Eras Bold ITC", 18, 'bold'), justify="center")
            self._marks_lbl.pack(pady=(10, 40))

        else:

            self._marks_lbl = Label(self._root,
                                       text="NEED TO WORK HARD.YOU CAN BE BETTER!",
                                       fg="#FFFFFF", bg="#660033", wraplength=500)
            self._marks_lbl.config(font=("Eras Bold ITC", 18, 'bold'))
            self._marks_lbl.pack(pady=(10, 10))


        imageurl = "images\wdone2.jpg"
        load = Image.open(imageurl)
        load = load.resize((280, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(image=render, bg="#660033")
        img.image = render
        img.pack(pady=(10,15))

        self.replay_btn=Button(self._root,text="REPLAY", fg="#E5E7E9", bg="#2582AB",width=16, height=2,command=lambda: self.replay())
        self.replay_btn.config(font=("Arial",16))
        self.replay_btn.pack(pady=(10,20))



    def score_entry(self):

        flag = self._db.score_entry(self.marks, self._email)
        if flag == 1:
            self.total_marks()
        else:
            messagebox.showerror("ERROR", " SOME PROBLEM IS THERE! TRY AGAIN!")

    def gen(self):
        self.ques=1
        self.index= []

        while(len(self.index) < 10):

            x = random.randint(0,19)
            if x in self.index:
                continue
            else:
                self.index.append(x)
        print(self.index)


    def answered(self):

        x = self.radiovar.get()
        self.participant_answer.append(x)
        self.radiovar.set(-1)
        if self.ques < 10:
            self._labelqustion.config(text=self._qustions[self.index[self.ques]])
            self._r1['text'] = self._options[self.index[self.ques]][0]
            self._r2['text'] = self._options[self.index[self.ques]][1]
            self._r3['text'] = self._options[self.index[self.ques]][2]
            self._r4['text'] = self._options[self.index[self.ques]][3]
            self.ques = self.ques + 1

        else:
            print(self.participant_answer)
            self.calculation()




    def start_quiz(self):
        self.gen()
        self._qustions = [

            "Q.1. What is the normal timing of an international football match?",
            "Q.2. What is the full form of RAM?",
            "Q.3. On which date is the republic day of India celebrated every year?",
            "Q.4. In Which of the following states Bharatnatyam is folk dance?",
            "Q.5. Where is the Wankhede stadium located?",
            "Q.6. Which place is called the orchid paradise in India?",
            "Q.7. Whose birthday is celebrated as teacher's day",
            "Q.8. What is the National Sport in England?",
            "Q.9. Who invanted Telescope? ",
            "Q.10.Who is founder of Tata Group? ",
            "Q.11.Which Of the following states is not located in the North of India ?",
            "Q.12.Which state has the largest population in India?",
            "Q.13.Who was the champion of 2014 FIFA World Cup?",
            "Q.14.The World lLargest desert is?",
            "Q.15.Who is the popularly called as Iron Man of India?",
            "Q.16.Which is The tallset Building in world?",
            "Q.17.What is The Largest spoken Languge in The World?",
            "Q.18.Which is the Hardest substance Available on Earth?",
            "Q.19.Who is the current Indian Cricket team Captain in Test?",
            "Q.20.Most Populated Countrey in the World?"
        ]

        self._options = [
            ["60 minutes", "120 minutes", "90 minutes", "180 minutes"],
            ["Right Access Memory", "Random Access Memory", "Random All Memory", "None of the above"],
            ["january 26", "August 15", "May 1", "October 2"],
            ["Manipur", "Uttar pradesh", "Tamil Nadu", "Gujrat"],
            ["Kolkata", "Hydrabad", "Himachal Pradesh", "Mumbai"],
            ["Arunachal Pradesh", "Rajasthan", "Kerala", "Telengana"],
            ["Derozio", "S Radhakrishnan", "Mother Teresa", "Vidyasagar"],
            ["Cricket", "Football", "Rugby", "Baseball"],
            ["Gutenberg", "Graham Bell", "Galileans", "Edison"],
            ["Jamsetji Tata", "Ratan Tata", "Naval Tata", "Dorabji Tata"],
            ["Jharkhand", "jammu Kashmir", "Himachal Pradesh", "Harayana"],
            ["uttar Pradesh", "West Bengal", "Bihar", "Maharastra"],
            ["Brazil", "Spain", "Germany", "Argentina"],
            ["Thar", "Kalahari", "Sahara", "Sonoran"],
            ["Subhash chandra Bose", "Sardar vallabhbhai Patel", "jawaharlal nehru", "Govind ballabh Pant"],
            ["Burjh Khalifa", "Sanghai Tower", "Makkah Royal Clock", "jeddah Tower"],
            ["English", "mandarin", "Hindi", "Urdu"],
            ["Rock", "Iron", "Steel", "Diamond"],
            ["Kapil dev", "MS Dhoni", "Rohit Sharma", "Virat kohli"],
            ["India", "China", "UK", "Russia"]

        ]

        self.correct_ans = [2,1,0,2,3,0,1,0,2,0,0,0,2,2,1,0,1,3,3,1]

        self._labelqustion=Label(self._root, text =self._qustions[self.index[0]], font=("Times New Roman",30,), width =500, justify="center", wraplength=500,fg="#FFFFFF",bg="#660033")
        self._labelqustion.pack(pady=(50,20))

        self.radiovar = IntVar()
        self.radiovar.set(-1)

        self._r1 = Radiobutton(self._root, text=self._options[self.index[0]][0], font=("Times", 25), value=0, variable=self.radiovar,fg="#FFFFFF",bg="#660033", command=lambda: self.answered())
        self._r1.pack()

        self._r2 = Radiobutton(self._root, text=self._options[self.index[0]][1], font=("Times", 25), value=1, variable=self.radiovar,fg="#FFFFFF",bg="#660033", command=lambda: self.answered())
        self._r2.pack()

        self._r3 = Radiobutton(self._root, text=self._options[self.index[0]][2], font=("Times", 25), value=2, variable=self.radiovar,fg="#FFFFFF",bg="#660033", command=lambda: self.answered())
        self._r3.pack()

        self._r4 = Radiobutton(self._root, text=self._options[self.index[0]][3], font=("Times", 25), value=3, variable=self.radiovar,fg="#FFFFFF",bg="#660033", command=lambda: self.answered())
        self._r4.pack()

        #self._next=Button(self._root, text="Next", fg="#E5E7E9", bg="#2582AB", width=25, height=3, command=lambda: self.answered())
        #self._next.config(font=("Times",16))
        #self._next.pack(pady=(40,10))



    def button_pressed(self):
        self.clear()
        self.start_quiz()



    def clear(self):
        for i in self._root.pack_slaves():
            i.destroy()



    def load_quiz_window(self):


        self._namelabel = Label(self._root, fg="#44CD1E", bg="#660033")
        self._namelabel.config(text="HELLO!\n " + str(self._name) )
        self._namelabel.config(font=("Algerian", 30,"bold"))
        self._namelabel.pack(pady=(50, 18))

        self._readylabel = Label(self._root, text="ARE YOU READY FOR  QUIZADDA ?", fg="#DBE326", bg="#660033")
        self._readylabel.config(font=("BROADWAY", 20,"bold" ))
        self._readylabel.pack(pady=(14, 50))

        self._followlabel = Label(self._root, text="READ THE INSTRUCTIONS CAREFULLY\n BEFORE STARTING !",fg="#E5E7E9", bg="#EA0655")
        self._followlabel.config(font=("Arial", 20, 'bold'))
        self._followlabel.pack(pady=(0, 20))

        self._rules1label = Label(self._root, text="1. THERE ARE TOTAL 10 QUESTIONS\n THAT YOU HAVE TO ATTEND", fg="#E5E7E9", bg="#660033")
        self._rules1label.config(font=("Arial", 14))
        self._rules1label.pack(pady=(10, 10))

        self._rules2label = Label(self._root, text="2. ALL QUESTIONS CONSISTS OF 10(Five)\n MARKS EACH", fg="#E5E7E9",bg="#660033")
        self._rules2label.config(font=("Arial", 14))
        self._rules2label.pack(pady=(0, 10))

        self._rules3label = Label(self._root, text="3. ALL QUESTIONS ARE COMPULSORY", fg="#E5E7E9", bg="#660033")
        self._rules3label.config(font=("Arial", 14))
        self._rules3label.pack(pady=(0, 10))

        self._rules4label = Label(self._root, text="4. ALL ARE MCQ TYPE QUESTIONS", fg="#E5E7E9", bg="#660033")
        self._rules4label.config(font=("Arial", 14))
        self._rules4label.pack(pady=(0, 10))

        self._rules5label = Label(self._root, text="5. ONLY ONE OPTION IS CORRECT", fg="#E5E7E9", bg="#660033")
        self._rules5label.config(font=("Arial", 14))
        self._rules5label.pack(pady=(0, 10))

        self._rules6label = Label(self._root, text="6. AFTER READING THE RULES CAREFULLY\n PRESS THE BUTTON TO START", fg="#E5E7E9",bg="#660033")
        self._rules6label.config(font=("Arial", 14))
        self._rules6label.pack(pady=(0, 10))

        self._start = Button(self._root, text="START QUIZ", fg="#E5E7E9", bg="#2582AB", width=25, height=3, command=lambda: self.button_pressed())
        self._start.config(font=("Arial", 10,"bold"))
        self._start.pack(pady=(10, 15))








obj=Quiz()


