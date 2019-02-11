#extending classes with mixins


# These classes, by themselves, are useless. In fact, if you instantiate any one of them, it
# does nothing useful at all (other than generate exceptions). Instead, they are supposed
# to be mixed with other mapping classes through multiple inheritance.
# Mixin classes appear in various places in the standard library, mostly as a means for
# extending the functionality of other classes similar to as shown. They are also one of
# the main uses of multiple inheritance. For instance, if you are writing network code,
# you can often use the ThreadingMixIn from the socketserver module to add thread
# support to other network-related classes