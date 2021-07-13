from otree.api import *
c = Currency  


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label='What is your age?', min=18, max=125)
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female'], ['Other','Other']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    
    )
    nationality = models.StringField(label='What is your nationality?')
    english_level = models.StringField(
        label = 'How would you rate your English level?',
        choices=[['Native or Bilingual Proficiency', 'Native or Bilingual Proficiency'], ['Full Professional Proficiency', 'Full Professional Proficiency'], ['Minimum Professional Proficiency','Minimum Professional Proficiency'], ['Elementary Proficiency','Elementary Proficiency']],
        widget=widgets.RadioSelect,
    )
    profession = models.StringField(
        label='Please indicate your employment status',
        choices=[['Unemployed', 'Unemployed'], ['Employed', 'Employed'], ['Student','Student'], ['Retired','Retired'],['Other','Other']],
        widget=widgets.RadioSelect,)
    if_other_prof = models.StringField(
        label="if other, please specify (if not, fill in a /)"
    )
    education = models.StringField(
        label='What is your highest level of education?',
        choices=[['No education', 'No education'], ['Elementary', 'Elementary'], ['High School','High School'], ['Bachelors or equivalent','Bachelors or equivalent'],['Masters or equivalent','Masters or equivalent'],['Doctoral or equivalent','Doctoral or equivalent'],['Other','Other']],
        widget=widgets.RadioSelect,)
    if_other_edu = models.StringField(
        label="if other, please specify (if not, fill in a /)"
    )
    RTcrt1 = models.FloatField(blank=True)
    RTcrt2 = models.FloatField(blank=True)
    RTcrt3 = models.FloatField(blank=True)
    RTcrt4 = models.FloatField(blank=True)
    crt1 = models.StringField(
       label = 'If you’re running a race and you pass the person in second place, what place are you in?'
    )
    crt2 = models.StringField(
       label = 'A farmer had 15 sheep and all but 8 died. How many are left?'
    )
    crt3 = models.StringField(
       label = 'Laura’s  father has  three  daughters. The first two are named  April and May.  What is the third daughter’s name? '
    )

    crt4 = models.StringField(
       label = 'How many cubic feet of dirt are there in a hole that is 3’ deep x 3’ widex 3’ long?'
    )

    q1 = models.StringField(
        choices = [[1, 'A'], [0, 'B']], 
        label = 'Scenario 1',
        widget = widgets.RadioSelectHorizontal,
        default = 0
    )
    
    q2 = models.StringField(
        choices = [[1, 'A'], [0, 'B']], 
        label = 'Scenario 1',
        widget = widgets.RadioSelectHorizontal,
        default = 0
    )
    q3 = models.StringField(
        choices = [[1, 'A'], [0, 'B']], 
        label = 'Scenario 1',
        widget = widgets.RadioSelectHorizontal,
        default = 0
    )
    q4 = models.StringField(
        choices = [[1, 'A'], [0, 'B']], 
        label = 'Scenario 1',
        widget = widgets.RadioSelectHorizontal,
        default = 0
    )
    q5 = models.StringField(
        choices = [[1, 'A'], [0, 'B']], 
        label = 'Scenario 1',
        widget = widgets.RadioSelectHorizontal,
        default = 0
    )
    q6 = models.StringField(
        choices = [[1, 'A'], [0, 'B']], 
        label = 'Scenario 1',
        widget = widgets.RadioSelectHorizontal,
        default = 0
    )
    q7 = models.StringField(
        choices = [[1, 'A'], [0, 'B']], 
        label = 'Scenario 1',
        widget = widgets.RadioSelectHorizontal,
        default = 0
    )
    q8 = models.StringField(
        choices = [[1, 'A'], [0, 'B']], 
        label = 'Scenario 1',
        widget = widgets.RadioSelectHorizontal,
        default = 0
    )
    q9 = models.StringField(
        choices = [[1, 'A'], [0, 'B']], 
        label = 'Scenario 1',
        widget = widgets.RadioSelectHorizontal,
        default = 0
    )
    q10 = models.StringField(
        choices = [[1, 'A'], [0, 'B']], 
        label = 'Scenario 1',
        widget = widgets.RadioSelectHorizontal,
        default = 0
    )
    RTq1 = models.FloatField(blank=True)
    RTq2 = models.FloatField(blank=True)
    RTq3 = models.FloatField(blank=True)
    RTq4 = models.FloatField(blank=True)
    RTq5 = models.FloatField(blank=True)
    RTq6 = models.FloatField(blank=True)
    RTq7 = models.FloatField(blank=True)
    RTq8 = models.FloatField(blank=True)
    RTq9 = models.FloatField(blank=True)
    RTq10 = models.FloatField(blank=True)

    email = models.StringField(
        label= 'If you wish to participate in the lottery, please indicate your email address'
    
    )

