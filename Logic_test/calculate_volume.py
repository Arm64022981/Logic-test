# ข้อที่7
def Calculate(x):
    volume = 5832
    for day in range(1, x + 1):
        used = volume / 3
        volume = volume - used
        print(f"วัน {day} น้ำเหลือ {volume:.2f} ลิตร")
    return volume

days = 7
remaining = Calculate(days)
print(f"น้ำเหลือในถังหลังจาก {days} วัน = {remaining:.2f} ลิตร")
