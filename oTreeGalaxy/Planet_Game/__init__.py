from otree.api import *
from otree import session
import random
import numpy as np
np.random.seed(seed=163)

c = Currency

doc = """
This app is supposed to guide the players through a galaxy of different planets. The participants can either choose to stay on a planet or 
they can choose to go to another planet. The game has several levels and every level has 100 rounds. In the end the score of the players
is displayed. 
"""


class Constants(BaseConstants): #variables that are constant for every participant
    name_in_url = 'Planet_Game'
    players_per_group = None #just 1 player so no group
    num_rounds = 2 #for now set to 4, because only test round
    #choices = ['Exploit', 'Explore']
    reward_planet_1 = random.randint(1,50)
    reward_planet_2 = random.randint(1,100)
    #in the extensive version I will have to include bigger lists here

    #to calculate the payoff for all previous rounds of a game, plus the current one: cumulative_payoff = sum([p.payoff for p in self.player.in_all_rounds()])

 
    
class Subsession(BaseSubsession): #round level can be specified here
    pass


class Group(BaseGroup): #this would be at the group level
    pass


class Player(BasePlayer): #variables to be specified per player -> these variables are saved

    #models will be the entire datasheets you will get
    nickname = models.StringField(
        #label = "Please enter a nickname that you would like to use",
    )
    forage_decision = models.BooleanField( #Booleanfields can only store true or false
    #label ="Please choose if you want to stay or keep going",
    #choices = [
        #[True, "Exploit"], 
        #[False, "Explore"], #change name of button otherwise it is too framed
    #]
    ) #here I can define what happens if player decides to explore or exploit/ in general actions
    #stop_search = models.BooleanField(
        #just asking after 3 rounds if the player would like to stay on this planet and stop his search
    #)
    #number_entered = models.IntegerField()
    #sum_of_rewards = models.IntegerField()

    def determine_reward(self): #based on input, determine rewards
        if self.forage_decision == False:
            self.payoff = Constants.reward_planet_1
        else:
            self.payoff = Constants.reward_planet_2



#probably I need to define something here
    #planets = {}

    #number_of_planets = 'num_rounds' #set number of planets to number of rounds as this is the same for the player as having an infinite amount of planets

    #for planet in range(number_of_planets):

        # generating current planet's empty dictionary
        #planets[planet] = {}

        # generating name
        #planets[planet]['name'] = 'planet_'+str(planet) #to be changed still but for now this is enough

        # generating planet center 
        #current_planet_center = np.random.randint(10, 90)
        #planets[planet]['center'] = current_planet_center
        
        # generating rewards
        #current_rewards = np.random.randint(current_planet_center - 10, current_planet_center + 10, size = 100)
        #planets[planet]['rewards'] = current_rewards
   

#Functions




# PAGES

class Nickname(Page): 
    form_model = 'player'
    form_fields = ['nickname']

    def displayed_once(self):
        if self.round_number == 1: #this means only in round 1 we want this to be displayed 
            return True
        else: 
            return False

class Level1(Page): #foraging page
    form_model = 'player'
    form_fields = ['forage_decision']
    #on this page we only want to choose whether we want to explore or exploit
    #on this page we also want to see a planet and a planet name

    def vars_for_template(self): 
        #creates variables that we can use in our template file
        #this one should create a random planet name 
        
        name_planet = "Uranus" #I can create a list and make it randomly select a name from it #for now it is just one name
        
        return{"name_planet": name_planet}

        #reward_2 = random.randint(1,100)
        #self.player.sum_of_rewards = reward_1 + reward_2 #by calling self we are referring to whatever object calls this; going to refer to the page the subject sees
        #return{
            #"reward_1": reward_1,

            #"reward_2": reward_2,
            
            #} 
    #check what player chose as an input and draws outcome
    
    
    pass   #this is a dictionary 
#iterate through planets

class Results(Page):
    timeout_seconds = 10
    timer_text = ''
    
    def vars_for_template(player):
        reward = player.determine_reward()
        return {"reward": reward,}
        

class CombinedResults(Page):
    def is_displayed(self): #this function makes sure that this is only shown in the last round. #I might want to change it though, such that total payoff is shown more often
        if self.round_number == Constants.num_rounds: #this means that we are in the last round 
            return True
        else: 
            return False
    #def vars_for_template(self):
        #all_players = self.player.in_all_rounds()
        #combined_payoff = 0
        #for player in all_players:
            #combined_payoff += player.payoff
        #return{
            #"combined_payoff": combined_payoff
        #}
   
page_sequence = [Nickname, Level1, Results] 

#I have a page in which they choose between exploit and explore, then they go to the next page in 
# which a result is shown. Then they go back to that back in which again they choose between exploit and
#explore, and then again a result is shown. Like this they learn. on results page I don't want a next button
#I just want it to have a timing 

#just a thought I had: I will always have 2 outcomes: either the player decides to exploit and gets an outcome, or the player
#decides to explore and first gets to a new planet, so we return a new name and then if he exploits, he gets an outcome. So 
#exploit returns a number, and explore returns a new name of the planet

#at the end of the levels, so in the last round, they should be able to press next
#in the very last level and last round, before pressing next, they should have a text saying, press next to proceed to the test/survey
