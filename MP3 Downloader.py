
import tkinter as tk
from pytube import YouTube
import os
from PIL import Image, ImageTk
import sv_ttk

# class MyFrame(tk.Frame):
#     font= 'Roboto'
#     

    
#     def __init__(self, root):
#         super().__init__(root)
#         self.pack()

#         # create title label
#         self.title_label = tk.Label(self, text="YouTube MP3 Downloader", font=(self.font, 24), fg_color='red')
#         self.title_label.pack(padx=20, pady=20)

#         # create main entry and button
#         self.url_entry = tk.Entry(self, placeholder_text="Write the video url")
#         self.url_entry.pack(padx=20, pady=20)

#         self.main_button_1 = tk.Button(self, text='Download', command=self.download_event)
#         self.main_button_1.pack(padx=20, pady=20)

def download_event():
    try:
        print(url.get())
        # yt = YouTube(url)
        # print("\nDownloading....")
        # video = yt.streams.filter(only_audio=True).first()
        # out_file = video.download()
        # base, ext = os.path.splitext(out_file)
        # new_file = base + ".mp3"
        # os.rename(out_file, new_file)
        # print("\nSuccessfully Downloaded\n")

    except Exception as e:
        print(e)

root = tk.Tk()
url = tk.StringVar()
root.title("Youtube MP3 Downloader")

# Set maximum window size
root.geometry('1147x697')

root.minsize(1147, 697)
root.maxsize(1147, 697)

# Create a bg label
image = Image.open("./images/background.png")
root.photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=root.photo)
label.place(x=0, y=0, relwidth=1, relheight=1)

# Add a frame
frame = tk.Frame(root, bg="#020E13", bd=5)  # Create a frame with gray background color and border width of 5 pixels
frame.place(relx=0.5, rely=0.2, relwidth=0.6, relheight=0.6, anchor=tk.N)  # Example of placing the frame

# Add a label inside the frame
title_label = tk.Label(frame, bg="#020E13", fg="#77CBDF", justify=tk.CENTER, text="Youtube MP3 Downloader", font=('Roboto', 24) )
title_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)  # Example of placing a button in the center

# Add an entry inside the frame
url_entry = tk.Entry(frame, bg="#3D4E58", fg="#77CBDF", justify=tk.CENTER, relief=tk.FLAT, font=('Roboto', 13), textvariable=url)
url_entry.place(width=472, height=25, relx=0.5, rely=0.5, anchor=tk.CENTER)  # Example of placing a button in the center

# Add a button inside the frame
download_button = tk.Button(frame, text='Download', bg="#0E2B36", fg="#77CBDF", relief=tk.FLAT, font=('Roboto', 13), command=download_event)  # Set button background color to gray and foreground (text) color to white
download_button.place(width=198, height=25, relx=0.5, rely=0.65, anchor=tk.CENTER)  # Example of placing a button in the center

root.mainloop()
