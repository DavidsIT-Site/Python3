#extending classes with mixins

# Mixin classes appear in various places in the standard library, mostly as a means for
# extending the functionality of other classes similar to as shown. They are also one of
# the main uses of multiple inheritance. For instance, if you are writing network code,
# you can often use the ThreadingMixIn from the socketserver module to add thread
# support to other network-related classes