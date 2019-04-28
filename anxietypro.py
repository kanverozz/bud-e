import os
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics.instructions import InstructionGroup
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.uix.anchorlayout import AnchorLayout
from json import load
from os.path import exists
from kivy.uix.image import AsyncImage
from kivy.animation import Animation
from kivy.properties import ObjectProperty
from kivy.core.audio import SoundLoader
from google.cloud import language_v1
from google.cloud.language_v1 import enums
from google.cloud import language
import six
from google.cloud.language import types
import sys
import operator
from kivy.properties import StringProperty


class MainWindow(Screen):
    sound = SoundLoader.load('C:/Users/abhis/Desktop/New folder/music.wav')
    sound.play()



class SecondWindow(Screen):
    pass


class SecondWindowDepression(Screen):
    pass


class ThirdWindow(Screen):
    pass

class FourthWindow(Screen):
    pass

class FifthWindow(Screen):
    pass

class SixthWindow(Screen):
    pass

class TextWindow(Screen):
    def entity_text(self):

        entitydict = {}

        def entity_sentiment_text(text):
            """Detects entity sentiment in the provided text."""
            client = language.LanguageServiceClient.from_service_account_json(
                "C:/Users/abhis/Desktop/New folder/ravi_nl_service_account.json")

            if isinstance(text, six.binary_type):
                text = text.decode('utf-8')

            document = types.Document(
                content=text.encode('utf-8'),
                type=enums.Document.Type.PLAIN_TEXT)

            # Detect and send native Python encoding to receive correct word offsets.
            encoding = enums.EncodingType.UTF32
            if sys.maxunicode == 65535:
                encoding = enums.EncodingType.UTF16

            result = client.analyze_entity_sentiment(document, encoding)

            for entity in result.entities:
                name = format(entity.name)
                for mention in entity.mentions:
                    magnitude = format(mention.sentiment.magnitude)
                entitydict[name] = magnitude
            sorted_entitydict = sorted(entitydict.items(), key=operator.itemgetter(1))
            return entitydict

        last_name_text_input = ObjectProperty()
        surname = self.last_name_text_input.text
        entitydict = entity_sentiment_text(surname)

        entitydictkeys = []
        entitydictvalues = []
        for key in entitydict:
            entitydictkeys.append(key)
            entitydictvalues.append(entitydict[key])

        school_occupation = ["homework", "hw", "study", "studying",
                             "work", "job", "tests", "school",]
        relationships = ["boyfriend", "girlfriend", "family", "parents",
                         "mom", "dad", "brother", "brothers", "sister",
                         "sisters", "friends", "friend", "best friend",
                         "best friends", "date","relationship","relationships"]
        drugs = ["drugs", "drug", "weed", "marijuana", "nicotine",
                 "tobacco", "smoking", "blunt", "heroine", "crack"]
        entitydictkeys[0] = entitydictkeys[0].lower()
        match = False
        for i in school_occupation:
            if entitydictkeys[0] == i:
                match = True
            if match == True:
                word = "school_occupation"
                break
        if match == False:
            for i in relationships:
                if entitydictkeys[0] == i:
                    match = True
                if match == True:
                    word = "realationships"
                    break
        if match == False:
            for i in drugs:
                if entitydictkeys[0] == i:
                    match = True
                if match == True:
                    word = "drugs"
                    break

        if word == "school_occupation":
                print("It looks like you are having problems with school, here are some tips on how to cope with these pressures: \n1) Take time to take care of yourself. Make sure you are sleeping properly, maintaining good  eating habits, and taking the time to slow down and let your brain process. \n2)  Change your mindset to a more positive way. Instead of focusing on things like when a project will be due, focus on what you can do to work on the project right now. Adjust your mindset to focus on the present rather than worrying about what could happen in the future. \n3) Take baby steps with assignments. Instead of focusing on the big picture of an assignment or project, try to take small steps, doing small portions of the project at a time. This helps cope with the stress that comes with large assignments like these. \n4) Remember that it’s okay not to have extreme, far-reaching goals. We are not necessarily encouraging you to lower all of your standards, but things like being the best in class doesn’t have to be your goal, but passing your class with a grade or understandment level that you feel comfortable with. \n5) During one of the most stressful periods of the day, testing, staying balanced can be crucial. For example, taking breaks while testing can help you balance your work to relaxation time can lead to better testing scores and less stress.")
        elif word == "relationships":
                print("1) Try to use exercise and other anxiety reduction strategies.  First and foremost, anxiety is still anxiety, and that means that effective anxiety reduction strategies can help control the way you feel. Exercise is the easiest one to integrate into your life right now. There is a lot of evidence that exercise is as powerful as most anxiety medications for controlling anxiety symptoms.2) Another way of dealing with relationship anxiety is starting over. If the trust is gone, talk to your partner about starting over completely and dating as though you'd never been together. Trust is about building a foundation and needs to be grown from the ground up. You need to stick with it though. If after a few weeks things are getting better, it's still too soon to say the trust is back. You don't want to fall back into old habits.\n4) Make sure you are staying mentally busy. Being busy in relationships can be difficult, but something that is known to improve the mood of the relationship is to stay mentally busy. Often you'll find that your mind is your enemy in relationships, as you imagine fighting with your partner. So keep your mind off your relationship as much as possible by doing outdoor activities, watching TV, going on dates, and so on. This decreases the way your mind can wander into negative emotions.\n5) Always be physically affectionate. Touching and holding, even when you're mad at the other person, is very calming. It's one of the reasons that successful couples often hug after a long and hard day. Try to be more physically affectionate for a while, even when you're mad at them so that it sends that relaxing reminder that you and your partner aren't going anywhere.\n")
        elif word == "drugs":
                print("There are ways to deal with anxiety that don’t involve the usage of drugs. Dr. Ellen Vora gives us 5 tips on what exactly these ways are: \n1) Effectively deal with peer pressure. The biggest reason teens start using drugs is because their friends utilize peer pressure. No one likes to be left out, and teens (and yes, some adults, too) find themselves doing things they normally wouldn’t do, just to fit in. In these cases, you need to either find a better group of friends that won’t pressure you into doing harmful things, or you need to find a good way to say no. Teens should prepare a good excuse or plan ahead of time, to keep from giving into tempting situations.\n 3) Seek help for mental illness. Mental illness and substance abuse often go hand-in-hand. Those with a mental illness may turn to drugs as a way to ease the pain. Those suffering from some form of mental illness, such as anxiety, depression or post-traumatic stress disorder should seek the help of a trained professional for treatment before it leads to substance abuse. \n 4)Examine the risk factors. If you’re aware of the biological, environmental and physical risk factors you possess, you’re more likely to overcome them. A history of substance abuse in the family, living in a social setting that glorifies drug abuse and/or family life that models drug abuse can be risk factors. \n5)Keep a well-balanced life. People take up drugs when something in their life is not working, or when they’re unhappy about their lives or where their lives are going. Look at life’s big picture, and have priorities in order.\n")

class FirstButton(Screen):
    pass

class WindowManager(ScreenManager):
    pass



kv = Builder.load_file("my.kv")


class MyApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()
