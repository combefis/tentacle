from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class TentacleForm(BoxLayout):
    colors = ["Black","Brown","Red","Orange","Yellow","Green","Blue","Violet","Grey","White"]
    resistance_input = ObjectProperty()
    band1_spr = ObjectProperty()
    band2_spr = ObjectProperty()
    multi_spr = ObjectProperty()

    def calculateRes(self):
        bands = int(str(self.colors.index(self.band1_spr.text))+str(self.colors.index(self.band2_spr.text)))
        multiplier = 10**(self.colors.index(self.multi_spr.text))
        resistance = bands*multiplier
        if resistance % 1000000 == 0:
            exp = "M"
            resistance //= 1000000
        elif resistance % 1000 == 0:
            exp = "k"
            resistance //= 1000
        else:
            exp = ""
        self.resistance_input .text= str(resistance) + exp + "\u2126"


class TentacleApp(App):
    pass

TentacleApp().run()
