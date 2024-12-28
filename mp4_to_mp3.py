# from moviepy.editor import VideoFileClip
from threading import Thread
from tkinter.filedialog import askopenfile

from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout

Window.size = (500, 400)


class MyApp(MDApp):
    def fileChooser(self, event):
        try:
            self.openFile = askopenfile(mode='r', filetypes=[('Video Files', '*.mp4')])
            if self.openFile:
                self.selected_file_label.text = self.openFile.name
                self.selected_file_label.pos_hint = {'center_x': .5, 'center_y': .4}
                self.convert_btn.pos_hint = {'center_x': .5, 'center_y': .3}
                self.convert_btn.disabled = False

        except Exception as e:
            self.error_label.text = "Error: File not selected " + str(e)

    def convertToAudio(self):
        pass

    def convertToAudioThread(self, event):
        thread1 = Thread(target=self.convertToAudio)
        thread1.daemon = True
        thread1.start()

    def build(self):
        layout = MDRelativeLayout(md_bg_color=(188 / 255, 108 / 255, 37 / 255, 1))

        # Label section
        self.img = Image(source="assets/img/images.jpg", size_hint=(1, 1),
                         pos_hint={'center_x': .5, 'center_y': .85})

        self.file_chooser_label = Label(text="Select a video file to convert to audio",
                                        pos_hint={'center_x': .5, 'center_y': .6},
                                        color=(1, 1, 1, 1))
        self.file_chooser_btn = Button(text="Choose File", size_hint=(.3, .1),
                                       pos_hint={'center_x':.5, 'center_y': .5}, color=(0, 1, 0), on_press=self.fileChooser)

        self.error_label = Label(text="", pos_hint={'center_x': .5, 'center_y': .4}, color=(1, 0, 0, 1))
        self.selected_file_label = Label(text="", pos_hint={'center_x': .5, 'center_y': .4}, color=(1, 1, 1))
        self.convert_btn = Button(text='Convert', size_hint=(.3, .1), pos_hint={'center_x': .5, 'center_y': .3},
                                  color=(0, 1, 0), on_press=self.convertToAudioThread, disabled=True)

        # Widget section
        layout.add_widget(self.img)
        layout.add_widget(self.file_chooser_label)
        layout.add_widget(self.file_chooser_btn)
        layout.add_widget(self.error_label)
        layout.add_widget(self.selected_file_label)
        layout.add_widget(self.convert_btn)

        return layout


if __name__ == '__main__':
    MyApp().run()
