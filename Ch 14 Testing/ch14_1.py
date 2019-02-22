It’s worth noting that certain C extensions to Python may write directly to standard output, bypassing
the setting of sys.stdout. This recipe won’t help with that scenario, but it should work fine with pure
Python code (if you need to capture I/O from such C extensions, you can do it by opening a temporary
file and performing various tricks involving file descriptors to have standard output temporarily
redirected to that file).