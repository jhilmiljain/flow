import sys

from st2common.runners.base_action import Action

class MyEchoAction(Action):
	def run(self,greeting):
		print(greeting, "Stackstorm")
