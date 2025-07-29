# ข้อที่12
def probability_sum_10_and_diff_2():
    total_cases = 0
    sum_10_cases = 0
    diff_2_cases = 0

    for dice1 in range(1, 7):
        for dice2 in range(1, 7):
            total_cases += 1

            if dice1 + dice2 == 10:
                sum_10_cases += 1

            if abs(dice1 - dice2) == 2:
                diff_2_cases += 1

    prob_sum_10 = sum_10_cases / total_cases
    prob_diff_2 = diff_2_cases / total_cases

    print(f"ความน่าจะเป็นที่ผลรวมของแต้มเป็น 10: {prob_sum_10:.4f} ({sum_10_cases}/{total_cases})")
    print(f"ความน่าจะเป็นที่ผลต่างของแต้มเป็น 2: {prob_diff_2:.4f} ({diff_2_cases}/{total_cases})")

probability_sum_10_and_diff_2()
