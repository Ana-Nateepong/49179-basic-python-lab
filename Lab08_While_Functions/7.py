nums = []
while True:
    x = input()
    if x == "end": break
    nums.append(float(x))
if nums:
    print("ค่าสูงสุด:", max(nums))
    print("ค่าต่ำสุด:", min(nums))
else:
    print("ไม่มีข้อมูล")
