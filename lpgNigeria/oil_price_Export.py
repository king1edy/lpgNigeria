import psycopg2
import xlrd

book = xlrd.open_workbook('C:\\Users\\dgodswill\\Documents\\LPG Nigeria\\LPG in Nigeria - Daily LPG Depot prices.xlsx')
sheet = book.sheet_by_name("Daily Depot Prices")

database = psycopg2.connect(
    database="lpg_nigeria",
    user="postgres",
    password="MyP@ssw0rds",
    host="localhost",
    port="5432")

cursor = database.cursor()

query = """INSERT INTO public.oil_price_oilprice(date, company, price) VALUES (%s, %s, %s)"""

for r in range(1, sheet.nrows):
    Date = xlrd.xldate.xldate_as_datetime(sheet.cell(r, 1).value, book.datemode)
    Company = sheet.cell(r, 2).value
    Price = sheet.cell(r, 3).value

    values = (Date, Company, Price)

    print(values)

    cursor.execute(query, values)

cursor.close()

database.commit()

database.close()

print("")
print("")
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print("I just imported Excel into postgreSQL")
