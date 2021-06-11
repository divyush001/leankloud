import csv;


marksheet = open('C:\\Users\Divyush\Downloads\Student_marks_list.csv')
marksheet_reader = csv.reader(marksheet)
#print(marksheet_reader)
marksheet_lists = list(marksheet_reader)
#print(marksheet_lists)

#print(len(marksheet_lists))
no_of_students=len(marksheet_lists)
#print(no_of_students-1)
i=1
#finding the highest scorer in each subject
#finding highest scorer maths
maths_highest_score=0
mark=0
mark=int(mark)
#list(map(int, results))
while (i<no_of_students):

    try:
        #mark = int(marksheet_lists[i][1])
        mark = int(marksheet_lists[i][1])
    except ValueError as err:
        pass
    #print(mark)
    mark = int(marksheet_lists[i][1])
    #print(type(mark))
    if(mark>int(maths_highest_score)):
        maths_highest_score=marksheet_lists[i][1]
        maths_highest_scorer = marksheet_lists[i][0]
    i+=1
print("Topper in Maths "+maths_highest_scorer)

#finding highest scorer biology
#print('finding biology top scorer')
biology_highest_score=0
biology_highest_scorer=''
mark=0
mark=int(mark)
i=1
#list(map(int, results))
while (i<no_of_students):
    try:
        #mark = int(marksheet_lists[i][1])
        mark = int(marksheet_lists[i][2])
    except ValueError as err:
        pass
    #print(mark)
    mark = int(marksheet_lists[i][2])
    #print(type(mark))
    if(mark>int(biology_highest_score)):
        biology_highest_score=marksheet_lists[i][2]
        biology_highest_scorer = marksheet_lists[i][0]

    i+=1
print("Topper in Biology "+biology_highest_scorer)

#finding highest scorer English
#print('finding English top scorer')
english_highest_score=0
english_highest_scorer=''
mark=0
mark=int(mark)
i=1
#list(map(int, results))
while (i<no_of_students):
    try:
        #mark = int(marksheet_lists[i][1])
        mark = int(marksheet_lists[i][3])
    except ValueError as err:
        pass
    #print(mark)
    mark = int(marksheet_lists[i][3])
    #print(type(mark))
    if(mark>int(english_highest_score)):
        english_highest_score=marksheet_lists[i][3]
        english_highest_scorer = marksheet_lists[i][0]

    i+=1
print("Topper in English "+english_highest_scorer)

#finding highest scorer Physics
#print('finding Physics top scorer')
physics_highest_score=0
physics_highest_scorer=''
mark=0
mark=int(mark)
i=1
#list(map(int, results))
while (i<no_of_students):
    try:
        #mark = int(marksheet_lists[i][1])
        mark = int(marksheet_lists[i][4])
    except ValueError as err:
        pass
    #print(mark)
    mark = int(marksheet_lists[i][4])
    #print(type(mark))
    if(mark>int(physics_highest_score)):
        physics_highest_score=marksheet_lists[i][4]
        physics_highest_scorer = marksheet_lists[i][0]

    i+=1
print("Topper in Physics "+physics_highest_scorer)

#finding highest scorer Chemistry
#print('finding Chemistry top scorer')
chemistry_highest_score=0
chemistry_highest_scorer=''
mark=0
mark=int(mark)
i=1
#list(map(int, results))
while (i<no_of_students):
    try:
        #mark = int(marksheet_lists[i][1])
        mark = int(marksheet_lists[i][5])
    except ValueError as err:
        pass
    #print(mark)
    mark = int(marksheet_lists[i][5])
    #print(type(mark))
    if(mark>int(chemistry_highest_score)):
        chemistry_highest_score=marksheet_lists[i][5]
        chemistry_highest_scorer = marksheet_lists[i][0]

    i+=1
print("Topper in Chemistry "+chemistry_highest_scorer)

#finding highest scorer Chemistry
#print('finding Hindi top scorer')
hindi_highest_score=0
hindi_highest_scorer=''
mark=0
mark=int(mark)
i=1
#list(map(int, results))
while (i<no_of_students):
    try:
        #mark = int(marksheet_lists[i][1])
        mark = int(marksheet_lists[i][6])
    except ValueError as err:
        pass
    #print(mark)
    mark = int(marksheet_lists[i][6])
    #print(type(mark))
    if(mark>int(hindi_highest_score)):
        hindi_highest_score=marksheet_lists[i][6]
        hindi_highest_scorer = marksheet_lists[i][0]

    i+=1
print("Topper in Hindi " +hindi_highest_scorer)

#####Finding the top 3 scoreres#####
#print('Finding the top scorer')
i=1
j=1
score_sum=0
total_score = []
while(i<no_of_students):
    score_sum=0
    j=1
    while(j<7):
        score_sum += int(marksheet_lists[i][j])
        j+=1
    total_score.append(score_sum)
    marksheet_lists[i].append(score_sum)
    #print('total score : ' + str(score_sum))
    i+=1
#print(marksheet_lists)
total_score.sort(reverse=True)
#print(total_score)
top_score_1 = total_score[0]
top_score_2 = total_score[1]
top_score_3 = total_score[2]
print("Best students in class are :")
k=1
while(k<no_of_students):
   if(marksheet_lists[k][7]==top_score_1):
       print(str(marksheet_lists[k][7])+' '+ marksheet_lists[k][0])
   #print(marksheet_lists[k][7])
   k+=1

k=1
while(k<no_of_students):
   if(marksheet_lists[k][7]==top_score_2):
       print(str(marksheet_lists[k][7])+' '+ marksheet_lists[k][0])
   #print(marksheet_lists[k][7])
   k+=1

k=1
while(k<no_of_students):
   if(marksheet_lists[k][7]==top_score_3):
       print(str(marksheet_lists[k][7])+' '+ marksheet_lists[k][0])
   #print(marksheet_lists[k][7])
   k+=1
print("program end")