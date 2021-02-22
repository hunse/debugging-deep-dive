import gc
import tracemalloc

tracemalloc.start(25)


def make_list(x, other=list()):
    other.append(x)
    return other


x = object()
y = object()

ary_list = list((x, y))
# ary_list = [x, y]  # if we define like this, we won't be able to get the traceback

q = make_list(x)
r = make_list(x, [y])

print("x referrers:")
referrers = gc.get_referrers(x)
for ref in referrers:
    tb = tracemalloc.get_object_traceback(ref)
    print(f"- id={id(ref)}:")

    # tracemalloc cannot always get the traceback. Cases where it fails include when
    # the argument is a basic object (int, string, lists created with [] brackets, but
    # not those created with the list() function).
    if tb is not None:
        for line in tb.format():
            print(line)
