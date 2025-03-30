import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import random 
import turtle_kremala 

class  HangmanGui:
    """Δημιουργεί τα γραφικά του βασικού παραθύρου και της εντολές για το γνωστό παιχνίδι ΚΡΕΜΑΛΑ"""
    def __init__(self,root):
        self.window = root
        self.reload_str =''
        self.tries = 0
        self.letters = []
        self.widgets()
        self.choose_hidden_word()
        self.commands_for_difficulty()

    def widgets(self):
        """Δημιουργεί τα frame/label/StringVariables/entryboxes"""
        # Menu
        self.my_menu = tk.Menu(self.window)
        self.window.config(menu = self.my_menu)

        # Frames
        self.window.config(bg = 'white')
        self.f1 = tk.LabelFrame(self.window,bg = 'white')
        self.f4 = tk.Frame(self.window,bg ='white')
        self.f5 = tk.Frame(self.window)
        self.f6 = tk.Canvas(self.window,width=300, height=385)#hangman <<gif>>
        self.f7 = tk.Frame(self.window,bg = 'red',width = 500,height = 400)
        self.f2 = tk.Frame(self.f4,bg = 'white')
        self.f3 = tk.Frame(self.f4,bg = 'white')

        # Labels
        self.title = tk.Label(self.f1,text = 'ΚΡΕΜΑΛΑ',font ='Arial 20',bg = 'white',fg = 'black')
        self.entrylabel = tk.Label(self.f2,text = 'Πίθανο γραμμα;→',bg = 'white',font = 'Arial 18')
        self.save_new_word = tk.Label(self.f3,text = 'Προσθέστε νέα λέξη: ',bg = 'white',font = 'Arial 18')

        # StringVariables
        self.entry_word_text = tk.StringVar()
        self.save_new_word_text = tk.StringVar()
        self.entry_letter_text = tk.StringVar()

        # Entry boxes
        self.entry_save_new_word = tk.Entry(self.f3,width = '15',bg = 'white',font = 'bolt 15',fg = 'black',bd='2',textvariable = self.save_new_word_text)
        self.entryletter = tk.Entry(self.f2,width ='2',bg ='white',bd ='3' ,fg = 'black',font = 'bolt 15',textvariable = self.entry_letter_text)
        self.entryword = tk.Entry(self.f5,width = 17,bg = 'white',bd = 5,font = 'arial 20',fg ='black',textvariable = self.entry_word_text)

        # ScrolledText Configuration
        self.system_to_user = ScrolledText(self.f7,height = 16,bg = 'white',fg = 'black',font = 'Calibri 15',wrap = 'word')

        # Menu options        
        self.mode = tk.Menu(self.my_menu,tearoff = False)
        self.my_menu.add_cascade(label = "Λειτουργία",menu = self.mode)
        self.mode.add_command(label='Μέρα',command = lambda:self.set_mode('white','black'))
        self.mode.add_command(label = 'Νύχτα',command = lambda:self.set_mode('black','white'))

        self.difficulty = tk.Menu(self.my_menu,tearoff = False)
        self.my_menu.add_cascade(label='Επίπεδο Δυσκολίας',menu = self.difficulty)
        self.easy = 8
        self.medium = 6
        self.hard = 4
        self.difficulty.add_command(label = 'Εύκολο',command = lambda:self.commands_for_difficulty(self.easy))
        self.difficulty.add_command(label = 'Μέτριο',command = lambda:self.commands_for_difficulty(self.medium))
        self.difficulty.add_command(label = 'Δύσκολο',command = lambda:self.commands_for_difficulty(self.hard))

        #Buttons
        self.check_letter_button = tk.Button(self.f2,text ="✔",font = 'Bolt 10',bg = '#1AB663',fg = 'black',command = self.check_entry_letter)
        self.save_new_word_button = tk.Button(self.f3,text = '+',font = 'Bolt 10',bg = '#1AB663',fg = 'black',command =self.save_new_word_to_txt)
        
        #bind Buttons
        self.window.bind('<Return>',lambda *args:[self.check_entry_letter()])

        #Pack
        self.f1.pack(side = 'top',expand = 0 ,fill = "both")
        self.f4.pack(side ='top',fill = 'x')
        self.f5.pack(side ='top',fill = 'x')
        self.f6.pack(side = 'left',anchor = 'nw')
        self.f7.pack(side ='right',fill = 'x',anchor = 'ne')
        self.f2.pack(side = 'left',pady = 10,padx = 10)
        self.f3.pack(side = 'right',pady = 10,padx = 20)
        self.title.pack(side='top',expand =1,fill='both')
        self.entrylabel.pack(side = 'left')
        self.entryletter.pack(side = 'left')
        self.check_letter_button.pack(side ='left',padx = 8)
        self.save_new_word.pack(side = 'left')
        self.entry_save_new_word.pack(side ='left')
        self.save_new_word_button.pack(side='right',padx = 8)
        self.entryword.pack(expand = 1,fill = 'x')
        self.system_to_user.pack(side = 'top',expand = 0)

    def set_mode(self,bg_color,fg_color):
        """ Μετατρέπει το background χρώμα απο λευκό σε μάυρο και αντρίστροφα.Αντίστοιχα για το χρώμα των γραμμάτων"""
        # Main window
        self.window.config(bg = bg_color)
        # Frames
        self.f1['bg'] = bg_color
        self.f4['bg'] = bg_color
        self.f2['bg'] = bg_color
        self.f3['bg'] = bg_color
        # Labels
        self.title['bg'] = bg_color
        self.entrylabel['bg'] = bg_color
        self.save_new_word['bg'] = bg_color
        self.title['fg'] = fg_color
        self.entrylabel['fg'] = fg_color
        self.save_new_word['fg'] = fg_color
        # Entry_boxes
        self.entry_save_new_word['bg'] = bg_color
        self.entryletter['bg'] = bg_color
        self.entryword['bg'] = bg_color
        self.entry_save_new_word['fg'] = fg_color
        self.entryletter['fg'] = fg_color
        self.entryword['fg'] = fg_color
        # buttons
        self.check_letter_button['fg'] = fg_color
        # ScrolledText
        self.system_to_user.config(bg = bg_color,fg = fg_color)
        # hangman_gif
        self.hanganman_gif.white_dark_mode(bg_color,fg_color)
    
    def save_new_word_to_txt(self):
        """ Είσαγει νέα λέξη στο λεξικό και τις προβάλει στο χρήστη"""
        with open("words.txt",'a',encoding='utf-8') as f:
            new_word = self.entry_save_new_word.get()
            new_word = new_word.upper()
            if new_word.isalpha():
                f.write('\n'+new_word)
        with open("words.txt",'r',encoding='utf-8') as f:
            self.system_to_user.insert('end',"Οι λεξεις που περιέχονται στο λεξικό:\n{}".format(f.read()))

    def commands_for_difficulty(self,difficulty=0):
        """Ορίζει το επίπεδο δυσκολίας και δίνει τιμή στις προσπάθειες που έχει ο χρήστης"""
        self.hanganman_gif = turtle_kremala.TurtleHangman(difficulty,self.f6)
        if difficulty == 0:
            self.system_to_user.insert('end','→Επιλέξτε επίπεδο δυσκολίας.\n')
        else:
            # print(self.tries)
            if difficulty == 8 and (self.tries == 8 or self.tries == 6 or self.tries == 4 or self.tries == 0):
                self.difficulty.entryconfig(0,label = '→Εύκολο')
                self.difficulty.entryconfig(1,label = 'Μέτριο')
                self.difficulty.entryconfig(2,label = 'Δύσκολο')
                self.system_to_user.insert('end','→To Eπίπεδο δυσκολίας ορίστηκε ως εύκολο\n Έχετε {} προσπάθειες\n'.format(difficulty))
                self.tries = difficulty

            elif difficulty == 6 and (self.tries == 8 or self.tries == 6 or self.tries == 4 or self.tries == 0):
                self.difficulty.entryconfig(1,label = '→Μέτριο')
                self.difficulty.entryconfig(0,label = 'Εύκολο')
                self.difficulty.entryconfig(2,label = 'Δύσκολο')
                self.system_to_user.insert('end','→To Eπίπεδο δυσκολίας ορίστηκε ως μέτριο\n Έχετε {} προσπάθειες\n'.format(difficulty))
                self.tries = difficulty

            elif difficulty == 4 and (self.tries == 8 or self.tries == 6 or self.tries == 4 or self.tries == 0):
                self.difficulty.entryconfig(2,label = '→Δύσκολο')
                self.difficulty.entryconfig(0,label = 'Εύκολο')
                self.difficulty.entryconfig(1,label = 'Μέτριο')
                self.system_to_user.insert('end','→To Eπίπεδο δυσκολίας ορίστηκε ως δύσκολο\n Έχετε {} προσπάθειες\n'.format(difficulty))
                self.tries = difficulty

            else:
                self.system_to_user.insert('end','Εφοσόν αρχήσατε το παιχνίδι το επίπεδο δυσκολίας δεν μπορεί να αλλάξει εως την λήξη\n')

    def choose_hidden_word(self):
        """Διαλέγει την κρυφή λεξη απο το αρχείο words.txt και θέτει ' _ ' στο self.entryword """
        with open('words.txt', 'r',encoding='utf-8')as f:
            self.hidden_word = random.choice(f.readlines()).rstrip() # Σημείωση η f.readlines() γυρναει μία λίστα 
                                                                    # με καθε στοιχείο της λίστα να είναι η γραμμή του αρχείου
            # print(self.hidden_word)
        empty = ' _ '*len(self.hidden_word)
        self.entry_word_text.set(empty)
    
    def check_entry_letter(self):
        """ Ελέγχει αν το γράμμα του χρήστη υπάρχει στην λέξη. Δίνει ως έξοδο την κρυμμένη λεξη με ' _' 
        και γραμμάτα που έχει πετύχει ο χρήστης και σβήνει το γράμμα που τοποθέτησε ο χρήστης""" 
        empty_str = ""
        user_letter = self.entryletter.get()
        user_letter = user_letter.upper()
        self.entry_letter_text.set(self.reload_str)
        if len(user_letter)==1 and user_letter.isalpha():
            # print(self.hidden_word)
            if user_letter in self.hidden_word and not(user_letter in self.letters):
                
                # print('→ Μπράβο! Το {} υπάρχει'.format(user_letter))
                self.system_to_user.insert('end','→ Μπράβο! Το {} υπάρχει\n'.format(user_letter))
            else:
                if not(user_letter in self.letters):
                    # print('→ Δυστηχώς το {} ΔΕΝ υπάρχει'.format(user_letter))
                    self.system_to_user.insert('end','→ Δυστηχώς το {} ΔΕΝ υπάρχει\n'.format(user_letter))
                    self.tries -=1
                    self.hanganman_gif.set_output()
                    if self.tries >=0:
                        self.system_to_user.insert('end','{} Προσπάθειες απομένουν\n'.format(self.tries))
                    else:
                        self.system_to_user.insert('end',"ΛΥΠΑΜΕ ΧΑΣΑΤΕ")
                        self.loser_window()
            self.letters.append(user_letter)
            for letter in self.hidden_word:
                if letter in self.letters:
                    empty_str+=str(letter)
                else:
                    empty_str+=' _'
            # print(empty_str)
            self.entry_word_text.set(empty_str)
        else:
            if len(user_letter)>1 : 
                # print('Ένα γράμμα, Δώσατε: ',user_letter)
                self.system_to_user.insert('end','✘ Ένα γράμμα, Δώσατε: {}\n'.format(user_letter))
            if not(user_letter.isalpha()):
                # print('Μόνο γράμματα. ΟΧΙ άλλα σύμβολα')
                self.system_to_user.insert('end','✘ Μην αφήνετε κενο. Μόνο γράμματα. ΟΧΙ άλλα σύμβολα\n')
        self.check_entry_word()


    def check_entry_word(self):
        """Ελένχει αν ο χρήστης βρήκε την λέξη"""
        entry_word = self.entryword.get()
        entry_word = entry_word.upper()
        if entry_word == self.hidden_word:
            self.system_to_user.insert('end','!!! ΣΥΓΧΑΡΗΤΗΡΙΑ ΚΕΡΔΙΣΑΤΕ !!!\n')
            self.winner_window()
        elif self.hidden_word in entry_word or self.hidden_word.lower() in entry_word:
            self.system_to_user.insert('end','Ελέγξτε αν έχετε κένα ή ορθόγραφικά λάθη\nΗ λέξη πρέπει να εισαχθεί χωρίς κενά στην αρχή και με κεφαλαία\n')
            # print('not yet')
    
    def winner_window(self):
        """ Δημιουργεί το νικητήριο παράθυρο"""
        self.winner_message1 = tk.Toplevel(self.window,bg = 'green')
        self.winner_message1.title('Βρήκατε τήν λέξη')
        self.winner_message1.geometry('550x150+{}+{}'.format(int((self.window.winfo_screenwidth()//2)-275),int((self.window.winfo_screenheight()//2)-75)))
        self.winner_message1.resizable(False,False)
        self.winner_message1.overrideredirect (True)
        tk.Label(self.winner_message1,text = '!!! ΣΥΓΧΑΡΗΤΗΡΙΑ ΚΕΡΔΙΣΑΤΕ !!!',bg = 'green',font = 'bolt  20').pack(expand = 1,fill = 'both')
        new_game_button = tk.Button(self.winner_message1,text = "Νέο παιχνίδι",bg = 'lightgreen',font = 'arial 15',command = self.new_game_command).pack(side='right',anchor = 'se',fill = 'x')
        exit_game_button = tk.Button(self.winner_message1,text = 'ΕΞΟΔΟΣ',bg = 'red',font = 'arial 13',command =self.exit_game_command).pack(side='left',anchor = 'sw',fill = 'x')
                
    def loser_window(self):
        """ Δημιουργεί το παράθυρο της ήττας"""
        self.loser_message1 = tk.Toplevel(self.window,bg = '#ac1e44')
        self.loser_message1.title('Δυστήχως δεν βρήκατε την λέξη')
        self.loser_message1.geometry('550x150+{}+{}'.format(int((self.window.winfo_screenwidth()//2)-275),int((self.window.winfo_screenheight()//2)-75)))
        self.loser_message1.resizable(False,False)
        self.loser_message1.overrideredirect (True)
        tk.Label(self.loser_message1,text = 'ΧΑΣΑΤΕ\nΤΕΛΟΣ ΠΑΙΧΝΙΔΙΟΥ',bg = '#ac1e44',font = 'bolt  20').pack(expand = 1,fill = 'both')
        new_game_button = tk.Button(self.loser_message1,text = "Νέο παιχνίδι",bg = 'lightgreen',font = 'arial 15',command = self.new_game_command).pack(side='right',anchor = 'se',fill = 'x')
        exit_game_button = tk.Button(self.loser_message1,text = 'ΕΞΟΔΟΣ',bg = 'red',font = 'arial 13',command =self.exit_game_command).pack(side='left',anchor = 'sw',fill = 'x')

    def new_game_command(self):
        """ Καταστρέφει το βασικό παράθυρο και δημιουργεί καινούριο"""
        self.window.destroy()
        root = tk.Tk()
        root.geometry('800x560+{}+{}'.format(int((root.winfo_screenwidth()//2)-800//2),int((root.winfo_screenheight()//2)-560//1.5)))
        root.resizable(False,False)
        HangmanGui(root)
        root.title('###Κρεμαλα###')
        root.mainloop()
        HangmanGui(root)
    
    def exit_game_command(self):
        """Καταστρέφει το βασικό παράθυρο"""
        self.window.destroy()

def main():
    root = tk.Tk()
    root.geometry('800x560+{}+{}'.format(int((root.winfo_screenwidth()//2)-800//2),int((root.winfo_screenheight()//2)-560//1.5)))
    root.resizable(False,False)
    HangmanGui(root)
    root.title('###Κρεμαλα###')
    root.mainloop()




if __name__ == "__main__":
    main()
