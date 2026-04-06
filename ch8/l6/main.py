from queue import Queue


def matchmake(queue, user):
    name, func = user
    if func == "leave":
        queue.search_and_remove(name)
    if func == "join":
         queue.push(name)
    if queue.size() >= 4:
        user1 = queue.pop()
        user2 = queue.pop()
        return f"{user1} matched {user2}!"
    return "No match found"
