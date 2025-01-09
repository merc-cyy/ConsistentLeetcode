class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #input: array of int piles and h hrs
        #output: k 
        #goal: find min speed of Koko eating such that, she can eat all bananas in h hrs
        #task: find a min k or the smallest k that will ensure she eats all bananas
        #constraints: can only eat k per hour so any extra is another separate hour and any less means she doesn't eat anymore in that hour

        #max k is max number in piles
        #min k is 1 but we are looking for the min k that ensures she eats all bananas

        #search through the range of k binarily

        #max_k
        max_k = max(piles)
        ans = max_k
        l, r = 1, max_k
        while l <= r:
            m = (l + r) // 2
            hrs = 0
            for i in piles:
                hrs += math.ceil(i / m)

            if hrs <= h:#can we do better? can we get a smaller k to utilise extra hours?
                r = m -1
                ans = min(ans, m)
            else:
                l = m + 1

        return ans



        #if hrs < h: search left
        #if hrs > h: search. right
        #else: (equal) return


        