#Big Five Personality Test

#Neuroticism
    bigN1 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigN2 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigN3 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigN4 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigN5 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigN6 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigN7 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigN8 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigN9 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigN10 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
#Extraversion

    bigE1 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigE2 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigE3 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigE4 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigE5 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigE6 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigE7 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigE8 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigE9 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigE10 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )

#Conscientiousness

    bigC1 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigC2 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigC3 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigC4 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        default = 1
    )
    bigC5 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigC6 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigC7 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigC8 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigC9 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigC10 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )

#openness
    bigO1 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigO2 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigO3 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigO4 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigO5 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigO6 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigO7 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigO8 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigO9 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )
    bigO10 = models.StringField(
        choices = [[1, 'Does not apply at all'], [0,'Rather does not apply'], [2,'Rather applies'], [3, 'Applies exactly']],
        widget = widgets.RadioSelectHorizontal,
        default = 1
    )




# FUNCTIONS
# PAGES
class Instructions(Page):
    form_model = 'player'
 
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender','nationality','english_level','profession','if_other_prof','education','if_other_edu','email']

class CRT1(Page):
    form_model = 'player'
    form_fields = ['crt1','RTcrt1']

class CRT2(Page):
    form_model = 'player'
    form_fields = ['crt2','RTcrt2']

class CRT3(Page):
    form_model = 'player'
    form_fields = ['crt3', 'RTcrt3']

class CRT4(Page):
    form_model = 'player'
    form_fields = ['crt4', 'RTcrt4']

class RiskQ1(Page):
    form_model = 'player'
    form_fields = ['q1','RTq1']

class RiskQ2(Page):
    form_model = 'player'
    form_fields = ['q2','RTq2']

@staticmethod
def is_displayed(player):
      return player.q1 == 1

class RiskQ3(Page):
    form_model = 'player'
    form_fields = ['q3','RTq3']

@staticmethod
def is_displayed(player):
      return player.q2 == 1

class RiskQ4(Page):
    form_model = 'player'
    form_fields = ['q4','RTq4']

@staticmethod
def is_displayed(player):
      return player.q3 == 1

class RiskQ5(Page):
    form_model = 'player'
    form_fields = ['q5','RTq5']

@staticmethod
def is_displayed(player):
      return player.q4 == 1

class RiskQ6(Page):
    form_model = 'player'
    form_fields = ['q6','RTq6']

@staticmethod
def is_displayed(player):
      return player.q5 == 1

class RiskQ7(Page):
    form_model = 'player'
    form_fields = ['q7','RTq7']

@staticmethod
def is_displayed(player):
      return player.q6 == 1

class RiskQ8(Page):
    form_model = 'player'
    form_fields = ['q8','RTq8']

@staticmethod
def is_displayed(player):
      return player.q7 == 1

class RiskQ9(Page):
    form_model = 'player'
    form_fields = ['q9','RTq9']

@staticmethod
def is_displayed(player):
      return player.q8 == 1

class RiskQ10(Page):
    form_model = 'player'
    form_fields = ['q10','RTq10']

@staticmethod
def is_displayed(player):
      return player.q9 == 1

#pages for personality questions

#neuroticism

class bigN1(Page):
    form_model = 'player'
    form_fields = ['bigN1']

class bigN2(Page):
    form_model = 'player'
    form_fields = ['bigN2']

class bigN3(Page):
    form_model = 'player'
    form_fields = ['bigN3']

