class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        num=0
        currstr=""
        ans=""
        #[3,"",2,""]
        for i in s:
            if i.isdigit():
                num=num*10+int(i)
            elif i=="[":
                stack.append(currstr)
                stack.append(num)
                num=0
                currstr=""
            elif i=="]":
                print(stack)
                stacknum=stack.pop()
                strn=stack.pop()
                
                currstr=strn+stacknum*currstr
                print(currstr)
            else:
                currstr+=i
        return currstr
                
#3[a]2[bc]   
#3[a2[c]]