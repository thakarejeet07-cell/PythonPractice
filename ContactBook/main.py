import contact_utils as cu

cu.add_contact("Aman", "9876543210")
cu.add_contact("Riya", "9123456780")

try:
    print(cu.get_contact("Aman"))
    print(cu.get_contact("Rahul")) 
except cu.ContactNotFoundError as e:
    print(f"Error: {e}")

try:
    cu.delete_contact("Rahul")
except cu.ContactNotFoundError as e:
    print(f"Error: {e}")

cu.delete_contact("Riya")