import sqlite3
import csv
# created new file and table and setting up sql tools
conn = sqlite3.connect('s&p500db.sqlite')
cur = conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS stock_study;

CREATE TABLE stock_study(
    company TEXT,
    sector TEXT,
    value_vs_workers INTEGER)''')

# set up how to find specif data in file
# instead of filtering by regular methods w/ [], I use csv.DictReader
# to each column is read and no mistakes are made w/ commas or . . .
# protects code from breaking if errors occur
fh = input("enter file name:")
with open(fh,'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            company = row['Shortname']
        except ValueError:
            continue
        try:
            sector = row['Sector']
        except ValueError:
            continue
        try:
            marketcap = int(row['Marketcap'])
        except ValueError:
            continue
        try:
            num_employees = int(row['Fulltimeemployees'])
        except ValueError:
            continue
        try:
            value_vs_workers = int(marketcap/num_employees)
        except ValueError:
            continue
        cur.execute("INSERT INTO stock_study (company,sector,value_vs_workers) VALUES (?,?,?)",(company,sector,value_vs_workers))

# create table for each sector type (by distinct filtering)
# sorts new tables and extracts one value from each and puts all into new table
cur.execute(f"SELECT DISTINCT sector FROM stock_study")
sectors = [row[0] for row in cur.fetchall()]
results_list = []
for x in sectors:
    clean_x = x.replace(" ", "_").replace("&", "AND")
    cur.execute(f'''CREATE TABLE IF NOT EXISTS {clean_x}(
        company TEXT,
        value_vs_workers INTEGER,
        sector TEXT)''')
    cur.execute(f"INSERT INTO {clean_x} SELECT company, value_vs_workers, sector from stock_Study WHERE sector = ?", (x,))
    query = (f"SELECT company,value_vs_workers, sector FROM {clean_x} ORDER BY value_vs_workers DESC Limit 1")
    cur.execute(query)
    top_sector_company = cur.fetchall()
    results_list.append(top_sector_company)

results_list.sort(key=lambda entry: entry[0][1], reverse=True)

print(f"{'company':30} | {'value_vs_workers':<30} | {'sector':<30}")
print("-"*70)
for entry in results_list:
    for company, value_vs_workers, sector in entry:
        print(f"{company:<30} | {value_vs_workers:<30,} | {sector:<30}")

conn.commit()
conn.close()
    
