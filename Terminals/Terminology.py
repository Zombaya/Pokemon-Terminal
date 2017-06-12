import os
from Terminals.terminalInterface import TerminalInterface 

class Terminology(TerminalInterface): 

	def change_terminal(self,pokemon):
		os.system("tybg \"" + pokemon.get_path() + "\"")

	def clear_terminal(self):
		os.system("tybg")

	def determine_terminal_pokemon(self):
		print("background determination not possible with this terminal")