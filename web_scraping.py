import requests #hacer consultas
from bs4 import BeautifulSoup #Parsear el html
import urllib #Guardar las imagenes

infinitive_original ='''Add
Afford
Agree
Announce
Answer
Appear
Arrive
Ask
Become
Begin
Believe
Bet
Bite
Bomb
Borrow
Break
Bring
Build
Buy
Call
Carry
Catch
Celebrate
Change
Chat
Check
Choose
Circle
Classify
Clean
Climb
Come
Compare
Complain
Complete
Conduct
Contain
Convert
Cook
Correct
Cost
Create
Cut
Dance
Date
Decide
Describe
Disagree
Discuss
Do
Draw
Dream
Drink
Drive
Dry
Earn
Eat
E-mail
End
Enjoy
Enter
Evaluate
Exchange
Exercise
Expand
Explain
Fall
Feel
Fight
Fill
Find
Finish
Fix
Fly
Forbid
Forget
Forgive
Form
Get up
Give
Go
Grow
Guess
Handle
Happen
Hate
Have
Hear
Help
Hide
Hike
Hit
Hold
Hope
Hurt
Imagine
Include 
Indicate
Insert
Interview
Introduce
Invite
Jog
Join
Keep
Know
Label
Lead
Learn
Leave
Let
Lift
Light
Like
List
Listen
Live
Look
Lose
Love
Make
Mark
Match
Meet
Mention
Miss
Move
Name
Need
Notice
Open
Order
Pay
Pick up
Plan
Play
Point
Practice
Prefer
Project
Promote
Put
Quit
Rain
Raise
Rank
React
Read
Receive
Recycle
Relax
Release
Remarry
Remember
Rent
Repair
Repeat
Report back
Represent
Rest
Retire
Return
Ride
Ring
Rise
Run
Save
Say
See
Sell
Serve
Set
Shake
Shoot
Show
Shut
Sing
Sit
Skate
Sleep
Smell
Smoke
Snow
Sound
Speak
Spell
Spend
Spill
Spread
Stand
Start
Stay
Stay up
Steal
Stick
Stink
Strike
Study
Suggest
Surf
Surround
Swear
Sweep
Swell
Swim
Swing
Take
Take care of
Talk
Teach
Tell
Test
Think
Throw
Tie
Trade
Travel
Try
Try on
Turn
Type
Underline
Understand
Upset
Use
Vacuum
Visit
Wait
Wake up
Walk
Want
Wash
Watch
Wear
Weep
Wet
Win
Work
Write'''


def string_array(lista):
    return lista.split('\n')

def run(lista):
    print('Espanol  -  Infinitive  -  Simple  -  Participle\n')
    listado = ''
    for idx, verb in enumerate(lista):

        lista_verb = ''

        response = requests.get(
            'http://conjugador.reverso.net/conjugacion-ingles-verbo-{}.html'.
            format(verb))  #accede por get a la url
        soup = BeautifulSoup(
            response.content,
            'html.parser')  #parsea (da formato) a la informacion de la pagina
        container = soup.find('div', {'id': 'ch_divSimple'})  #busca el id
        con_V = container.find('div', {'class': 'result-block clearfix'})
        #all
        #espanol
        #container_spa = soup.find('div', {'id': 'ch_divConjugatorHeader'})
        #div_spa = container_spa.find('div', {'id': 'ch_leftWordTransl'})
        #p_sp = div_spa.find('p', {'class': 'context-term'})
        #print(p_sp.text)
        listado += ('verbo  -')
        lista_verb += ('verbo  -')
        #infinitive
        listado += ('{}  -  '.format(str(verb)))
        lista_verb += ('{}  -  '.format(str(verb)))
        #simple
        tarjetas_simple_x = con_V.find('div', {'class': 'word-wrap-row'})
        div_simple = tarjetas_simple_x.find_all('div', {'class': 'wrap-three-col'})
        lista_simple = div_simple[1].find('ul',
                                        {'class': 'wrap-verbs-listing top2'})
        simple = lista_simple.find('i', {'class': 'verbtxt'})
        listado += '{}  -  '.format(str(simple.text))
        lista_verb += '{}  -  '.format(str(simple.text))
        #participle
        tarjetas_varias = con_V.find_all('div', {'class': 'word-wrap-row'})
        participle_div = tarjetas_varias[4].find(
            'ul', {'class': 'wrap-verbs-listing top3'})
        participle = participle_div.find('i')
        listado += '{}\n'.format(str(participle.text))
        lista_verb += '{}\n'.format(str(participle.text))
        #print('{} obtenido...\n'.format(verb))
        print('{}. {}'.format(idx, lista_verb))






if __name__ == '__main__':
    array_infinitive = string_array(infinitive_original)
    run(array_infinitive)
    #obtener()
