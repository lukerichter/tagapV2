# Keys for the incoming csv dict
NAME = 'Name'
SCHOOL = 'Schule'
GENDER = 'Geschlecht'
BIRTH_DATE = 'Geb. Datum'
HEIGHT = 'Größe'

AGILITY = ['Rumpf']
THROWING = ['Ball 1', 'Ball 2', 'Ball 2']
JUMPING = ['Stand 1', 'Stand 2']
SPRINTING = ['Sprint 1', 'Sprint 2']
COORDINATION = ['Koordination']
ENDURANCE = ['Ausdauer']

# Keys for the outgoing csv dict
OUT_NAME = 'Name'
OUT_SCHOOL = 'Schule'
OUT_GENDER = 'Geschlecht'
OUT_AGE = 'Alter'
OUT_HEIGHT = 'Größe'
OUT_AGILITY = 'Rumpf'
OUT_AGILITY_POINTS = 'Rumpf Pkt.'
OUT_THROWING = 'Ball'
OUT_THROWING_POINTS = 'Ball Pkt.'
OUT_JUMPING = 'Stand'
OUT_JUMPING_POINTS = 'Stand Pkt.'
OUT_SPRINTING = 'Sprint'
OUT_SPRINTING_POINTS = 'Sprint Pkt.'
OUT_COORDINATION = 'Koordination'
OUT_COORDINATION_POINTS = 'Koordination Pkt.'
OUT_ENDURANCE = '8-Min'
OUT_ENDURANCE_POINTS = '8-Min-Pkt.'
OUT_SUM = 'Gesamt'

# Strings that represent the gender
MALE = 'm'
FEMALE = 'w'

# Lists of possible strings that represent the gender
GENDER_MALE_LIST = ['m', 'mann', 'männlich', 'male']
GENDER_FEMALE_LIST = ['f', 'frau', 'w', 'weiblich', 'female']

# List of possible strings that represent invalid values
INVALID_VALUES = ['-', '/', '', 'f', 'u']
INVALID_CHAR = '-'
INVALID_HIGH = float('inf')
INVALID_LOW = float('-inf')
