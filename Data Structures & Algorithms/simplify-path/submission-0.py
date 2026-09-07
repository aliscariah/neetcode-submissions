class Solution:
    def simplifyPath(self, path: str):
        words=path.split("/")
        stack=[]
        i=0
        while i < len(words):
            if words[i]=="" or words[i]==".":
                pass
            
            elif words[i] == ".." :
                if stack:
                    stack.pop()
            
            else:
                stack.append(words[i])
            i+=1

        output=""
        if stack :
            for st in stack:    
                output+="/"+st
        else:
            return "/"

        return output

        
        