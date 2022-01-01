class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        print(rec1[0])
        x1=rec1[0]
        y1=rec1[1]
        x2=rec1[2]
        y2=rec1[3]
        x3=rec2[0]
        y3=rec2[1]
        x4=rec2[2]
        y4=rec2[3]
        """

                   ____________________x4,y4
                  |                   |
           _______|______x2,y2        |
          |       |______|____________|
          |      x3,y3   |
          |______________|
         x1,y1

        """
        if x1<x4 and x3<x2 and y1<y4 and y3<y2:
            return True
        return False