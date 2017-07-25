# def load_addresses(numbers_file):
# 
#    #address_list = []
#    #final_list = []
#    #for line in numbers_file.readline():
#    #   line = line.split(" ")
#    #   address_list.append(line[0])
#    #   line.remove(line[0])
#    #   address_list.append(line[-1])
#    #   line.remove(line[-1])
#    #   address_list.insert(line, 1)
#    #final_list.append(address_list)
# 
#    final_list = []
#    for line in numbers_file.readline():
#       line=line.strip()
#       address_list = []
#       words = line.split()
#       address_list.append(word[0])
#       for each in range(1,len(words)-1)
#          each=each.strip()
#          address_list.append(each)
#       address_list.append(word[-1])
# 
# 
# 
#    final_list.append(address_list)

        
def longest_sequence(r):

   biggest = 0
   count = 0


   for each_line in r:
      each_line = each_line.strip()
      if len(each_line) == 0:
         count += 1
      else:
         if biggest < count:
            biggest = count
         count = 0

   if biggest < count:
         biggest = count
   return biggest





r=open("t2.txt","r")
print(longest_sequence(r))


def get_word_list(word_file):
   
   clean_list = []
   for each_line in word_file:
      each_line = each_line.strip()
      clean_list.append(each_line)
   return clean_list


def a():

   file1=open("t3.txt","w")

   file1.write("hello1\n")  
   file1.write("hello2\n")  
   file1.write("hello3\n")  
   file1.write("hello4\n")  
   file1.write("hello5\n")  



a()



c



lass Card:

   def __init__(self):
      















