def rotateBox(box):
    R = len(box)
    C = len(box[0])
    
    def rotate(box):
        new_box = [[None] * R for _ in range(C)]
        
        for i in range(R):
            for j in range(C):
                new_box[j][i] = box[R-i-1][j]
        return new_box
    
    rbox = rotate(box)
    R = len(rbox)
    C = len(rbox[0])
    
    for j in range(C):
        last_free = R - 1 
        
        for current in range(R - 1, -1, -1):
            match rbox[current][j]:
                case "*":
                    last_free = current - 1
                case "#":
                    # drop this to the last_free
                    rbox[current][j] = "."
                    rbox[last_free][j] = "#"
                    last_free -= 1
                case _:
                    continue
    return rbox