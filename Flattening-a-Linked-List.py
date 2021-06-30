#MEDIUM -- https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1


def flatten(root):
    #Your code here
    temp = root.next
    temp_head = root.next
    fir_nod = root
    
    while temp_head is not None:
        #print(temp_head.data)
        fir_nod = root
        while 1:
            #print(temp.data)
            if root.data > temp.data:
                tt = temp.bottom
                temp.bottom = root
                root = temp
                temp = tt
                if temp is None:
                    break
                
            
            if fir_nod.bottom is None:
                tt = temp.bottom
                fir_nod.bottom = temp
                temp.bottom = None
                temp = tt
                fir_nod = root
                if temp is None:
                    break
                #break
            
            elif fir_nod.bottom.data <= temp.data:
                fir_nod = fir_nod.bottom
            else:
                tt = temp.bottom
                pp = fir_nod.bottom
                fir_nod.bottom = temp
                temp.bottom = pp
                temp = tt
                if tt is None:
                    break
                
        
        temp_head = temp_head.next
        temp = temp_head
        
    return root

