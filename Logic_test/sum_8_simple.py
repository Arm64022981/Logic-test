# ข้อที่11
def find_sum_1000_with_8():
    results = []
    candidates = [8, 88, 888]
    for a in candidates:
        for b in candidates:
            for c in candidates:
                for d in candidates:
                    for e in candidates:
                        if a + b + c + d + e == 1000:
                            results.append([a, b, c, d, e])
    return results

if __name__ == "__main__":
    solutions = find_sum_1000_with_8()
    print(f"พบ {len(solutions)} วิธีที่ใช้เลข 8 บวกกันได้ 1000:")
    for sol in solutions:
        print(" + ".join(str(x) for x in sol), "=", 1000)
