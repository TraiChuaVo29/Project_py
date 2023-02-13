def time_now():
    # Xác định ngày tháng hiện tại
    # Trả về kết quả là 3 biến day, month, year
    from datetime import date
    today = date.today()

    day = today.day
    month = today.month
    year = today.year

    return day, month, year
def code_month(month):
    # Đưa ra mã tháng
    if month == 1 or month == 9 or month == 12:
        code_month = 0
    elif month == 4 or month == 7:
        code_month = 1
    elif month == 10:
        code_month = 2
    elif month == 2 or month == 5:
        code_month = 3
    elif month == 8:
        code_month = 4
    elif month == 3 or month == 11:
        code_month = 5
    else:
        code_month = 6
    return code_month

def code_year(year):
    # Đưa ra mã năm
    xy = year % 100
    code_year = ((xy % 7) + (xy // 4)) % 7
    return code_year

def code_century(year):
    # Đưa ra thế kỷ
    wz = year // 100
    code_century = ((wz % 4) * 5) % 7
    if code_century == 0:
        code_century = 7
    return code_century

def leap_year(year):
    # Xác định năm đó có phải là năm nhuận hay không
    # Nếu là năm nhuận sẽ trả về kết quả là True
    # Nếu không là năm nhuận sẽ trả về kết quả là False
    result = False
    if year % 100 == 0:
        if year % 400 == 0:
            result = True
        else:
            result = False
    else:
        if year % 4 == 0:
            result = True
        else:
            result = False
    return result

def error_leap_year(leap_year, month):
    # Lấy kết quả của việc xác định năm nhuận để đưa ra giá trị sai số
    if month >= 3:
        error_leap_year = -2
    else:
        if leap_year == True:
            error_leap_year = -1
        else:
            error_leap_year = 0
    return error_leap_year

def search_weekdays(surplus, day, month, year):
    # Hàm sẻx trả về kết quả là ngày tháng năm và thứ ở thời điểm hiện tại dựa vào số dư (surplus) được cung cấp
    if surplus == 1:
        print("Ngay %d thang %d nam %d la ngay Chu Nhat !" %(day, month, year))
    if surplus == 2:
        print("Ngay %d thang %d nam %d la ngay thu Hai !" %(day, month, year))
    if surplus == 3:
        print("Ngay %d thang %d nam %d la ngay thu Ba !" %(day, month, year))
    if surplus == 4:
        print("Ngay %d thang %d nam %d la ngay thu Tu !" %(day, month, year))
    if surplus == 5:
        print("Ngay %d thang %d nam %d la ngay thu Nam !" %(day, month, year))
    if surplus == 6:
        print("Ngay %d thang %d nam %d la ngay thu Sau !" %(day, month, year))
    if surplus == 7:
        print("Ngay %d thang %d nam %d la ngay thu Bay !" %(day, month, year))


def main():
    # Xác định thời gian hiện tại là thứ ngày tháng năm nào
    day, month, year = time_now()
    
    surplus = (day + code_month(month) + code_year(year) + code_century(year) + error_leap_year(leap_year(year), month)) % 7

    search_weekdays(surplus, day, month, year)

if __name__ == "__main__": 
    main() 