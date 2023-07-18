# quotes.toscrape.com
from tkinter import Tk, Button
from PIL import ImageTk, Image

class myButton(Button):
    def __init__(self, pict, command):
        self.image = Image.open(pict)
        self.command = command
        self.image = self.image.resize((100, 100))
        self.pict = ImageTk.PhotoImage(self.image)
        super().__init__(image=self.pict, command=command)


#b2 = myButton(text="123", width=15, height=3, image="1.png") # Полно
# b2 = myButton("123", 15, 3, "1.png") # Коротко
# b2.pack()


root = Tk()
root.geometry('800x600')
root.title('Красивая кнопка')
image = '100.jpg'

# Button(root, image=pict, command=lambda: print('click')).pack()
myButton(image, command=lambda: print('click')).pack()
root.mainloop()
