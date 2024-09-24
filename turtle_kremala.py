import turtle as t

class TurtleHangman:
    """Σχεδιάζει τα γραφικά της κρεμάλας"""
    def __init__(self,difficulty = None,canvas = None):
        self.turtle_screen = t.TurtleScreen(canvas)
        self.turtle_screen.bgcolor('white')
        self.turtle = t.RawTurtle(self.turtle_screen,shape = 'circle')
        self.turtle.pencolor('black')
        self.turtle.hideturtle()
        self.turtle.speed(5)
        self.dif = difficulty
        self.mistake = 1

    def white_dark_mode(self,bg_color,fg_color):
        """ Αλλάζει τα λευκά γραφικά σε μαύρα και αντιστροφα"""
        self.turtle_screen.bgcolor(bg_color)
        self.turtle.pencolor(fg_color)

    def set_output(self):
        """ Ορίζει με ποιές διαδοχικές συνθήκες θα σχεδιαστή η κρεμάλα"""
        if self.dif == 8:
            self.turtle_gif_easy_mode()
        elif self.dif == 6:
            self.turtle_gif_medium_mode()
        elif self.dif == 4:
            self.turtle_gif_hard_mode()

    def turtle_gif_easy_mode(self):
        """ Γραφικά για επίπεδο δυσκολίας Εύκολο"""
        t = self.turtle
        if self.mistake==1:
            t.pensize(6)
            t.penup()
            t.goto(-120,-180)
            t.pendown()
            t.left(90)
            t.forward(350)
            self.mistake+=1
        elif self.mistake == 2:
            t.right(90)
            t.forward(150)
            self.mistake +=1
        elif self.mistake == 3:
            t.right(90)
            t.forward(50)
            t.pensize(4)
            t.right(90)
            self.mistake +=1
        elif self.mistake == 4:
            t.begin_fill()
            t.circle(30)
            t.end_fill()
            t.left(90)
            t.penup()
            t.forward(60)
            t.pendown()
            self.mistake +=1
        elif self.mistake == 5:
            t.forward(150)
            self.mistake +=1
        elif self.mistake == 6:
            t.right(45)
            t.forward(70)
            t.penup()
            t.backward(70)
            t.left(90)
            t.pendown()
            t.forward(70)
            t.penup()
            t.backward(70)
            self.mistake +=1
        elif self.mistake == 7:
            t.right(45+180)
            t.forward(100)
            t.pendown()
            t.left(45)
            t.forward(50)
            t.penup()
            t.backward(50)
            t.pendown()
            self.mistake +=1
        elif self.mistake == 8:
            t.right(90)
            t.forward(50)
            self.mistake +=1

    def turtle_gif_medium_mode(self):
        """ Γραφικά για επίπεδο δυσκολίας Μέτριο"""
        t = self.turtle
        if self.mistake==1:
            t.pensize(6)
            t.penup()
            t.goto(-120,-180)
            t.pendown()
            t.left(90)
            t.forward(350)
            self.mistake+=1
        elif self.mistake == 2:
            t.right(90)
            t.forward(150)
            t.right(90)
            t.forward(50)
            t.pensize(4)
            t.right(90)
            self.mistake +=1
        elif self.mistake == 3:
            t.begin_fill()
            t.circle(30)
            t.end_fill()
            t.left(90)
            t.penup()
            t.forward(60)
            t.pendown()
            self.mistake +=1
        elif self.mistake == 4:
            t.forward(150)
            self.mistake +=1
        elif self.mistake == 5:
            t.right(45)
            t.forward(70)
            t.penup()
            t.backward(70)
            t.left(90)
            t.pendown()
            t.forward(70)
            t.penup()
            t.backward(70)
            self.mistake +=1
        elif self.mistake == 6:
            t.right(45+180)
            t.forward(100)
            t.pendown()
            t.left(45)
            t.forward(50)
            t.penup()
            t.backward(50)
            t.pendown()
            t.right(90)
            t.forward(50)
            self.mistake +=1

    def turtle_gif_hard_mode(self):
        """ Γραφικά για επίπεδο δυσκολίας Δύσκολο"""
        t = self.turtle
        if self.mistake==1:
            t.pensize(6)
            t.penup()
            t.goto(-120,-180)
            t.pendown()
            t.left(90)
            t.forward(350)
            t.right(90)
            t.forward(150)
            t.right(90)
            t.forward(50)
            t.pensize(4)
            t.right(90)
            t.begin_fill()
            t.circle(30)
            t.end_fill()
            t.left(90)
            t.penup()
            t.forward(60)
            t.pendown()
            self.mistake +=1
        elif self.mistake == 2:
            t.forward(150)
            self.mistake +=1
        elif self.mistake == 3:
            t.right(45)
            t.forward(70)
            t.penup()
            t.backward(70)
            t.left(90)
            t.pendown()
            t.forward(70)
            t.penup()
            t.backward(70)
            self.mistake +=1
        elif self.mistake == 4:
            t.right(45+180)
            t.forward(100)
            t.pendown()
            t.left(45)
            t.forward(50)
            t.penup()
            t.backward(50)
            t.pendown()
            t.right(90)
            t.forward(50)
            self.mistake +=1