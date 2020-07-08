'''
CodeVita 2016, Exam Efficiency
Exam Efficiency
In an examination with multiple choice questions, the following is the exam question pattern.

X1 number of One mark questions, having negative score of -1 for answering wrong
X2 number of Two mark questions, having negative score of -1 and -2 for one or both options wrong
X3 number of Three mark questions, having negative score of -1, -2 and -3 for one, two or all three options wrong
Score Required to Pass the exam : Y
For 1,2 and 3 mark questions, 1,2 and 3 options must be selected. Simply put, once has to attempt to answer all questions against all options.
Identify the minimum accuracy rate required for each type of question to crack the exam.

Calculations must be done up to 11 precision and printing up to 2 digit precision with ceil value

Input Format:
First line contains number of one mark questions denoted by X1,
Second line contains number of two mark questions denoted by X2
Third line contains number of three mark questions denoted by X3
Fourth line contains number of marks required to pass the exam denoted by Y.
Output Format:
Minimum Accuracy rate required for One mark question is 80%
Minimum Accuracy rate required for Two mark question is 83.33%
Minimum Accuracy rate required for Three mark question is 90%
Note:- If the mark required to pass the exam can be achieved by attempting without attempting any particular type of question then show message similar to, One mark question need not be attempted, so no minimum accuracy rate applicable

See Example Test cases for better understanding.

Sample Input / Output
Input	Output	Explanation
20
30
30
120	One mark questions need not be attempted, so no minimum accuracy rate applicable.
Minimum Accuracy rate required for Two mark question is 58.33%
Minimum Accuracy rate required for Three mark question is 72.23%	If one got full marks in two marks question and three marks question then total accuracy can be 0 in one mark question
In same way it will be done for two marks and three marks question
20
30
30
170	Minimum Accuracy rate required for one mark question is 100%
Minimum Accuracy rate required for Two mark question is 100%
Minimum Accuracy rate required for Three mark question is 100%	If one got full marks in two marks question and three marks question then total accuracy should be 100% in one mark question to pass the exam.
In same way it will be done for two marks and three marks question

'''

x1=int(input())
x2=int(input())
x3=int(input())
y=int(input())

#sections
y1=(2*x2)+(3*x3)
y2=x1+(3*x3)
y3=x1+(2*x2)

if y1==y-x1 and y2==y-(2*x2) and y3==y-(3*x3):
    print('Minimum Accuracy rate required for One mark question is 100%')
    print('Minimum Accuracy rate required for Two mark question is 100%')
    print('Minimum Accuracy rate required for Three mark question is 100%')
    exit(0)
    

if y1>=y:
    print('One mark question need not be attempted, so no minimum accuracy rate applicable')
else:
    marksleft=y-y1
    #m-(x1-m)>=marksleft and acc=100*m/x1
    acc = ((marksleft + x1)/(x1))*50
    acc="{:.2f}".format(acc)
    if acc[-2:]=="00":
        acc=int(float(acc))
    print(f'Minimum Accuracy rate required for One mark question is {acc}%')
if y2>=y:
    print('Two mark question need not be attempted, so no minimum accuracy rate applicable')
else:
    marksleft=y-y2
    #2m-2(x2-m)>=marksleft and acc=100*m/x2
    acc = ((marksleft + (2*x2))/(x2))*25
    acc="{:.2f}".format(acc)
    if acc[-2:]=="00":
        acc=int(float(acc))
    print(f'Minimum Accuracy rate required for Two mark question is {acc}%')

if y3>=y:
    print('Three mark question need not be attempted, so no minimum accuracy rate applicable')
else:
    marksleft=y-y3
    #3m-3(x3-m)>=marksleft and acc=100*m/x3
    acc = ((marksleft + (3*x3))/(x3))*(100/6)
    acc="{:.2f}".format(acc)
    if acc[-2:]=="00":
        acc=int(float(acc))
    print(f'Minimum Accuracy rate required for Three mark question is {acc}%')

