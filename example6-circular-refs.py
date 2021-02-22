"""
Modified from: https://pythonchb.github.io/PythonTopics/weak_references.html
"""

import gc
import sys
import weakref

import guppy
import numpy as np

deleted_object_messages = []


class MyChild(object):
    def __init__(self, parent):
        self._parent = parent
        # self._parent = weakref.ref(parent)

        # store some data so it will use appreciable memory
        self.data = np.ones(1000000)

    @property
    def parent(self):
        return self._parent() if isinstance(self._parent, weakref.ref) else self._parent

    def __del__(self):
        # overriding __del__ stops gc from collecting circular references for this obj
        deleted_object_messages.append(("MyChild deleted", id(self)))


class MyParent(object):
    def __init__(self):
        self.children = []

    def addChild(self):
        child = MyChild(self)
        self.children.append(child)
        return child

    def __del__(self):
        # overriding __del__ stops gc from collecting circular references for this obj
        deleted_object_messages.append(("MyParent deleted", id(self)))


# set these flags to get gc to record uncollectable objects in `gc.garbage`
# gc.set_debug(gc.DEBUG_UNCOLLECTABLE | gc.DEBUG_SAVEALL)

p = MyParent()
print("refcount for p:", sys.getrefcount(p))

a = p.addChild()
a2 = p.addChild()
print("refcount for p after adding an two children:", sys.getrefcount(p))
print("a's refcount:", sys.getrefcount(a))
print("a2's refcount:", sys.getrefcount(a2))

p_ref = weakref.ref(p)
a_ref = weakref.ref(a)
a2_ref = weakref.ref(a2)

print("deleting p...")
del p
print("a's refcount:", sys.getrefcount(a))
print("a2's refcount:", sys.getrefcount(a2))

print("deleting a...")
del a
print(f"messages: {deleted_object_messages}")

print("deleting a2...")
del a2
print(f"messages: {deleted_object_messages}")

print(f"p_ref: {p_ref()}")
print(f"a_ref: {a_ref()}")
print(f"a2_ref: {a2_ref()}")

# # must call before looking at `gc.garbage`
# gc.collect()

# print("\ngc.garbage:")
# print(gc.garbage)
