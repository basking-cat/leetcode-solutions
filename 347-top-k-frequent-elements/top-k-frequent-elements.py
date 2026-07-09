import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # store frequencies in a hashmap
        # add all the elements in the hashmap into min-heap
        # keep only k elements in min-heap and when overflowed, pop the min element
        # pop all the k elements left in min-heap & return them

        hashmap = {}
        for n in nums:
            if n not in hashmap:
                hashmap[n] = 0
            hashmap[n] += 1

        min_heap = []
        for key in hashmap.keys():
            heapq.heappush(min_heap, (hashmap[key], key))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [e[1] for e in min_heap]

        # time: O(nlogk)
        # space: O(n)