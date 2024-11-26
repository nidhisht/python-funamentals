message = "global scope"    # Global Scope

def localScope():
    message = "local scope" # Local scope
    return message


print(message)      # output: global scope
print(localScope()) # output: local scope
print(message)      # output: global scope