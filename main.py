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

def generate_declansion(nouns, adjectives, ending, sentence_start_ge, sentence_start_en, add_n_to_noun=False):
  result = []
  for noun in nouns:
    noun_transformed = noun
    if add_n_to_noun and noun[-1] != 'n' and noun[-1] != 's':
      noun_transformed += 'n'
    for adjective in adjectives:
      german = f'{sentence_start_ge} {adjective}{ending} {noun_transformed}'
      english = f'{sentence_start_en} {translations[adjective]} {translations[noun]}'
      result.append(f'{german}: \t{english}')
  return result

def main(args):
  result = []

  # Strong declansion
  # Nominativ
  result += generate_declansion(nouns_male, adjectives, 'er', 'es gibt', 'there is')
  result += generate_declansion(nouns_neuter, adjectives, 'es', 'es gibt', 'there is')
  result += generate_declansion(nouns_female, adjectives, 'e', 'es gibt', 'there is')
  result += generate_declansion(nouns_plural, adjectives, 'e', 'es gibt', 'there are')
  # Akkusativ
  result += generate_declansion(nouns_male, adjectives, 'en', 'Tieren fressen', 'I see')
  result += generate_declansion(nouns_neuter, adjectives, 'es', 'Tieren fressen', 'I see')
  result += generate_declansion(nouns_female, adjectives, 'e', 'Tieren fressen', 'I see')
  result += generate_declansion(nouns_plural, adjectives, 'e', 'Tieren fressen', 'I see')
  # Dativ
  result += generate_declansion(nouns_male, adjectives, 'em', 'ich bin mit', 'I\'m with')
  result += generate_declansion(nouns_neuter, adjectives, 'em', 'ich bin mit', 'I\'m with')
  result += generate_declansion(nouns_female, adjectives, 'er', 'ich bin mit', 'I\'m with')
  result += generate_declansion(nouns_plural, adjectives, 'en', 'ich bin mit', 'I\'m with', add_n_to_noun=True)

  # Weak declansion
  # Nominativ
  result += generate_declansion(nouns_male, adjectives, 'e', 'da ist der', 'there is the')
  result += generate_declansion(nouns_neuter, adjectives, 'e', 'da ist das', 'there is the')
  result += generate_declansion(nouns_female, adjectives, 'e', 'da ist die', 'there is the')
  result += generate_declansion(nouns_plural, adjectives, 'en', 'da sind die', 'there are the')
  # Akkusativ
  result += generate_declansion(nouns_male, adjectives, 'en', 'ich habe den', 'I have the')
  result += generate_declansion(nouns_neuter, adjectives, 'e', 'ich habe das', 'I have the')
  result += generate_declansion(nouns_female, adjectives, 'e', 'ich habe die', 'I have the')
  result += generate_declansion(nouns_plural, adjectives, 'en', 'ich habe die', 'I have the')
  # Dativ
  result += generate_declansion(nouns_male, adjectives, 'en', 'ein Leben mit dem', 'a life with the')
  result += generate_declansion(nouns_neuter, adjectives, 'en', 'ein Leben mit das', 'a life with the')
  result += generate_declansion(nouns_female, adjectives, 'en', 'ein Leben mit die', 'a life with the')
  result += generate_declansion(nouns_plural, adjectives, 'en', 'ein Leben mit die', 'a life with the', add_n_to_noun=True)

  # Mixed declansion
  # Nominativ
  result += generate_declansion(nouns_male, adjectives, 'er', 'das ist ein', 'that is a')
  result += generate_declansion(nouns_neuter, adjectives, 'es', 'das ist ein', 'that is a')
  result += generate_declansion(nouns_female, adjectives, 'e', 'das ist eine', 'that is a')
  result += generate_declansion(nouns_plural, adjectives, 'en', 'hier sind keine', 'there are no')
    # Akkusativ
  result += generate_declansion(nouns_male, adjectives, 'en', 'ich brauche einen', 'I need a')
  result += generate_declansion(nouns_neuter, adjectives, 'es', 'ich brauche ein', 'I need a')
  result += generate_declansion(nouns_female, adjectives, 'e', 'ich brauche eine', 'I need a')
  result += generate_declansion(nouns_plural, adjectives, 'en', 'ich brauche keine', 'I don\'t need')
  # Dativ
  result += generate_declansion(nouns_male, adjectives, 'en', 'ein Leben mit einem', 'a life with a')
  result += generate_declansion(nouns_neuter, adjectives, 'en', 'ein Leben mit einem', 'a life with a')
  result += generate_declansion(nouns_female, adjectives, 'en', 'ein Leben mit einer', 'a life with a')
  result += generate_declansion(nouns_plural, adjectives, 'en', 'ein Leben mit keinen', 'a life without', add_n_to_noun=True)

  for entry in result:
    print(entry)


if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
