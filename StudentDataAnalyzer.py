import os
import csv
import pandas as pd

class Student_Data_Analyzer:
    # Store default file path for when not exit file
    path=r"C:\Users\cheta\OneDrive\Desktop\students.csv"

    # Add student details in execel
    def Add_Student(self,path,Roll_number,Name,subject,percentage):
        with open(path,'a', newline="") as f:
            writer=csv.writer(f)
            writer.writerow([Name,Roll_number,subject['science'],subject['maths'],subject['hindi'],subject['english'],percentage])
            print("Data add in excel")
            
    # Calculate Average score of class and single student
    def CalculateAvg(self,path):
            print("Press 1 for All student average marks ")
            print("Press 2 for One student average marks ")
            choice=int(input())
        
            match choice :
                # This section for calculate class average
                case 1:
                    with open (path,'r') as f:
                        reader=csv.reader(f)
                        # data convert into list 
                        data=list(reader)
                        ans=0
                        
                        for i in range(1,len(data)):
                            sum=0
                            for y in range(2,len(data[i])-1):
                                sum+=int(data[i][y])
                            ans+=sum/4
                        
                        print("Students average score in college is {} %".format(round(ans/len(data)-1,2)))

        
                # This section for calculate single student       
                case 2:
                    ur_input=int(input("Enter student id"))
                    with open(self.path,'r') as f:
                        reader=list(csv.reader(f))
                        for i in range(1,len(reader)):
                            if ur_input==int(reader[i][1]):
                                ans=reader[i][-1]
                                print(f"{reader[i][0]} score is {ans} %")
                                break
                case _:
                    print("You Enter something wrong ")
                    exit

    # Filter top 5 Students in class
    def FilterStudent(self,path) :
              
        with open(path,'r') as f:
            reader=list(csv.reader(f))
            if len(reader)<2:
                print("No student data available")
                return
            df=pd.DataFrame(reader[1:],columns=reader[0])
            df=df.sort_values(by="persentage" ,ascending=False)
            df=df.iloc[:,[0,-1]]
            print(df.head(5))

    #Display all Students
    def Display(self,path):
        with open(path,'r') as f:
            reader=list(csv.reader(f))
            # columns=reader[0]
            # rows=reader[1:]
            # print(" |  ".join(columns))
            # for row in rows:
            #     print("   | ".join(row))
                
            df=pd.DataFrame(reader[1:],columns=reader[0])
            print(f"Your data has {len(df)} rows")
            print(df.head(5))
                   
                
                
# Main function 

if __name__== "__main__":
    try:
        obj=Student_Data_Analyzer()
    
        # Take file path from user
        path=input("""If you have a file, Enter the file path\nFor example :- C:\\desktop\\<file_name.csv """)
        if not(os.path.exists(path)):
            print("You entered worng path,Table created at :- C:\\Users\\cheta\\OneDrive\\Desktop\\students.csv")
            with open (obj.path,'w',newline="") as f:
                path=obj.path
                writer=csv.writer(f)
                writer.writerow(["Name","Roll_number",'Science','Maths','Hindi','English',"persentage"])
            
        stop=False
        while(True):
            print("\n+++++++++ Wellcome to Student Data Analyzer +++++++++")
            print("Press 1 for Add Student")
            print("Press 2 for Calculate average")
            print("Press 3 for Filter 5 top rank student in college")
            print("Press 4 for Display lenght of table and 5 rows")
            print("Press 5 for exit")
            user=int(input())
            
            match user :
                case 1:
                    Roll_number=int(input("Enter you roll number "))
                    Name=input("Enter your name ")
                    subjects=["maths","hindi","english","science"]
                    subject={}
                    
                    for i in subjects:
                        while True:
                            try:
                                mark=int(input(f"Enter your {i} marks "))
                                if 1<=mark<=100:
                                    subject[i]=mark
                                    break
                                
                                print("Invalid marks. Please enter 1 to 100")
                            except ValueError:
                                print("Please enter a number only")
                            
                    percentage=sum(subject.values())/4
                    obj.Add_Student(path,Roll_number,Name,subject,percentage)
                    
                case 2:
                    obj.CalculateAvg(path)
                    
                case 3:
                    obj.FilterStudent(path)

                case 4:
                    obj.Display(path)
                    
                case 5:
                    break;
                case _:
                    print("\n Your enter something worng \n")
                    break;
    except ValueError as v:
        print(v)