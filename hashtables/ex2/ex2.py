#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    print(hashtable.storage)

    current_location = "NONE"

    i = 0
    while route[len(route) - 1] is None:
        next_stop = hash_table_retrieve(hashtable, current_location)
        print(next_stop)
        route[i] = next_stop
        i += 1
        current_location = next_stop

    print(route)

    return route

tickets = [
    Ticket("NONE", "PDX"),
    Ticket("PDX", "DCA"),
    Ticket("DCA", "NONE")
]

reconstruct_trip(tickets, len(tickets))