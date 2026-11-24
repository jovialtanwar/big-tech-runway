role = input("Enter role (admin/guest): ")
command = input("Enter command (SET/GET/DELETE): ")
if command == "GET":
    print("Fetching value from memory...")
elif (command == "SET" or command == "DELETE") and role == "admin":
    print("Access granted: modifying database!")
elif (command == "SET" or command == "DELETE") and role != "admin":
    print("Access denied: admin role required!")
else:
    print("Invalid command!")