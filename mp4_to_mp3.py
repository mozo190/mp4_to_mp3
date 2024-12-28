from threading import Thread
from time import sleep
from tkinter.filedialog import askopenfile

from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from moviepy import VideoFileClip

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
        """Start the conversion process"""
        self.error_label.text = "Converting..... Please wait"
        self.error_label.pos_hint = {'center_x': .5, 'center_y': .2}
        self.error_label.color = (1, 1, 1, 1)
        self.activity_indicator.value = 0

        def conversionTask():
            try:
                video = VideoFileClip(self.openFile.name)
                audio = video.audio
                for i in range(0, 100, 10):
                    sleep(0.9)
                    self.activity_indicator.value = i
                audio.write_audiofile("assets/audio/output.mp3")
                self.error_label.text = "Conversion Done"
                self.error_label.pos_hint = {'center_x': .5, 'center_y': .2}
                self.activity_indicator.value = 100

            except Exception as e:
                self.error_label.text = "Error during conversion: " + str(e)
                self.error_label.pos_hint = {'center_x': .5, 'center_y': .2}

            finally:
                self.activity_indicator.parent.remove_widget(self.activity_indicator)

        Thread(target=conversionTask).start()

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
                                       pos_hint={'center_x': .5, 'center_y': .5}, color=(0, 1, 0),
                                       on_press=self.fileChooser)

        self.error_label = Label(text="", pos_hint={'center_x': .5, 'center_y': .4}, color=(1, 0, 0, 1))
        self.selected_file_label = Label(text="", pos_hint={'center_x': .5, 'center_y': .4}, color=(1, 1, 1))
        self.convert_btn = Button(text='Convert', size_hint=(.3, .1), pos_hint={'center_x': .5, 'center_y': .3},
                                  color=(0, 1, 0), on_press=self.convertToAudioThread, disabled=True)
        self.activity_indicator = ProgressBar(pos_hint={'center_x': .5, 'center_y': .1},
                                              size_hint=(.3, .1),
                                              value=0)

        # Widget section
        layout.add_widget(self.img)
        layout.add_widget(self.file_chooser_label)
        layout.add_widget(self.file_chooser_btn)
        layout.add_widget(self.error_label)
        layout.add_widget(self.selected_file_label)
        layout.add_widget(self.convert_btn)
        layout.add_widget(self.activity_indicator)

        return layout


if __name__ == '__main__':
    MyApp().run()
