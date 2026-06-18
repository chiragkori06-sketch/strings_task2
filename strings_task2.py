import sys


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def clean_brand_name(name):
    return name.strip().replace("-", " ")


def format_product_display(name, price):
    return f"{name} - ₹{price}"


# 1. Print product name in uppercase and lowercase
product_name = "Redmi Note 12 Pro"
print("1. Uppercase and lowercase:")
print(product_name.upper())
print(product_name.lower())


# 2. Clean brand name
messy_brand = " oneplus-Nord "
print("\n2. Clean brand name:")
print(clean_brand_name(messy_brand))


# 3. Extract brand and model using split() and slicing
full_name = "Apple iPhone 14 Pro Max"
first_word = full_name.split()[0]
split_point = len(first_word)

brand = full_name[:split_point]
model = full_name[split_point + 1:]

print("\n3. Brand and model:")
print("Brand:", brand)
print("Model:", model)


# 4. Format product display
print("\n4. Product display:")
print(format_product_display("Boat Earbuds", 1299))


# 5. Clean a list of messy product names
messy_products = [" mi-Band 5 ", " SAMSUNG-Galaxy ", " realme-Book "]
cleaned_products = []

for product in messy_products:
    cleaned = product.strip().replace("-", " ").title()
    cleaned_products.append(cleaned)

print("\n5. Cleaned product list:")
print(cleaned_products)
