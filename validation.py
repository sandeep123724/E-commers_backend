import re
class ValidationError(Exception):
    pass
def validate_customer(name,email,phone,city):
    if len(name)<3:
        raise ValidationError("Name must  be at least 3 characters long.")

    Email=r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(Email,email):
        raise ValidationError('Invalid email format.')

    if not(phone.isdigit() and len(phone)==10):
        raise ValidationError("phone number must be 10 digits.")

    if city =="" or city is None:
        raise ValidationError("City cannot be empty.")

    return "validation Sucessfully"

def Validate_Product(name,category,price,stock):
    if not name:
        raise ValidationError("Product name cannot empty")
    categories =["Electronics","Clothing","Books"]
    if category not in categories:
        raise ValidationError(f"category must be one of {categories}")
    if price<=0:
        raise ValidationError("price must be greater then 0")
    if stock <0:
        raise ValidationError("stock cannot be negative. ")

    return "Product validation is correct"

def Validate_order_transaction(current_status,new_status):
    if current_status=="completed":
        raise ValidationError("cannot change status or cancel a completed order.")
    allowed_status=['new','cancelled','completed']

    if new_status not in allowed_status:
        raise ValidationError('invaild status')

    return "Order validation is correct"


result = Validate_order_transaction(
    "new",
    "completed",

)
print(result)


