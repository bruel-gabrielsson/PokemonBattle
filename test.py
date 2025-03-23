from ai21 import AI21Client
from ai21.models.chat import ChatMessage

KEY = 'v7uBaXL8sXKB4SmHsrxIOa14sYsWPcT9'

client = AI21Client(api_key=KEY)  # or pass it in directly

response = client.chat.completions.create(
    model='jamba-large',
    messages=[ChatMessage(role='user', content='Hello, please provide a brief explanation of what AI21 does, in 100 words or less', role='assistant', content='nah!')]
)

"""

You are an immersive battle simulator, similar to Pokémon battles but adapted for a variety of imaginative scenarios and characters.

There are two combatants: Player1 and Player2. Each has chosen one unique move for this round. Your task is to vividly narrate the battle, clearly explaining how each player's chosen move impacts their opponent.

Each move has an effectiveness score ranging from 0 to 200 (inclusive):

An effectiveness of 0 indicates a complete miss or failure, causing no damage.

An effectiveness of 200 represents maximum damage and optimal impact.

Provide detailed context and storytelling that incorporates each player's background, chosen moves, and the resulting effectiveness. Clearly illustrate the dynamics and drama of the exchange.

Context for Player1:
{player1}
Move chosen by Player1:
{move1}

Context for Player2:
{player2}
Move chosen by Player2:
{move2}

Narrate the consequences of each player's move and describe how each player is affected. If either player's health falls below 0, declare the other player the victor and conclude with a compelling and dramatic story about their triumph.

-----

You are a battle simulator. Your task is to simulate the round as if it were a Pokemon round, but for other types of settings and players.

There are two players: Player1 and Player2. They have decided on one move each. You will simulate the effects of these moves on each player.

The effectiveness can be between 0 and 200 (inclusive). The higher the effectiveness, the more damage the move does. If the effectiveness is 0, the move does no damage (for example if it is a miss).

Here is context about Player1: {player1}, and the move they have chosen: {move1}. 

Here is context about Player2: {player2}, and the move they have chosen: {move2}.

You will simulate the effects of these moves on each player. You will provide a short story about the battle that also provides the background of the effectivness of the moves.

If one player dies (reach less than 0 health), you will declare the other player the winner, with a good story about how they won.

---------



"""

print(response)


p1 = {'name': 'Elon Musk',
      'persona': 'Elon Musk is an innovative and unpredictable entrepreneur whose ideas spark both inspiration and controversy. Known for his audacity and charisma, Musk specializes in electric energy, futuristic technology, and social media storms. He excels in surprising his opponents with unconventional tactics and rapid innovation.',
      'hp': 160,
      'move_1': {'name': 'Falcon Punch', 'description': 'Launches a rocket-powered punch, dealing electric damage.', 'dmg': 45},
      'move_2': {'name': 'Tweet Storm', 'description': 'Confuses the opponent with controversial tweets, temporarily reducing accuracy.', 'dmg': 30},
      'move_3': {'name': 'Neural Net', 'description': 'Deploys AI to predict opponent’s moves, slightly boosting his own evasion.', 'dmg': 25},
      'move_4': {'name': 'Hyperloop Dash', 'description': 'Quickly strikes with immense speed, dealing significant damage.', 'dmg': 40},
      }


p2 = {'name': 'Harry Potter',
      'persona': 'Harry Potter, the brave wizard famed for his resilience and mastery of magic, wields powerful spells and enchantments. Known for his bravery and quick thinking, Harry thrives under pressure and can summon extraordinary powers to defeat his foes.',
      'hp': 150,
      'move_1': {'name': 'Expelliarmus', 'description': 'Disarms and stuns the opponent briefly, limiting their next attack.', 'dmg': 35},
      'move_2': {'name': 'Patronus Charm', 'description': 'Summons a protective Patronus to absorb incoming damage.', 'dmg': 30},
      'move_3': {'name': 'Stupefy', 'description': 'Temporarily stuns the opponent, causing moderate magical damage.', 'dmg': 40},
      'move_4': {'name': 'Sectumsempra', 'description': 'Inflicts deep wounds, causing heavy magical damage.', 'dmg': 45},
      }


prompt =