'''
Problem statement

Create a rate-tracking closure.

The outer function should create a tracker with a starting count.

The returned inner function should:

Increase the count every time it is called
Return the latest count
Keep its state private
Avoid global variables
Avoid classes
'''

def create_request_tracker(start: int =0):
    count = start

    def track():
        nonlocal count 
        count += 1
        return count
    return track


track_request = create_request_tracker()

print(track_request())

print(track_request())
print(track_request())