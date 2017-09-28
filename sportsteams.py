from random import randrange

class teams():
	def __init__(self, sport, team_name, city, captain):
		self.sport = sport
		self.team_name = team_name
		self.city = city
		self.captain = captain


	def championships(self):
		if self.sport == "hockey":
			return "{} have won {} Stanley Cups in the past 10 years.".format(self.team_name, randrange(0, 10))
		elif self.sport == "football":
			return "{} have won {} Vince Lombardi's in the past 10 years.".format(self.team_name, randrange(0, 10))
		elif self.sport == "basketball":
			return "{} have won {} Larry O'Brien's in the past 10 years.".format(self.team_name, randrange(0, 10))
		elif self.sport == "soccer":
			return "{} have won {} FIFA World Cups in the past 10 years.".format(self.team_name, randrange(0, 3))

	def teamInfo(self):
		return "The {}'s are a {} team that play in {}, and their captain is {}.".format(self.team_name, self.sport, self.city, self.captain)


my_team = teams("hockey", "Da Booties", "Hell", "Michael Cera")
wins = my_team.championships()
info = my_team.teamInfo()
print (wins)
print (info)

my_fteam = teams("football", "Dank Memes", "Atlantis", "Justin Timberlake")
print ("\n", my_fteam.championships())
print (my_fteam.teamInfo())

my_lteam = teams('basketball', "Living Arts", 'Ann Arbor', 'Mark Jones')
print ("\n", my_lteam.championships())
print (my_lteam.teamInfo())
