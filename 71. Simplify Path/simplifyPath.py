class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        n = len(path)
        name, dot_count = "", 0
        i = 1
        while i < n:
            if path[i] == "/":
                if name == ".":
                    name = ""
                elif name == "..":
                    if len(stack) > 0:
                        stack.pop()
                else:
                    if name != "":
                        stack.append(name)
                name = ""
                #print("STACK: ", stack)
            else:
                name += path[i]
                #print("name: ", name)
            i += 1
        name = ''.join(name.split('/'))
        if len(name)>0:
            if name == ".":
                pass
            elif name == "..":
                if len(stack)>0:
                    stack.pop()
                else:
                    pass
            else:
                stack.append(name)
        #print(stack)
        return '/' if len(stack) == 0 else '/' + '/'.join(stack)
