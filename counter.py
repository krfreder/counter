from guizero import App, Text

def counter():
    text.value = int(text.value) + 1

app = App(bg="black") #This sets the background color to black
app.set_full_screen("f11")
app.tk.bind('<Escape>', lambda e: app.tk.destroy()) #To exit fullscreen press the <Escape> key

text = Text(app, height = "fill", font = "Calibri", size = 60, text = "Pints Poured")
text.text_color = "white" #This sets the font color for the words "Pints Poured"
text = Text(app, height = "fill", font = "Calibri", size = 90, text = "1") #Whenever you need to correct the count, adjust the number within quotes after 'text = '
text.text_color = "red" #This sets the font color for the number
text.repeat(5000, counter) #The number is the amount of milliseconds you want the counter to wait before it increases

app.display()