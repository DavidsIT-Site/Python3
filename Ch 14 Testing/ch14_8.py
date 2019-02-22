
 all exceptions also derive from BaseException, you should not use this as a base class for new exceptions.
BaseException is reserved for system-exiting exceptions, such as KeyboardInterrupt or SystemExit,
and other exceptions that should signal the application to exit. Therefore, catching these exceptions is
not the intended use case.