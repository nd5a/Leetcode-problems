# Design Task Manager

from sortedcontainers import SortedList

class TaskManager(object):

    def __init__(self, tasks):
        """
        :type tasks: List[List[int]]
        """
        self.sl = SortedList()
        self.lookup = {}

        for u, t, p in tasks:
            self.add(u, t, p)

    def add(self, userId, taskId, priority):
        """
        :type userId: int
        :type taskId: int
        :type priority: int
        :rtype: None
        """
        self.sl.add((priority, taskId, userId))
        self.lookup[taskId] = (priority, userId)

    def edit(self, taskId, newPriority):
        """
        :type taskId: int
        :type newPriority: int
        :rtype: None
        """
        prev_priority, prev_user = self.lookup[taskId]
        self.sl.remove((prev_priority, taskId, prev_user))
        self.sl.add((newPriority, taskId, prev_user))
        self.lookup[taskId] = (newPriority, prev_user)


    def rmv(self, taskId):
        """
        :type taskId: int
        :rtype: None
        """
        prev_priority, prev_user = self.lookup[taskId]
        self.sl.remove((prev_priority, taskId, prev_user))

    def execTop(self):
        """
        :rtype: int
        """
        if len(self.sl) == 0:
            return -1
        
        p, t, u = self.sl[-1]
        self.sl.pop()
        return u


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()