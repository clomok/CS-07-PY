serviceports = {}
service = port = "1"
while service != "0" and port != "0":
#while True:
    service = input("Please enter a service's name or type '0' to stop: ")
    if service == "0":
        break

    port = input("Please enter a port number or type in '0' to stop: ")
    if port == "0":
        break

    serviceports[service] = port
    print(service + " : " + port)

print(serviceports)