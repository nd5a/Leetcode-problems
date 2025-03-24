# Count Days Without Meetings

class Solution:
    def countDays(self, days, meetings):
        meetings.sort()
        
        merged_intervals = []
        for start, end in meetings:
            if merged_intervals and merged_intervals[-1][1] >= start:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], end)
            else:
                merged_intervals.append([start, end])
        
        occupied_days = sum(end - start + 1 for start, end in merged_intervals)
        
        return days - occupied_days