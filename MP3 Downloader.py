
import tkinter
from tkinter import ttk
from pytube import YouTube
import os
from PIL import Image, ImageTk
import sv_ttk

# class MyFrame(ttk.Frame):
#     font= 'Roboto'
#     def download_event(self):
#         try:
#             url = self.url_entry.get()
#             yt = YouTube(url)
#             print("\nDownloading....")
#             video = yt.streams.filter(only_audio=True).first()
#             out_file = video.download()
#             base, ext = os.path.splitext(out_file)
#             new_file = base + ".mp3"
#             os.rename(out_file, new_file)
#             print("\nSuccessfully Downloaded\n")

#         except Exception as e:
#             print(e)

    
#     def __init__(self, root):
#         super().__init__(root)
#         self.pack()

#         # create title label
#         self.title_label = ttk.Label(self, text="YouTube MP3 Downloader", font=(self.font, 24), fg_color='red')
#         self.title_label.pack(padx=20, pady=20)

#         # create main entry and button
#         self.url_entry = ttk.Entry(self, placeholder_text="Write the video url")
#         self.url_entry.pack(padx=20, pady=20)

#         self.main_button_1 = ttk.Button(self, text='Download', command=self.download_event)
#         self.main_button_1.pack(padx=20, pady=20)


def main():
    root = tkinter.Tk()
    root.title("Youtube MP3 Downloader")
    sv_ttk.set_theme("dark")

    # Set maximum window size
    root.geometry('1150x700')
    root.maxsize(1150, 700)

    # Create a bg label
    image = Image.open("./images/background.png")
    root.photo = ImageTk.PhotoImage(image)
    label = ttk.Label(root, image=root.photo)
    label.place(x=0, y=0, relwidth=1, relheight=1)

    # Add a frame
    frame = ttk.Frame(root, bg="#020E13", bd=5)  # Create a frame with gray background color and border width of 5 pixels
    frame.place(relx=0.5, rely=0.2, relwidth=0.6, relheight=0.6, anchor=ttk.N)  # Example of placing the frame

    # Add other widgets inside the frame
    button = ttk.Button(root, text='Download', bg="#0E2B36", fg="#77CBDF", relief=ttk.FLAT)  # Set button background color to gray and foreground (text) color to white
    button.place(relx=0.5, rely=0.5, anchor=ttk.CENTER)  # Example of placing a button in the center

    root.mainloop()

if __name__ == "__main__":
    main()