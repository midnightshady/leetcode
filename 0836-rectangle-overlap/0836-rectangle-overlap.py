class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        
        # rec2 is completely right of rec1
        if rec2[0] >= rec1[2]:
            return False
        
        # rec2 is completely left of rec1
        if rec2[2] <= rec1[0]:
            return False
        
        # rec2 is completely above rec1
        if rec2[1] >= rec1[3]:
            return False
        
        # rec2 is completely below rec1
        if rec2[3] <= rec1[1]:
            return False
        
        return True