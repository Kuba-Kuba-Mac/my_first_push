# python writing files (.txt , .json, .csv)
import  json



employees = ["kuba","Azat","Tima","Beka","Aziz"]
file_path = "/Users/macbook/Desktop/output.txt"

try:
    with open(file=file_path, mode="w") as file:
        for i in employees:
            file.write(i+"\n")
        print(f"txt file '{file_path}' was created ")
except FileExistsError:
    print("That file is already exist")



# employees = {
#     "name":"kuba",
#     "age":19,
#     "status":"student"
# }
# file_path = "/Users/macbook/Desktop/output.json"
#
# try:
#     with open(file=file_path, mode="w") as file:
#         json.dump(employees, file, indent=4)
#         print(f"json '{file_path}' was created ")
# except FileExistsError:
#     print("That file is already exist")