'''
Exam Efficiency [Editorial]
Simple Case 1

Let’s first analyse a simpler version of this question, where there are only X1 number of One mark questions, with a negative score of -1 if we get one wrong. The student needs Y marks to pass the exam.

Had there been no negative marking, the student would need to solve atleast Y number of questions correctly, and thus, the minimum required accuracy would be: 100 * ( Y / X1 )

Now, because there is negative marking, each question we answer incorrectly will reduce our score. Suppose the student needs to answer M questions correctly. The marks he’ll score are: M - (X1-M) (since he receives -1 marks for the remaining incorrect answers). To pass, his marks have to be >= Y

Which means,

M - (X1 - M) >= Y, or
 
2M >= Y + X1, or
 
M >= (Y + X1)/2
Which means, the minimum accuracy required becomes 100 * (M/X1) where M is calculated as above.

Simple Case 2

Let us look at a slightly harder version of the previous case next, with 2 types of questions. X1 number of One mark questions, with -1 negative scoring, and X2 number of Two mark questions, with -1, -2 as possible negative scoring. Student needs Y marks to pass.

Note:- If the mark required to pass the exam can be achieved by attempting without attempting any particular type of question then show message similar to, One mark question need not be attempted, so no minimum accuracy rate applicable.**

What is the minimum number of One mark questions the student has to answer to pass?

Consider the scenario, where the student answers ALL Two mark questions correctly. He scores 2*X2 marks from these 2 mark questions (since in the exam, a student has to answer all questions).

If Y <= 2*X2, it means that, in the best case, a student can answer all 2 mark questions correctly and hit the pass marks. According to the question, if such a scenario is possible, then we say “One mark question need not be attempted, so no minimum accuracy rate applicable.”.

However, if Y > 2*X2, it means that even in the best case scenario, he will still need to score the remaining Y - 2*X2 marks from the One mark section.

In that case, the minimum accuracy for the one mark questions can be calculated as demonstrated in the Simple Case 1 example discussed above, the difference being, here, instead of Y, the student has to score Y - 2*X2 marks.

To calculate minimum accuracy required for Two marks questions, again assume the best case scenario for the One mark questions, i.e. The student gets all of the One mark questions right! If we can hit the pass mark just by getting all the One mark questions right, according to the question, minimum accuracy rate is not applicable to the Two mark question section.

However, even after answering all X1 One mark questions correctly, if Y > X1, then we are left with Y - X1 marks to pass.

Let M be the number of Two mark questions that the student needs to attempt correctly to pass with the remaining marks (it means that he has incorrectly answered X2 - M questions. Now, in the worst case, the student gets -2 for each wrong answer, which means, to pass the equation now becomes:

student marks in two marks section = 2*M - 2*(X2-M)
 
To pass, this has to be >= (Y - X1)
 
or, 2*M - 2*X2 + 2*M >= Y - X1
 
or, M >= (Y - X1 + 2*X2) / 4
 
and thus, minimum accuracy rate of Two mark questions becomes 100 * (M/X2)
Actual question

Now, coming back to the actual question, here are the major patterns.

To calculate minimum accuracy rate of any section,

First (step 1), assume you can score maximum marks in the other two sections.
Check if you can pass the exam by doing just the above, in that case, no minimum accuracy is required for this section.
Else, assume you need M correctly solved questions in this section at a minimum to pass the exam. These M questions will have to earn you whatever marks were remaining to pass in step 1.
This means, X - M questions in this section of X questions will be solved incorrectly.
Assume the worst, and imagine getting the maximum penalty for each wrong answer.
Calculate M for which you can score the marks remaining after step 1.
To quickly work this through, let’s take the example given in the question:

X1 = 20, X2 = 30, X3 = 30
 
Y = 120
Consider the X1 section.

If we get all X2, X3 right, we can score 2*30 + 3*30 = 150 >= Y marks, which means minimum accuracy is not applicable to this X1 section.

Consider the X2 section,

If we get all X1, X3 right, we can score 1*20 + 3*30 = 110 marks, to pass we need 120 which means, at a minimum we need to score 10 marks in X2. Assuming we need M questions in this section, and we do the worst on all our incorrect questions in this section, we need 2*M - 2*(X2-M) >= 10 or 2*M -2*(30-M) >= 10.

This makes M >= 70/4, and the minimum accuracy becomes 100 * (M/X2), or, 100 * (70/4) * (1/30) = 58.3333...

Consider the X3 section,

If we get all X1, X2 right, we can score 1*20 + 2*30 = 80 marks, which means we need to score at least 40 marks in X3 to pass. Analysing the situation in a similar way,

3*M - 3*(X3-M) >= 40 or, 3*M - 3*(30-M) >= 40 or, M >= (130/6), which means, the minimum accuracy required in this section is 100 * (M/X3) = 100 * (130/6) * (1/30) = 72.2222...

All that remains is to print these percentages according to the format specified in the question!
'''
