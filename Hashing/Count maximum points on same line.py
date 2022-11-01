''' 
-> calc. Slope of each point and store in map. Elements with same slope are in same line.
-> return the slope with maximum points.
'''

class Solution:
   def slopeMaxElements(self, points: List[int], k: int) -> int:
       d = {}   
       for i in points:
           x = i[0]
           y = i[1]
           slope = (y-0)/(x-0)
           if slope in d:
               d[slope] += 1
           else:
               d[slope] = 1
              
       return max(d.values())
