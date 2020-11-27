import ctypes  # An included library with Python install.
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
Mbox('ALERT!', 'Drink atleast 3 liters water in a day', 1)