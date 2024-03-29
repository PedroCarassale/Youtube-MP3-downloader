import tkinter
from tkinter import ttk

import sv_ttk

def main():
    root = tkinter.Tk()
    root.title("Youtube MP3 Downloader")
    sv_ttk.set_theme("dark")

    # Set maximum window size
    root.geometry('1150x700')
    root.maxsize(1150, 700)

    # Add a frame
    frame = ttk.Frame(root)  # Create a frame with width of 5 pixels
    frame.pack()  # Example of placing the frame

    # Add other widgets inside the frame
    button = ttk.Button(frame, text='Download')  # Set button background color to gray and foreground (text) color to white
    button.pack()  # Example of placing a button in the center

    root.mainloop()

if __name__ == "__main__":
    main()