class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = dict()
        curr_room = 0
        curr_room_keys  = rooms[curr_room]
        visited[0] = True
        while curr_room_keys:
            curr_room_key = curr_room_keys.pop(0)
            if curr_room_key in visited:
                continue
            else:
                visited[curr_room_key] = True
                curr_room_keys = rooms[curr_room_key] + curr_room_keys
        return len(visited) == n
