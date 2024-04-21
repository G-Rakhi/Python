class Node:
    def __init__(self,d):
        self.lc=None
        self.rc=None
        self.d=d
        
def left_right_View(root,side):
    if not root:
        return {}
    result={}
    q=[(root,0)]
    while q:
        node, level=q.pop(0)
        if level not in result:
            result[level]=[]
        result[level].append(node.d)
        if node.lc:
            q.append((node.lc,level+1))
        if node.rc:
            q.append((node.rc,level+1))
    if side=='L':
        print("Left View")
    else:
        print("\nRight View")
    for k in result.keys():
        if side=='L':
            print(result[k][0],end=' ')
        elif side=='R':
            print(result[k][-1],end=' ')
        
#Driver Code
root=Node('A')
root.lc=Node('B')
root.rc=Node('C')
root.lc.lc=Node('D')
root.lc.rc=Node('E')
root.rc.lc=Node('F')
root.rc.rc=Node('G')
root.rc.rc.lc=Node('H')

left_right_View(root,'L')
left_right_View(root,'R')




