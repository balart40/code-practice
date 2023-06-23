class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        # brute force 132 / 160
        """
        session = 0
        total_hire_cost = 0
        while session < k:
            #print "session "+str(session)
            #print costs
            # create heaps
            left_right = []
            if len(costs) < candidates:                
                for i in range(len(costs)):
                    heapq.heappush(left_right, (costs[i], i))
                candidate = heapq.heappop(left_right)
                total_hire_cost += candidate[0]
                costs.pop(candidate[1])
            else:        
                left = []
                right = []
                for i in range(candidates):
                    heapq.heappush(left, (costs[i], i))
                    heapq.heappush(right, (costs[len(costs) - i -1],len(costs) - i -1))
                left_candidate = heapq.heappop(left)
                right_candidate = heapq.heappop(right)
                if left_candidate[0] <= right_candidate[0]:
                    #print "left: "+str(left_candidate[0])
                    total_hire_cost += left_candidate[0]
                    costs.pop(left_candidate[1])
                else:
                    #print "right: "+str(right_candidate[0])
                    total_hire_cost += right_candidate[0]
                    costs.pop(right_candidate[1])
            session += 1
        return total_hire_cost
        """
        # left = candidates
        left = candidates - 1
        # right = n - candidates
        right = len(costs) - candidates
        left_candidates = costs[:min(left + 1, len(costs))] + [float("inf")]
        right_candidates =  costs[max(left + 1, right, 0):] + [float("inf")]
        heapq.heapify(left_candidates)
        heapq.heapify(right_candidates)
        total_hire_cost = 0
        sessions = 0
        while sessions < k:
            left_candidate, right_candidate = left_candidates[0], right_candidates[0]
            if left_candidate <= right_candidate:
                total_hire_cost += heapq.heappop(left_candidates)
                left += 1
                if left < right and left < len(costs):
                    heapq.heappush(left_candidates, costs[left])
            else:
                total_hire_cost += heapq.heappop(right_candidates)
                right -= 1
                if left < right and right >= 0:
                    heapq.heappush(right_candidates, costs[right])
            sessions += 1
        return total_hire_cost