#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ticket_hash = {}
    route = []

    for ticket in tickets:
        if ticket.source == "NONE":
            route.append(ticket.destination)
        ticket_hash[ticket.source] = ticket.destination
        
    current_ticket = ticket_hash[route[0]]

    count = 1

    while count < length:
        route.append(current_ticket)
        current_ticket = ticket_hash[current_ticket]
        count += 1

    return route

ticket_1 = Ticket("NONE", "PDX")
ticket_4 = Ticket("DCA", "PAN")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("PAN", "NONE")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4]

print(reconstruct_trip(tickets, 4))
