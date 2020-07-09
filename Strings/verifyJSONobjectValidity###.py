'''
Codevita [2016] Verify JSON Object Validity
Verify JSON Object validity
A JSON object is a key-value pair data structure that is enclosed within { }. A sample JSON object would look like

{
"key1":"value1",
"key2":"value2",
"key3": {
"key4":"value4",
"key5":"value5"},
"key6":"value6",
"key7":[
{
"key8":"value8"
}]
}
Given a JSON object, ignore the literal values of the object and check whether the distinguishing characters and notation of the object are valid to determine if the JSON object is valid or not.

Note:

Key3 points to another JSON object (Concept of nesting of JSON objects).
Key7 points to an array of JSON objects.
You may wish to refer JSON.org to get a more formal description of JSON grammar.
Input Format
First line contains a pattern of JSON without any literal
Output Format:
Print 1 if pattern is valid, -1 otherwise.

Constraints:
A JSON object should start with { and ends with a }.
The key and value should be separated by a :.
A , suggests an additional JSON property.
An array only consists of JSON objects. It cannot contain a “key”:“value” pair by itself.
Sample Input & Output
Input
{:[{},{}]}

Output
1

Explanation

{
"Key": [{
"Key": "Value"
}, {
"Key": "Value"
}]
}
Pattern is following all constraints hence prints 1

Input
{:{[]},{}}

Output
-1

Explanation

{
"Key": {
[
"Key": "Value"
]
},
{
"Key": "Value"
}
}
Constraint 4 “An array only consists of JSON objects. It cannot contain a “key”:“value” pair by itself.” not followed here, so it’s a invalid pattern, hence prints -1

'''

def check(s):
    end=0
    start=0
    if s[0]!='{' or s[-1]!='}':
        print(-1)
        return
    for i in range(1,len(s)):
        if s[i]=='{':
            start = i
            for j in range(i+1,len(s)):
                if s[j]=='}':
                    end = j
                    break
            if end==0:
                print(-1)
                return
            ll=s[start:end+1]
            #print(ll)
            
            if '[' in ll :
                if ':' not in ll:
                    print(-1)
                    return
            end=0
            start=0


    else:
        print(1)
        return



s = input().strip()
#s='{:{[]},{}}'# -1
#s='{:{},:[{},{},{}],:[]}'# 1
#s='{:{:{:[{},{}]}}}' #1
#print(s)
check(s)

