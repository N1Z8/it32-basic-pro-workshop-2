quantity = int(input("Enter value1: "))
cost_price = int(input("Enter value2: "))
sell_price = int(input("Enter value3: "))
team_members = int(input("Enter value4: "))

a = quantity * cost_price
b = quantity * sell_price
c = quantity * sell_price - quantity * cost_price
total_boss = c *(20/100)

print(f"ต้นทุนทั้งหมด {a } บาท")
print(f"รายรับทั้งหมด {b } บาท")
print(f"รายได้สุทธิ {c} บาท")
print(f"จำนวนเงินที่หักให้บอส { total_boss } บาท")