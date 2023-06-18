class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = dict()

        def dfs(list_of_rooms):
            if not list_of_rooms:
                return
            while list_of_rooms != []:
                next_room = list_of_rooms.pop(0)
                if next_room not in visited:
                    visited[next_room] = True
                    dfs(rooms[next_room])
            return
        visited[0] = True
        dfs(rooms[0])
        return len(visited.keys()) == len(rooms)