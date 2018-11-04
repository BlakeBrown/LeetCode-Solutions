# Solution 1: Brute force O(n^2). Sort rooms in ascending order of start time.
# For each room, check if a previous room has been freed and if so book it.

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        intervals.sort(key = lambda x: x.start)
        rooms = [intervals[0]] # base case: book the first room
        for i in range(1,len(intervals)):
            empty_room = False
            # Check if any previously booked rooms are empty
            for j in range(len(rooms)):
                if rooms[j].end <= intervals[i].start:
                    # Book the empty room
                    rooms[j].end = intervals[i].end
                    empty_room = True
                    break
            if not empty_room:
                rooms.append(intervals[i])
        return len(rooms)


# Solution 2: Notice that we don't need to store pairs since we only care about
# the end of a booked room
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        intervals.sort(key = lambda x: x.start)
        rooms = [intervals[0].end] # base case: book the first room
        for i in range(1,len(intervals)):
            empty_room = False
            # Check if any previously booked rooms are empty
            for j in range(len(rooms)):
                if rooms[j] <= intervals[i].start:
                    # Book the empty room
                    rooms[j] = intervals[i].end
                    empty_room = True
                    break
            if not empty_room:
                rooms.append(intervals[i].end)
        return len(rooms)

# Solution 3: We could do some sort of clever binary search on rooms in the previous sol.,
# but let's try another approach. Sort a list of start times and
# end times. When we hit a start time ++ to the number of used rooms, when we hit an end time
# -- to the number of used rooms. Keep track of the max used rooms.

# O(nlogn) beats 50%

# We could do slightly better by maintaining seperate arrays for start/end times
# so we get O(2 * (n/2 log n/2)) but meh not worth the effort. Asymptotic runtime is the same.

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        bookings = []
        for interval in intervals:
            bookings.append((interval.start,1))
            bookings.append((interval.end,-1))
        bookings.sort()
        max_rooms_used = 0
        rooms_used = 0
        for booking in bookings:
            rooms_used += booking[1]
            max_rooms_used = max(rooms_used, max_rooms_used)
        return max_rooms_used

