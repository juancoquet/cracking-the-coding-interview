import queue


# 4.1 route between nodes
def route_exists(start, target):
	if bfs(start, target):
		path = [target,]
		current = target
		while current.predecessor is not None:
			path.append(current.predecessor)
		path.reverse()
		return(path)
	return False


def bfs(start, target):
	to_search = queue()
	start.visited = True
	to_search.enqueue(start)
	while to_search.size > 0:
		current = to_search.dequeue()
		for neighbour in current.connected_to:
			if not neighbour.visited and not neighbour.fully_searched:
				neighbour.visited = True
				to_search.enqueue(neighbour)
				neighbour.predecessor = current
				if neighbour == target:
					return True
		current.fully_searched = True
	return False