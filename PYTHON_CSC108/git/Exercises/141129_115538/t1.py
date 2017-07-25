def our_swapcase(s):
   '''(str) -> str
      Return a copy of the string s with uppercase letters converted to lowercase, and lowercase letters converted to uppercase.'''
   
   new_str = ""
   for letter in s:
      if letter.isupper():
         new_str += letter.lower()
      else:
         new_str += letter.upper()
   return new_str

def length_dict(word_list):
   
   new_dict = {}
   #key = word length
   #value = lst of the words
   #[apple, bee, cook]
   for word in word_list:
      if len(word) in new_dict:
         new_dict[len(word)].append(word)
      else:
         new_dict[len(word)] = [word]
   return new_dict


#a)
def invert_book_to_people(book_to_people):
   
   person_to_books  = {}
   for book in book_to_people:
      for person in book_to_people[book]:
         if person in person_to_books:
            person_to_books[person].append(book)
         else:
            person_to_books[person] = [book]
   return person_to_books










def make_recommendations(book_to_people, book):

#      {'
#        Tresure Island' : ['Joanna', 'Jonathan', 'Hui', "Ali'], 
#      ' Wuthering heights': ['Hui', 'Monia', 'Ali' ],
#        'Middlemarch' : ['Vlad', 'Ali']}
   
   recommend_dict = {}
# { 'Trasure Isaland': 2 'Middlemarch': 1}

   people_to_book = invert_book_to_people(book_to_people)
#  {  'Roy': ['a',b'...]
#     'Hui': ['Tresu Isand', 'Wuthering Heights] }
#     ...
#  }

   
   for people in book_to_people[book]:
   #            ['Hui', 'Monia', 'Ali' ]

      book_read_by_people = people_to_book[people]
      #------------------
     #  ['Tresu Isand', 'Wuthering Heights]


      for each_book in book_read_by_people:
         if each_book != book
            # recommended already
            if each_book in recommend_dict:
               recommend_dict[each_book] += 1
            # recommed first
            else:
               recommend_dict[each_book] = 1

   return recommend_dict
