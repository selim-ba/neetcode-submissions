class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # Version1 - Simple double loop brute force works for 38/39 test cases
        #max_area = 0
        #for i in range(0,len(heights)):
        #    p_1 = heights[i]
        #    for j in range(1,len(heights)):
        #        p_2 = heights[j]
        #        current_distance = j-i
        #        current_height = min(p_1,p_2)
        #        current_max = current_distance*current_height
        #        if current_max > max_area:
        #            max_area = current_max
        #return max_area

        # Version 2 - two pointer
        i = 0
        j = len(heights)-1
        max_area = 0
        while (i < len(heights)) and (j > 0):
            p_1 = heights[i]
            p_2 = heights[j]
            current_distance = j-i
            current_max = current_distance * min(p_1,p_2)
            #print(i,j,p_1,p_2,current_distance,current_max,max_area)
            if current_max > max_area:
                max_area = current_max
            if p_1 < p_2:
                i += 1
            else:
                j -= 1
        return max_area
                



                

        