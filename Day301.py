# Minimum Number of People to Teach

class Solution:
    def minimumTeachings(self, n, languages, friendships):
        N = len(languages)

        # Convert each user's languages into a set for quick lookup
        lans = [set(l) for l in languages]

        # Find all people involved in problematic friendships
        mustLearnSet = set()
        for u, v in friendships:
            if len(lans[u-1] & lans[v-1]) == 0:  # no common language
                mustLearnSet.add(u-1)
                mustLearnSet.add(v-1)

        # If everyone already can communicate
        if not mustLearnSet:
            return 0 

        best = float("inf")

        # Try teaching each language
        for l in range(1, n+1):
            count = 0
            for person in mustLearnSet:
                if l not in lans[person]:
                    count += 1
            best = min(best, count)

        return best
