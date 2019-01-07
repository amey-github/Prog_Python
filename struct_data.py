from struct import *

# Store as bytes data........................

packed_data = pack('iif', 1, 5, 3.14)
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))


# Convert bytes data back to readable form....

unpacked_data = unpack('iif', packed_data)
print(unpacked_data)