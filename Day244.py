# Maximum Matching of Players With Trainers

class Solution:
    def matchPlayersAndTrainers(self, players,  trainers):
        # players.sort()
        # sl = SortedList(trainers)
        # count = 0
        # for p in players:
        #     index = sl.bisect_left(p)

        #     if index < len(sl):
        #         count += 1
        #         sl.remove(sl[index])
        # return count

        players.sort()
        trainers.sort()
        T = len(trainers)

        tindex = 0
        count = 0
        for p in players:
            while tindex < T and trainers[tindex] < p:
                tindex += 1
            
            if tindex < T:
                tindex +=1
                count+= 1
        return count