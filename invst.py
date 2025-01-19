amt=int(input("enter the initial amount : "))
rate=float(input("enter the interest : "))
year=int(input("enter the estimated year for investment : "))
for year in range(1,year+1):
    f_amt=amt*(1+rate)**year
    print("%-6d %12.2f" %(year,f_amt))

