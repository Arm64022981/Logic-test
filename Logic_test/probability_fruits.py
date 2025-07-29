# ข้อที่10
import math

def nCr(n, r):
    return math.comb(n, r)

def probability_pick_fruits():
    total_fruits = 10
    mango = 1
    mangosteen = 3  
    orange = 6      

    total_ways = nCr(total_fruits, 3)
    ways_pick_each = nCr(orange,1) * nCr(mangosteen,1) * nCr(mango,1)

    probability = ways_pick_each / total_ways
    return probability

if __name__ == "__main__":
    p2 = probability_pick_fruits()
    print(f"ความน่าจะเป็นหยิบผลไม้ละชนิด 1 ลูก = {p2:.2f} หรือ {p2*100:.1f}%")
