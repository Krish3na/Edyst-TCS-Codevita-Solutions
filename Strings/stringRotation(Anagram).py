'''
String Rotation
String Rotation
Rotate a given String in the specified direction by specified magnitude.

After each rotation make a note of the first character of the rotated String, After all rotation are performed the accumulated first character as noted previously will form another string, say FIRSTCHARSTRING.

Check If FIRSTCHARSTRING is an Anagram of any substring of the Original string.

If yes print YES otherwise NO.

Input
The first line contains the original string s.
The second line contains a single integer q.
The ith line of the next q lines contains character d[i] denoting direction and integer r[i] denoting the magnitude.
Output
YES or NO

Constraints
1 <= Length of original string <= 30
1<= q <= 10
Sample Input & Output
Input

carrace
3
L 2
R 2
L 3

Output

NO

Explanation

After applying all the rotations the FIRSTCHARSTRING string will be rcr which is not anagram of any sub string of original string carrace
'''

def countchars(s):
    dic={}
    for i in s:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    return dic

def arecountsEqual(s1,s2):
    for i in s1:
        if i not in s2 or s1[i]!=s2[i]:
            return False
    return True

def isanagram(s,fs):
    if len(fs)>len(s):
        return False
    countfs=countchars(fs)
    for i in range(0,len(s)-len(fs)):
        window=s[i:i+len(fs)]
        countwin=countchars(window)
        
        if arecountsEqual(countwin,countfs):
            return True
    return False


string=input()
n=int(input())
firstchars=[]
idx=0
for i in range(n):
    dir,s=input().strip().split()
    s=int(s)
    if dir=='L':
        idx=(idx+s)%len(string)
    else:
        idx=(idx-s)%len(string)
                     
    firstchars.append(string[idx])
    
if isanagram(string,firstchars):
    print('YES')
else:
    print('NO')

    
