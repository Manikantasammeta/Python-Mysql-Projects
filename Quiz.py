import mysql.connector as con
from datetime import datetime
db_connection = con.connect(
    host="localhost",        # Hostname (usually 'localhost' if running locally)
    user="root",             # Your MySQL username
    password="1234",         # Your MySQL password
    database="Quiz"          # The name of the database you want to connect to
)

print("wlcome to Quiz")
while True:
    print(f"selecct the Following option \n 1-Admin Login \n 2-User Login")
    login_input=int(input("Enter the Option:"))
    if login_input ==1:
        while True:
            Admin_username=input("Enter User Name: ")
            if Admin_username=="Mani":
                Admin_password=input("Enter Password: ")
                if Admin_password=="1234":
                    while True:
                        print(f"selecct the Following option \n 1-Add New Question \n 2-Modify Questions \n 3-Delete Question \n 4-view All Questions \n 5- View Users \n 6-Exit ")
                        Admin_choice=int(input("Enter Option: "))
                        if Admin_choice==1:
                            cur=db_connection.cursor()
                            tech=input("Enter Technology: ").upper()
                            Question=input("Enter the Question : ")
                            Option_1=input("Enter Option-1: ")
                            Option_2=input("Enter Option-2: ")
                            Option_3=input("Enter Option-3: ")
                            Option_4=input("Enter Option-4: ")
                            Answer=input("Enter Answer Option 1 or 2 or 3 or 4 : ")
                            insert_query = """INSERT INTO questions (technology, question_text, option1, option2, option3, option4, correct_answer)VALUES (%s, %s, %s, %s, %s, %s, %s);"""
                            cur.execute(insert_query, (tech, Question, Option_1, Option_2, Option_3, Option_4, Answer))
                            db_connection.commit()
                            print("Question Aadded Sucessesfully ")
                            cur.close()
                            
                            print("\n\n")

                        elif Admin_choice==2:
                            cur=db_connection.cursor()
                            cur.execute("SELECT * FROM questions")
                            data=cur.fetchall()
                            question_number = int(input("Enter the question number you want to Modify: "))
                            if question_number <=len(data):
                                
                                cur.execute(f"SELECT * FROM questions WHERE id = {question_number} LIMIT 1")
                                data = cur.fetchone()
                                print(data)
                                for i in range(1):
                                    print("Question no",data[0],"Technology:",data[1])
                                    print("Question",data[2])
                                    print("Option-1: ",data[3])
                                    print("Option-2: ",data[4])
                                    print("Option-3: ",data[5])
                                    print("Option-4: ",data[6])
                                print("\n\n")
                                tech=input("Enter New Question Technology: ").upper()
                                Question=input("Enter the New Question : ")
                                Option_1=input("Enter Option-1: ")
                                Option_2=input("Enter Option-2: ")
                                Option_3=input("Enter Option-3: ")
                                Option_4=input("Enter Option-4: ")
                                Answer=input("Enter Answer Option 1 or 2 or 3 or 4 : ")
                                
                                update_query = """UPDATE questions SET technology = %s,question_text = %s, 
                                option1 = %s, option2 = %s, option3 = %s, option4 = %s, correct_answer = %s 
                                WHERE id = %s"""
                                cur.execute(update_query, (tech, Question, Option_1, Option_2, Option_3, Option_4, Answer,question_number))
                                db_connection.commit()
                                print("Question updated successfully!")   
                                print("\n\n")   
                            else:
                                print("The Question number you entered not exit \n plz Try again with a valid Question number")  
                            cur.close()
                        elif Admin_choice==3:
                            Ques_no=int(input("Enter the Question number that you Want delete: "))
                            cur=db_connection.cursor()
                            cur.execute(f"delete FROM questions where id ={Ques_no}")  
                            print("Question Deleted Sucessfully") 
                            print("\n\n")
                            db_connection.commit()          
                            cur.close()
                        elif Admin_choice==4:
                            cur=db_connection.cursor()
                            cur.execute("SELECT * FROM questions")
                            data=cur.fetchall()
                            for i in range(len(data)):
                                print("Question no",data[i][0],"Technology:",data[i][1])
                                print("Question",data[i][2])
                                print("Option-1: ",data[i][3])
                                print("Option-2: ",data[i][4])
                                print("Option-3: ",data[i][5])
                                print("Option-4: ",data[i][6])
                                print("\n")
                            cur.close()
                        
                        elif Admin_choice==6:
                            break
                    break
    
                else:
                    print("Password is In Correct  Enter User Name & Password")
            else:
                print("unvalid User Name Enter User Name & Password")
    else:
        while True:
            print(25*"*"+" Welcome to Quiz "+25*"*")
            print(10*"*"," LOG IN ",10*"*")
            while True:
                User_name=input("Enter UserName: ").upper()
                User_Mobile =input("Enter Mobile no: ")
                print("*"*20)
                if len(User_Mobile)==10:
                    print("1-Take Quiz \n 2-Highest Score ")
                    user_choice=int(input("Enter option 1 or 2: "))
                    if user_choice ==1:
                        cur=db_connection.cursor()
                        cur.execute("SELECT * FROM questions")
                        data=cur.fetchall()
                        
                        Languages=[]    
                        for i in [data[i][1] for i in range(len(data))]:
                            if i not in Languages:
                                Languages.append(i)
                                
                                
                        for i in range(1,len(Languages)+1):
                            print("Enter-",i,":",Languages[i-1])
                            
                        Quiz_Tech_Option=int(input("Enter a Techonology: "))
                        select_query = "SELECT * FROM questions WHERE technology = %s"
                        cur.execute(select_query, (Languages[Quiz_Tech_Option-1],))

                    
                        Quiz_Data=cur.fetchall()
                        
                        Correct=[Quiz_Data[i][7] for i in range(len(Quiz_Data))]
                        User_Answers=[] # To store User Answers
                        
                        Question_cnt=0 # to count the Questions
                        for i in range(len(Quiz_Data)): # To display all the Questions 
                            Question_cnt+=1
                            print(i+1,"Question",Quiz_Data[i][2])
                            print("Option-1: ",Quiz_Data[i][3])
                            print("Option-2: ",Quiz_Data[i][4])
                            print("Option-3: ",Quiz_Data[i][5])
                            print("Option-4: ",Quiz_Data[i][6])
                            user_option=int(input("Enter Correct Option 1 or 2 or 3 or 4: ")) #tacking user answer 
                            User_Answers.append(user_option) # storing answers in one list 
                        correct_answers=0
                        Attempt=0
                        print(User_Answers)
                        print(Correct)
                        Start_time=datetime.now()
                        for i in range(len(User_Answers)):
                            if Correct[i]==User_Answers[i]:
                                correct_answers+=1
                                
                        end_time=datetime.now()
                        Wrong_Answers=Question_cnt-correct_answers
                        entry=datetime.now()
                        insert_query = """INSERT INTO user_details (user_name, mobile_number, score,entry_datetime)VALUES (%s, %s, %s,%s)"""
                        cur.execute(insert_query, (User_name, User_Mobile, correct_answers,entry))
                        db_connection.commit()
                        
                        print("*"*70) 
                        print(" "*80) 
                        print("*"*30,"Your",Languages[Quiz_Tech_Option-1],"is Completed ","*"*30 )
                        print("Name: ",User_name)
                        print("Mobile: ",User_Mobile)
                        print("Total Question: ",len(Quiz_Data))
                        print("time taken:",end_time-Start_time)
                        print("Scorre: ",correct_answers,"/",len(Quiz_Data))
                        print("*"*70) 
                        break
                    cur.close()
                    break
                    
                else:
                    print("Enter 10 digits Mobile number")            
                break  
            break
        
                            
                        
                        