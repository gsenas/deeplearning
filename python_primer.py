from __future__ import absolute_import, division, print_function, unicode_literals

print("Hello World")


def helloWorldXY(x, y):
    if x < 10:
        print("Hello World, x was < 10")
    elif x < 20:
        print("Hello World, x was >= 10 but < 20")
    else:
        print("Hello World, x was >= 20")
    return x + y


for i in range(8, 25, 5):  # i=8, 13, 18, 23 (start, stop, step)
    print("--- Now running with i: {}".format(i))
    r = helloWorldXY(i, i)
    print("Result from HelloWorld: {}".format(r))

    print("Iterate over the items. `range(2)` is like a list [0,1].")
for i in range(2):
    print(i)

print("Iterate over an actual list.")
for i in [0, 1]:
    print(i)

print("While works")
i = 0
while i < 2:
    print(i)
    i += 1

print("Python supports standard key words like continue and break")
while True:
    print("Entered while")
    break
