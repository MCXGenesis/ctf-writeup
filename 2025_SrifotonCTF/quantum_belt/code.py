import sys

def exit():
    sys.exit(0)

def advanced_scramble(L):    
    A = L[:] 
    i = 2
    
    while i < len(A):
        if i-1 < len(A):
            popped = A.pop(i-1)
            
            enhanced_popped = {
                'data': popped,
                'pop_index': i-1,
                'iteration': i-2
            }
            
            if i-2 < len(A):
                if isinstance(A[i-2], list):
                    A[i-2].append(enhanced_popped)
                else:
                    A[i-2] = [A[i-2], enhanced_popped]
        
        if i-1 < len(A):
            slice_data = A[:i-2]  
            enhanced_slice = {
                'slice': slice_data,
                'slice_end': i-2,
                'append_to': i-1
            }
            
            if isinstance(A[i-1], list):
                A[i-1].append(enhanced_slice)
            else:
                A[i-1] = [A[i-1], enhanced_slice]
        
        i += 1
    
    return A

def get_flag():
    flag = open('flag.txt', 'r').read()
    flag = flag.strip()
    
    hex_flag = []
    for i, c in enumerate(flag):
        char_data = {
            'hex': str(hex(ord(c))),
            'pos': i,
            'char': c  
        }
        hex_flag.append([char_data])  
    
    return hex_flag

def main():
    flag_data = get_flag()
    scrambled = advanced_scramble(flag_data)
    print(scrambled)

if __name__ == '__main__':
    main()
