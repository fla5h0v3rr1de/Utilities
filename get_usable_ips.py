<<<<<<< HEAD
import ipaddress
import re
from datetime import date

# User input subnet
user_input = str(input("Enter a valid IP address and subnet in the format x.x.x.x/y: "))

# Checks the format from the user input
def get_valid_subnet():
    while True:
             
        # Validate user input format
        pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}$'

        if re.fullmatch(pattern, user_input):
            try:
                # Create an IPv4 network object
                network_block = ipaddress.IPv4Network(user_input, strict=False)
                # Return list of usable IP addresses
                host_ips = [str(ip) for ip in network_block.hosts()]
                return host_ips
            except ValueError:
                print("Invalid subnet range. Please Enter correct subnet range format.")
                return False
        else:
            print("Invalid format. Please enter valid IP address or input only one instance of a subnet format in x.x.x.x/y.")
            return False

# Generate usable host IP address
usable_ips = get_valid_subnet()

# Generate output file path
today = date.today()
replace_string = user_input.replace('/', '_')
output_file_path = replace_string + "_" + str(today)

# Save the generated lists of usable host IP addresses in a file
if usable_ips == False :
    print("Unable to print result....")    
else:
    with open(output_file_path, "w") as f:
           for ip in usable_ips:
               f.write(ip + "\n")

    print(f"Completed generating usable host IPs. Check {output_file_path} for result")
=======
import ipaddress
import re
from datetime import date

# User input subnet
user_input = str(input("Enter a valid IP address subnet in the format x.x.x.x/y: "))

# Checks the format from the user input
def get_valid_subnet():
    while True:
             
        # Validate user input format
        pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}$'

        if re.fullmatch(pattern, user_input):
            try:
                # Create an IPv4 network object
                network_block = ipaddress.IPv4Network(user_input, strict=False)
                # Return list of usable IP addresses
                host_ips = [str(ip) for ip in network_block.hosts()]
                return host_ips
            except ValueError:
                print("Invalid subnet range. Please Enter correct subnet range format.")
                return False
        else:
            print("Invalid format. Please enter valid IP address or input only one instance of a subnet format in x.x.x.x/y.")
            return False

# Generate usable host IP address
usable_ips = get_valid_subnet()

# Generate output file path
today = date.today()
replace_string = user_input.replace('/', '_')
output_file_path = replace_string + "_" + str(today)

# Save the generated lists of usable host IP addresses in a file
if usable_ips == False :
    print("Unable to print result....")    
else:
    with open(output_file_path, "w") as f:
           for ip in usable_ips:
               f.write(ip + "\n")

    print(f"Completed generating usable host IPs. Check {output_file_path} for result")
>>>>>>> d1dec58 (second commit)
