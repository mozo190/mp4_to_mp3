from threading import Thread
from moviepy.editor import VideoFileClip
from tkinter.filedialog import askopenfile

from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.app import MDApp

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

from kivy.core.window import Window

class MyApp(MDApp):
    def build(self):

        layout = MDRelativeLayout()

        return layout


if __name__ == '__main__':
    MyApp().run()