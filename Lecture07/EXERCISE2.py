performance_data = {
    "Sales": {
        "Alice": [80, 85, 88, 90], 
        "Bob": [70, 75, 78, 80],
        "Charlie": [60, 65, 70, 72]
  },  
  "Engineering": {
        "David": [90, 92, 94, 95], 
        "Eve": [85, 88, 87, 90], 
        "Frank": [88, 87, 86, 85]
        },
    "HR":{
        "Grace": [70, 72, 74, 76],
        "Heidi": [65, 68, 70, 73], 
        "Ivan": [60, 62, 64, 66]}}
# คำนวณคะแนนเฉลี่ยการทำงานของแต่ละพนักงาน
average_scores = {}
for department, employees in performance_data.items():
    average_scores [department]= {}
    for employee, scores in employees.items():
        average = sum(scores) / len(scores)
        average_scores [department] [employee] = average
        
print("Average Performance Scores :",average_scores)

# ระบุพนักงานที่มีผลงานดีที่สุดในแต่ละแผนกตามคะแนนเฉลี่ยของพวกเขา
# หาผลเฉลี่ยคะแนนการทำงานสูงสุดในแต่ละแผนก
# หาพนักงานที่แสดงให้เห็นถึงการพัฒนาอย่างต่อเนื่อง
# สร้างรายงานสรุป