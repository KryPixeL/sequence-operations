# create list of additive sequence with given rules
def create_sequence(a, d, stop_type, stop):
    # init
    seq = []

    # append until index met
    if stop_type == 1:
        for i in range(stop):
            seq.append(a + (d * i))

        # return the final list
        return seq

    # setup finished_seq
    if stop_type == 2:
        finished_seq = False

    # might change to for and calculate how many iterations required
    while not finished_seq:

        # if the final index of the current list exceeds/equals stop
        # then, yknow, stop
        if seq[-1] >= stop:
            finished_seq = False
            return seq

        else:
            seq.append(a + d * (len(seq) - 1))


def seq_list_print(index):
    # enumurate for n=?
    for count, i in enumerate(seq_list[index], start=1):
        print("n=%d: %d" % (count, i))

    print("")


# tests and, if possible, returns int
def try_int(value):
    # value is int, return it
    try:
        value = int(value)
        return value

    # value is not int, return error
    except ValueError:
        print(invalid % value)
        return False


# all seq put in master list
seq_list = []

# default error
invalid = "The value '%s' is inadequate.\n"  # %s inserts string
stop_fail = """The stopping point '%d' will never be reached
when increasing/decreasing by '%d'\n"""

# program loop
doing_program = True

# bools for questioning
getting_a = True
getting_d = False
getting_stop_type = False
getting_stop = False
getting_confirm = False
getting_seq = False

# main loop
while doing_program:

    # get initial value for sequence
    while getting_a:
        a = input("Starting value: ")

        # convert int to str, false if bad
        a = try_int(a)

        # move on if conversion good
        if a is not False:
            getting_a = False
            getting_d = True
            print("")

    # get increase/decrease
    while getting_d:
        d = input("Value to increase/decrease by: ")
        d = try_int(d)

        if d is not False:
            getting_d = False
            getting_stop_type = True

            # here to prevent repeat on failure to get stop type
            print("\nStop at defined index starting from 1  (1)")
            print("Stop when value is reached or exceeded (2)\n")

    # get stop_type
    while getting_stop_type:

        stop_type = input("Desired mode: ")

        stop_type = try_int(stop_type)

        # also check int is 1 or 2
        if stop_type is not False and stop_type in [1, 2]:
            getting_stop_type = False
            getting_stop = True
            print("")

        if stop_type is not False and stop_type not in [1, 2]:
            print(invalid % stop_type)

    while getting_stop:
        # change input string accordingly
        if stop_type == 1:
            stop = input("Index to stop at: ")
        else:
            stop = input("Value to stop at when reached or exceeded: ")

        stop = try_int(stop)

        if stop is not False:

            # init to prevent crash
            closet_to_stop = 0

            # check if stop can even be reached in mode 2
            if stop_type == 2:

                # manual config of seq
                temp_seq = [a, a+d]

                # returns value closest to stop
                closet_to_stop = min(temp_seq, key=lambda x: abs(x - stop))

                # if the closest value is without the increase/decrease,
                # than increasing/decreasing is creating distance and stop
                # will never be reached
                if closet_to_stop == temp_seq[0]:
                    print(stop_fail % (stop, d))

            # if mode 1 or mode 2 is good, continue
            if stop_type == 1 or closet_to_stop == temp_seq[1]:
                getting_stop = False
                getting_confirm = True

                # print recorded props
                print("\nSequence Properties")
                print("Initial value     -> %d" % a)
                print("Increase/decrease -> %d" % d)
                print("Stop mode         -> %d" % stop_type)
                print("Stop value        -> %d\n" % stop)

    while getting_confirm:

        # do confirm
        confirm = input("Is this information correct? (y/n) ").capitalize()

        # string is valid?
        if confirm not in ["Y", "N"]:
            print(invalid % confirm)

        # move on or redo
        else:
            # user is ready to move on
            if confirm == "Y":
                getting_confirm = False
                getting_seq = True

            # user wants redo
            else:
                getting_confirm = False
                getting_a = True

                print("")

    while getting_seq:
        seq = create_sequence(a, d, stop_type, stop)

        # not in use yet
        # seq_list.append(seq)

        # enumurator
        seq_list_print(seq)

        # reset
        getting_seq = False
        getting_a = True
