from datetime import date, timedelta
def dateRange(date1, date2):
    #return all dates from date1 to date2
    for n in range(int ((date2 - date1).days)+1): yield date1 + timedelta(n)
def isMagicDate(date):
    #a magic date is a date where day*month = last two years
    if(date.day * date.month == (int(str(date.year)[2:]))): print(date.strftime("%Y-%m-%d")," is a Magic Date")
def main():
    startDate = date(1901,1,1)
    endDate = date(1999,12,31)
    for dt in dateRange(startDate, endDate): isMagicDate(dt)
main()

