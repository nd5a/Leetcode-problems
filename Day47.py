# Find Minimum Diameter After Merging Two Trees

import collections
class Solution:
    def minimumDiameterAfterMerge(self, edges1, edges2):
        def get_diameter(edges):
            adj_list = collections.defaultdict(list)

            for u, v in edges:
                adj_list[u].append(v)
                adj_list[v].append(u)

            farthest = None
            farthest_distance = 0

            def get_farthest(node, parent, distance):
                nonlocal farthest
                nonlocal farthest_distance
                if distance > farthest_distance:
                    farthest_distance = distance
                    farthest = node
                
                for v in adj_list[node]:
                    if v != parent:
                        get_farthest(v, node, distance + 1)
                
            get_farthest(0, -1, 1)
            first_farthest = farthest

            farthest = None
            farthest_distance = 0
            get_farthest(first_farthest, -1, 1)

            return farthest_distance
        
        d1 = get_diameter(edges1)
        d2 = get_diameter(edges2)

        return max(d1 // 2 + d2 // 2 + 1, d1 - 1, d2 - 1)

# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# from datetime import datetime, timedelta

# # Define project phases and their durations
# phases = [
#     ("Maintenance", "2024-01-01", "2024-01-15"),
#     ("Deployment", "2024-03-11", "2024-03-20"),
#     ("Testing", "2024-03-01", "2024-03-10"),
#     ("Coding", "2024-02-01", "2024-02-28"),
#     ("Design", "2024-01-16", "2024-01-31"),
#     ("Requirements Gathering","2024-03-21", "2024-03-31"),
# ]

# # Convert dates to datetime objects
# phases = [(phase[0], datetime.strptime(phase[1], "%Y-%m-%d"), datetime.strptime(phase[2], "%Y-%m-%d")) for phase in phases]

# # Calculate durations in days for plotting
# start_dates = [phase[1] for phase in phases]
# durations = [(phase[2] - phase[1]).days for phase in phases]
# labels = [phase[0] for phase in phases]

# # Create the timeline chart
# fig, ax = plt.subplots(figsize=(10, 6))

# # Plot each phase as a horizontal bar
# ax.barh(labels, durations, left=[(start - start_dates[0]).days for start in start_dates], color='skyblue', edgecolor='black')

# # Format the x-axis with date labels
# start_date = start_dates[0]
# end_date = phases[-1][2]
# ax.set_xlim([(start_date - timedelta(days=2)), (end_date + timedelta(days=2))])
# ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
# ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
# plt.xticks(rotation=45)

# # Add labels and grid
# ax.set_xlabel("Timeline")
# ax.set_title("Project Timeline for Blog Website")
# ax.grid(axis="x", linestyle="--", alpha=0.7)

# plt.tight_layout()
# plt.show()
