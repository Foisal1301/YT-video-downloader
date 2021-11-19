import os
try:
    import pytube
    from kivy.app import App
    from kivy.uix.label import Label
    from kivy.uix.gridlayout import GridLayout
    from kivy.uix.textinput import TextInput
    from kivy.uix.button import Button
except:
    os.system("pip install pytube kivy")
    import pytube
    from kivy.app import App
    from kivy.uix.label import Label
    from kivy.uix.gridlayout import GridLayout
    from kivy.uix.textinput import TextInput
    from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    #initialize infinite keyword
    def __init__(self,**kwargs):
        #call grid layout constructor
        super(MyGridLayout,self).__init__(**kwargs)

        #set columns
        self.cols = 1


        self.link_lbl = Label(text='Paste the url of your video',font_size=32)
        self.add_widget(self.link_lbl)

        self.link = TextInput(multiline=False,font_size=32)
        self.add_widget(self.link)

        self.path_lbl = Label(text="Enter your path or keep empty for default path",font_size=32)
        self.add_widget(self.path_lbl)

        self.path = TextInput(multiline=False,font_size=32)
        self.add_widget(self.path)

        self.down = Button(text="Download",font_size=32)
        self.down.bind(on_press=self.press)
        self.add_widget(self.down)

    def press(self,instance):
        link = self.link.text
        path = self.path.text

        if path == '':
            path = f"C:\\Users\\{os.getenv('USER',os.getenv('USERNAME','user'))}\\Desktop"

        self.link.text = ""

        try:
            yt = pytube.YouTube(link)
            yt.streams.get_highest_resolution().download(path)
            self.add_widget(Label(text="Successfully Downloaded!!!", font_size=64))
        except:
            self.add_widget(Label(text="Download Failed!!!!",font_size=72))

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()