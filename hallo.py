from ctypes import CDLL

lib = CDLL("target/release/librust_in_python.dylib")
lib.hello()
