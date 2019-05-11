import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import os
import sys
import Encode
import Decode


class TheGrid(Widget):
	encode = ObjectProperty(None)
	decode = ObjectProperty(None)
	result = ObjectProperty(None)

	def encbtn(self):
		self.result.text = str(Encode.Encrypt(self.encode.text))
	def decbtn(self):
		self.result.text = str(Decode.Decrypt(self.decode.text))

class Abbrevify(App):
	def build(self):
		return TheGrid()


if __name__ == "__main__":
	Abbrevify().run()
