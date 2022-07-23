import sys
from enum import Enum

class Declansion(Enum):
  STRONG = 1
  WEAK = 2
  MIXED = 3

class Gener(Enum):
  MALE = 1
  FEMALE = 2
  NEUTER = 3
  PLURAL = 4

demonstrative_pronouns = {
  'dies',
}

indefinite_articles = {
  'ein',
  'kein',
}

possessive_pronouns = {
  'mein',
  'dein',
  'sein',
  'Ihr',
  'sein',
  'unser',
  'eur',
  'ihr',
}

nouns_male = {
  'Apfel',
  'Arzt',
  'Beruf',
  'Brief',
  'Bus',
  'Bruder',
  'Garten',
  'Kuchen',
  'Mund',
  'Regen',
  'Saft',
  'Tag',
  'Tisch',
  'Vater',
  'Zug',
}

nouns_female = {
  'Bahn',
  'Firma',
  'Arbeit',
  'Küche',
  'Tasche',
  'Tomate',
  'Toilette',
  'Woche',
  'Zeitung',
  'Bank',
  'Banane',
  'Birne',
  'Blume',
  'Dame',
  'Flasche',
}

nouns_neuter = {
  'Foto',
  'Essen',
  'Dorf',
  'Datum',
  'Buch',
  'Bild',
  'Bad',
  'Auto',
  'Lied',
  'Gepäck',
  'Glas',
  'Glück',
  'Haus',
  'Hotel',
  'Konto',
}

nouns_plural = {
  'Äpfel',
  'Berufe',
  'Briefe',
  'Busse',
  'Brüder',
  'Arbeiten',
  'Taschen',
  'Tomaten',
  'Toiletten',
  'Bananen',
  'Fotos',
  'Dörfer',
  'Bücher',
  'Bilder',
  'Lieder',
}

adjectives = {
  'groß',
  'klein',
  'lang',
  'kurz',
  'gut',
  'schlecht',
  'kalt',
  'heiß',
}

translations = {
  'dies': 'this',
  'ein': 'a',
  'kein': 'no',
  'mein': 'my',
  'dein': 'your (informal)',
  'sein': 'his',
  'Ihr': 'your (formal)',
  'sein': 'his',
  'unser': 'our',
  'eur': 'your (plural informal)',
  'Apfel': 'apple',
  'Arzt': 'doctor',
  'Beruf': 'profession',
  'Brief': 'letter',
  'Bus': 'bus',
  'Bruder': 'brother',
  'Garten': 'garden',
  'Kuchen': 'pie',
  'Mund': 'mouth',
  'Regen': 'rain',
  'Saft': 'juice',
  'Tag': 'day',
  'Tisch': 'table',
  'Vater': 'father',
  'Zug': 'train',
  'Bahn': 'subway train',
  'Firma': 'firm',
  'Arbeit': 'job',
  'Küche': 'kitchen',
  'Tasche': 'bag',
  'Tomate': 'tomato',
  'Toilette': 'toilet',
  'Woche': 'week',
  'Zeitung': 'newspaper',
  'Bank': 'bank',
  'Banane': 'banana',
  'Birne': 'pear',
  'Blume': 'flower',
  'Dame': 'lady',
  'Flasche': 'bottle',
  'Foto': 'photo',
  'Essen': 'food',
  'Dorf': 'village',
  'Datum': 'date',
  'Buch': 'book',
  'Bild': 'picture',
  'Bad': 'bath',
  'Auto': 'car',
  'Lied': 'song',
  'Gepäck': 'luggage',
  'Glas': 'glass',
  'Glück': 'luck',
  'Haus': 'house',
  'Hotel': 'hotel',
  'Konto': 'account',
  'Äpfel': 'apples',
  'Berufe': 'professions',
  'Briefe': 'letters',
  'Busse': 'busses',
  'Brüder': 'brothers',
  'Arbeiten': 'jobs',
  'Taschen': 'bags',
  'Tomaten': 'tomatoes',
  'Toiletten': 'toilets',
  'Bananen': 'bananas',
  'Fotos': 'photos',
  'Dörfer': 'villages',
  'Bücher': 'books',
  'Bilder': 'pictures',
  'Lieder': 'songs',
  'groß': 'big',
  'klein': 'small',
  'lang': 'long',
  'kurz': 'short',
  'gut': 'good',
  'schlecht': 'bad',
  'kalt': 'cold',
  'heiß': 'hot',
}

def main(args):
  result = []
  # Strong declansion
  # Nominativ
  # Male
  for noun in nouns_male:
    for adjective in adjectives:
      german = '{}er {}'.format(adjective, noun)
      english = '{} {}'.format(translations[adjective], translations[noun])
      result.append('{}: \t{}'.format(german, english))
  # Female
  for noun in nouns_female:
    for adjective in adjectives:
      german = '{}e {}'.format(adjective, noun)
      english = '{} {}'.format(translations[adjective], translations[noun])
      result.append('{}: \t{}'.format(german, english))
  # Neuter
  for noun in nouns_neuter:
    for adjective in adjectives:
      german = '{}es {}'.format(adjective, noun)
      english = '{} {}'.format(translations[adjective], translations[noun])
      result.append('{}: \t{}'.format(german, english))

  for entry in result:
    print(entry)


if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
