# 1. Our data(A list of servers dictionories)
servers = [{"name" : "web_server" , "status" : "online"},
           {"name" : "Database" , "status" : "down"},
           {"name" : "backup_server" , "status" : "online"}]

# 2. Open a file to write our report
# w is for "write"

with open("server_report.txt", "w") as file:
    file.write("WEEKLY STATUS REPORT\n")
    file.write("====================\n")
    
# 3. Loop through our data and write to the file
    for s in servers:
        line = "System:" + s["name"] + "| Status:" + s["status"] + "\n"
        file.write(line)

print("Reprt generated successfully!")