class bigN4(Page):
    form_model = 'player'
    form_fields = ['bigN4']

class bigN5(Page):
    form_model = 'player'
    form_fields = ['bigN5']

class bigN6(Page):
    form_model = 'player'
    form_fields = ['bigN6']

class bigN7(Page):
    form_model = 'player'
    form_fields = ['bigN7']

class bigN8(Page):
    form_model = 'player'
    form_fields = ['bigN8']

class bigN9(Page):
    form_model = 'player'
    form_fields = ['bigN9']

class bigN10(Page):
    form_model = 'player'
    form_fields = ['bigN10']

#extraversion

class bigE1(Page):
    form_model = 'player'
    form_fields = ['bigE1']

class bigE2(Page):
    form_model = 'player'
    form_fields = ['bigE2']

class bigE3(Page):
    form_model = 'player'
    form_fields = ['bigE3']

class bigE4(Page):
    form_model = 'player'
    form_fields = ['bigE4']

class bigE5(Page):
    form_model = 'player'
    form_fields = ['bigE5']

class bigE6(Page):
    form_model = 'player'
    form_fields = ['bigE6']

class bigE7(Page):
    form_model = 'player'
    form_fields = ['bigE7']

class bigE8(Page):
    form_model = 'player'
    form_fields = ['bigE8']

class bigE9(Page):
    form_model = 'player'
    form_fields = ['bigE9']

class bigE10(Page):
    form_model = 'player'
    form_fields = ['bigE10']

#Conscientiousness

class bigC1(Page):
    form_model = 'player'
    form_fields = ['bigC1']

class bigC2(Page):
    form_model = 'player'
    form_fields = ['bigC2']

class bigC3(Page):
    form_model = 'player'
    form_fields = ['bigC3']

class bigC4(Page):
    form_model = 'player'
    form_fields = ['bigC4']

class bigC5(Page):
    form_model = 'player'
    form_fields = ['bigC5']

class bigC6(Page):
    form_model = 'player'
    form_fields = ['bigC6']

class bigC7(Page):
    form_model = 'player'
    form_fields = ['bigC7']

class bigC8(Page):
    form_model = 'player'
    form_fields = ['bigC8']

class bigC9(Page):
    form_model = 'player'
    form_fields = ['bigC9']

class bigC10(Page):
    form_model = 'player'
    form_fields = ['bigC10']

#openness

class bigO1(Page):
    form_model = 'player'
    form_fields = ['bigO1']

class bigO2(Page):
    form_model = 'player'
    form_fields = ['bigO2']

class bigO3(Page):
    form_model = 'player'
    form_fields = ['bigO3']

class bigO4(Page):
    form_model = 'player'
    form_fields = ['bigO4']

class bigO5(Page):
    form_model = 'player'
    form_fields = ['bigO5']

class bigO6(Page):
    form_model = 'player'
    form_fields = ['bigO6']

class bigO7(Page):
    form_model = 'player'
    form_fields = ['bigO7']

class bigO8(Page):
    form_model = 'player'
    form_fields = ['bigO8']

class bigO9(Page):
    form_model = 'player'
    form_fields = ['bigO9']

class bigO10(Page):
    form_model = 'player'
    form_fields = ['bigO10']

class ThankYou(Page):
    form_model = 'player'

page_sequence = [Instructions, bigN1, bigC4, bigE3, bigC3, bigN7, bigO7, bigC2, bigN5, bigO2, bigE8, bigO3,  bigO5, CRT1, bigE6, bigO4, bigO10, bigN3, bigC9, bigO1, bigO6, bigC5, bigC6, bigC7, CRT2, bigE10, bigO9, bigO8, CRT3, bigE9, bigE4, bigE5, bigN8, bigN9, bigN10, bigE7, bigE1, bigE2, bigN4, bigC8, bigC10, bigN6, CRT4, bigC1, bigN2, RiskQ1, RiskQ2, RiskQ3, RiskQ4, RiskQ5, RiskQ5, RiskQ6, RiskQ7, RiskQ8, RiskQ9, RiskQ10, Demographics, ThankYou]

    

    

  

  