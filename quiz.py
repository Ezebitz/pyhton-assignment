print('welcome to ask python quiz')

answer=input('Are you ready to play the quiz?:(yes/no)') 
score=0
total_questions=0
if Answer.lower()=='yes':
   Answer=input ('Question 1:what is your favorite programming\"language')
   if Answer.lower()=='python':
           score += 1
           print("correct")

   else:
           print('wrong Answer:(')
           Answer=input('Question 2:Do you follow any Author on AskPython?')

   if Answer.lower()=='yes':
           score+=1
   
           print ('correct')
   else: 
           print ('wrong:(')
   Answer=input('Question 3:What is your favourite website for python programming')
   if Answer.lower()=='AskPython':
           score+=1
           print ('correct')
   else:
           print ('wrong:(')
print ('Thank you for playing this small quiz game,you attempted',score, "questions correctly")
mark=(scores/questions)*100;
print('mark obtained:',mark)
print('bye')

