class AppError(Exception):
    pass

class DatabaseError(AppError):
    pass

def save_user(data):
    try:
        raise ConnectionError("Could not reach database server")
    except ConnectionError as original_error:
        raise DatabaseError("Failed to save user") from original_error


try:
    save_user({"name": "Aman"})
except DatabaseError as e:
    print(f"Error: {e}")
    print(f"Caused by: {e.__cause__}") 
        


        


