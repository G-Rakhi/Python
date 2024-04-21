class Node:
    def __init__(self,d):
        self.lc=None
        self.rc=None
        self.d=d
        self.hd=0
def topView(root):
    m={}
    q=[root]
    while q:
        curr_node=q.pop(0)
        if curr_node.hd not in m:
            m[curr_node.hd]=curr_node.d
            if curr_node.lc:
                curr_node.lc.hd=curr_node.hd-1
                q.append(curr_node.lc)
            if curr_node.rc:
                curr_node.rc.hd=curr_node.hd+1
                q.append(curr_node.rc)
    print("Top View")
    for i in sorted(m):
        print(m[i],end=' ')
        
#Driver Code
root=Node('A')
root.lc=Node('B')
root.rc=Node('C')
root.lc.lc=Node('D')
root.lc.rc=Node('E')
root.rc.lc=Node('F')
root.rc.rc=Node('G')

topView(root)















