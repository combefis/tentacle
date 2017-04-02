from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen


class Home(Screen):
    pass

class Resistor(Screen):
    colors = ["Black","Brown","Red","Orange","Yellow","Green","Blue","Violet","Grey","White"]
    resistance_input = ObjectProperty()
    band1_spr = ObjectProperty()
    band2_spr = ObjectProperty()
    multi_spr = ObjectProperty()

    def calculateRes(self):
        bands = int(str(self.colors.index(self.band1_spr.text))+str(self.colors.index(self.band2_spr.text)))
        multiplier = 10**(self.colors.index(self.multi_spr.text))
        resistance = bands*multiplier
        exp = ""
        if resistance / 1000000 >= 1:
            exp = "M"
            resistance /= 1000000
        elif resistance / 1000 >= 1:
            exp = "k"
            resistance /= 1000

        self.resistance_input .text= str(resistance) + exp + "\u2126"

    def calculateBand(self):
        print("calc")
        try: 
            resistance = int(self.resistance_input.text)
        except ValueError:
            print("erreur")

        i = 0
        multi = 1
        while resistance % multi == 0:
            rest = resistance//multi
            if rest <= 10:
                multiplier = self.colors[i-1]
            else:
                multiplier = self.colors[i]
            i += 1
            multi = 10 ** i
        self.multi_spr.text = multiplier
        self.band1_spr.text = self.colors[int(str(rest)[0])]
        self.band2_spr.text = self.colors[int(str(rest)[1])]

class TentacleApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Home(name="home"))
        sm.add_widget(Resistor(name="resistor"))
        return sm

TentacleApp().run()
