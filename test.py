from ai21 import AI21Client
from ai21.models.chat import ChatMessage

KEY = 'v7uBaXL8sXKB4SmHsrxIOa14sYsWPcT9'

client = AI21Client(api_key=KEY)  # or pass it in directly

response = client.chat.completions.create(
    model='jamba-large',
    messages=[ChatMessage(role='user', content='Hello, please provide a brief explanation of what AI21 does, in 100 words or less', role='assistant', content='nah!')]
)



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