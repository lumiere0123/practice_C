training_file = open('story.txt', 'r')

story = training_file.read().split()
print(story)

training_file.close()