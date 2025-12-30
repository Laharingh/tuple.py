employees= [
  {"eid": 1, "ename": "Amitabh Bachchan", "gender": "Male"},
  {"eid": 2, "ename": "Shah Rukh Khan", "gender": "Male"},
  {"eid": 3, "ename": "Salman Khan", "gender": "Male"},
  {"eid": 4, "ename": "Aamir Khan", "gender": "Male"},
  {"eid": 5, "ename": "Akshay Kumar", "gender": "Male"},
  {"eid": 6, "ename": "Ajay Devgn", "gender": "Male"},
  {"eid": 7, "ename": "Hrithik Roshan", "gender": "Male"},
  {"eid": 8, "ename": "Ranbir Kapoor", "gender": "Male"},
  {"eid": 9, "ename": "Ranveer Singh", "gender": "Male"},
  {"eid": 10, "ename": "Varun Dhawan", "gender": "Male"},

  {"eid": 11, "ename": "Deepika Padukone", "gender": "Female"},
  {"eid": 12, "ename": "Alia Bhatt", "gender": "Female"},
  {"eid": 13, "ename": "Kareena Kapoor", "gender": "Female"},
  {"eid": 14, "ename": "Katrina Kaif", "gender": "Female"},
  {"eid": 15, "ename": "Priyanka Chopra", "gender": "Female"},
  {"eid": 16, "ename": "Anushka Sharma", "gender": "Female"},
  {"eid": 17, "ename": "Aishwarya Rai", "gender": "Female"},
  {"eid": 18, "ename": "Vidya Balan", "gender": "Female"},
  {"eid": 19, "ename": "Taapsee Pannu", "gender": "Female"},
  {"eid": 20, "ename": "Kangana Ranaut", "gender": "Female"},

  {"eid": 21, "ename": "Rajinikanth", "gender": "Male"},
  {"eid": 22, "ename": "Kamal Haasan", "gender": "Male"},
  {"eid": 23, "ename": "Vijay", "gender": "Male"},
  {"eid": 24, "ename": "Ajith Kumar", "gender": "Male"},
  {"eid": 25, "ename": "Suriya", "gender": "Male"},
  {"eid": 26, "ename": "Dhanush", "gender": "Male"},
  {"eid": 27, "ename": "Mahesh Babu", "gender": "Male"},
  {"eid": 28, "ename": "Prabhas", "gender": "Male"},
  {"eid": 29, "ename": "Allu Arjun", "gender": "Male"},
  {"eid": 30, "ename": "Ram Charan", "gender": "Male"},

  {"eid": 31, "ename": "Nayanthara", "gender": "Female"},
  {"eid": 32, "ename": "Samantha Ruth Prabhu", "gender": "Female"},
  {"eid": 33, "ename": "Rashmika Mandanna", "gender": "Female"},
  {"eid": 34, "ename": "Pooja Hegde", "gender": "Female"},
  {"eid": 35, "ename": "Keerthy Suresh", "gender": "Female"},
  {"eid": 36, "ename": "Sai Pallavi", "gender": "Female"},
  {"eid": 37, "ename": "Tamannaah Bhatia", "gender": "Female"},
  {"eid": 38, "ename": "Trisha Krishnan", "gender": "Female"}
]


male_employees=[]

for employee in employees:
    if employee["gender"]=="Male":
          male_employees.append(employees)
print("No of male employees:", len (male_employees))



