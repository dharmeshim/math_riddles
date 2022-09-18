import sqlite3
import random
db = sqlite3.connect('database.db')
c=db.cursor()
c.execute("CREATE TABLE IF NOT EXISTS data(name TEXT , highscore REAL)")
db.commit()

def welcome(name,highscore): # Display the welcoming message 
    print("                    Hello {} ! \n\n                    Welcome to Maths game \n\n                    Your high score : {}\n\n____________________________________________________________\n\n".format(name,highscore))
    input("Press Enter to start")


    
def main():
    print("____________________________________________________________\n\n                         [SIMPLE MATH GAME]\n\n____________________________________________________________\n")
    data=c.execute("SELECT * FROM data")

    # Count the number of the table's rows 
    x=0
    for i in data:
        x=x+1
        
    if x==0: # If empty (first run)
        # Ask about the user name
        ask=True
        while ask:
            try:
                name = input("Please Enter your name : ")
                if name=="" or len(name)==0:
                    print("Please Enter a valid value !")
                else:
                    ask=False                
            except valueError:
                print("Please Enter a valid value")
                askName()
                
        print("\n___________________________________________________________\n")
        c.execute("INSERT INTO data VALUES(?,?)",(name,"0")) # Set the name in database 
        db.commit()  
        welcome(name,"0")
        highscore=0
        
    else: # User played before
        data=c.execute("SELECT * FROM data")
        for i in data: # Get the name and highscore        
            name=i[0]
            highscore=i[1]
        welcome(name,highscore)

    def checkscore(calc,scor):
        rnum=0
        if scor>25:
            rnum =random.randint(14,19)
            calc= calc + rnum
        elif scor>20:
            rnum =random.randint(11,13)
            calc= calc + rnum
        elif scor>15:
            rnum =random.randint(7,10)
            calc= calc + rnum
        elif scor>10:
            rnum =random.randint(5,6)
            calc= calc + rnum
        return(calc)
            


 
    score=0
    lose=False
    numdig=0
    while lose!=True:
        calc=random.randint(0,4) # Generate a random calculation type 0=[+] 1=[*]
        calc=checkscore(calc,score)

        if calc==0: #(+adition)
            firstnum=random.randint(2,10) # First n0umber
            secondnum=random.randint(2,10) # Second number
            result=firstnum+secondnum
            inp="   {} + {} = " # User input text
            numdig=2

        elif calc==1: #(-sub)
            firstnum=random.randint(2,10) # First number
            secondnum=random.randint(2,10) # Second number
            result=firstnum-secondnum
            inp="   {} - {} = " # User input text
            numdig=2

        elif calc==2: #(*mul)
            firstnum=random.randint(2,10) # First number
            secondnum=random.randint(2,10) # Second number
            result=firstnum*secondnum
            inp="   {} x {} = " # User input text
            numdig=2

        elif calc==3: #(+add)
            firstnum=random.randint(2,20) # First number
            secondnum=random.randint(2,20) # Second number
            result=firstnum+secondnum
            inp="   {} + {} = "
            numdig=2

        elif calc==4: #(- sub)
            firstnum=random.randint(2,20) # First number
            secondnum=random.randint(2,20) # Second number
            result=firstnum-secondnum
            inp="   {} - {} = "
            numdig=2

        elif calc==5: #(+add)
            firstnum=random.randint(2,100) # First number
            secondnum=random.randint(2,50) # Second number
            result=firstnum+secondnum
            inp="   {} + {} = "
            numdig=2

        elif calc==6: #(-sub)
            firstnum=random.randint(2,50) # First number
            secondnum=random.randint(2,40) # Second number
            result=firstnum-secondnum
            inp="   {} - {} = "
            numdig=2

        elif calc==7: #(+add)
            firstnum=random.randint(2,50) # First number
            secondnum=random.randint(-10,10) # Second number
            result=firstnum+secondnum
            inp="   {} + {} = "
            numdig=2

        elif calc==8: #(+addition)
            firstnum=random.randint(2,100) # First number
            secondnum=random.randint(2,100) # Second number
            result=firstnum+secondnum
            inp="   {} + {} = "
            numdig=2

        elif calc==9: #(-sub)
            firstnum=random.randint(2,100) # First number
            secondnum=random.randint(2,50) # Second number
            result=firstnum-secondnum
            inp="   {} - {} = "
            numdig=2

        elif calc==10: #(+addition)
            firstnum=random.randint(2,50) # First number
            secondnum=random.randint(2,10)
            thirdnumber=random.randint(2,100) 
            result = firstnum + secondnum + thirdnumber
            inp="   {} + {} + {} = "
            numdig=3

        elif calc==11: #(- sub)
            firstnum=random.randint(2,100) # First number
            secondnum=random.randint(2,50) # Second number
            thirdnumber=random.randint(2,10) 
            result = firstnum + secondnum - thirdnumber
            inp="   {} + {} - {}= "
            numdig=3

        elif calc==12: #(- sub)
            firstnum=random.randint(2,100) # First number
            secondnum=random.randint(2,50) # Second number
            thirdnumber=random.randint(2,10) 
            result = firstnum + secondnum - thirdnumber
            inp="   {} + {} - {}= "
            numdig=3

        elif calc==13: #(+addition)
            firstnum=random.randint(2,100) # First number
            secondnum=random.randint(2,100) # Second number
            result=firstnum+secondnum
            inp="   {} + {} = "
            numdig=2

        elif calc==14: #(*mul)
            firstnum=random.randint(2,50) # First number
            secondnum=random.randint(2,10) # Second number
            result=firstnum * secondnum
            inp="   {} x {} = "
            numdig=2

        elif calc==15: #(+add *mul)
            firstnum=random.randint(2,10) # First number
            secondnum=random.randint(2,10)
            thirdnumber=random.randint(2,5) 
            result = firstnum + secondnum * thirdnumber
            inp="   {} + {} x {} = "
            numdig=3

        elif calc==16: #(+addition)
            firstnum=random.randint(100,500) # First number
            secondnum=random.randint(100,500)
            thirdnumber=random.randint(2,100) 
            result = firstnum + secondnum + thirdnumber
            inp="   {} + {} + {} = "
            numdig=3

        elif calc==17: #(+add -sub)
            firstnum=random.randint(100,500) # First number
            secondnum=random.randint(100,500)
            thirdnumber=random.randint(2,100) 
            result = firstnum + secondnum - thirdnumber
            inp="   {} + {} - {} = "
            numdig=3

        elif calc==18: #(+addition)
            firstnum=random.randint(100,500) # First number
            secondnum=random.randint(100,500)
            thirdnumber=random.randint(2,100) 
            result = firstnum + secondnum - thirdnumber
            inp="   {} + {} - {} = "
            numdig=3

        else: #(*multiplication)
            firstnum=random.randint(2,10)
            secondnum=random.randint(2,10)
            thirdnumber=random.randint(2,10) 
            result = firstnum * secondnum * thirdnumber
            inp="   {} x {} x {} = "
            numdig=3

            
        def askUser(): # Ask user 
                if numdig==2:
                    qstring=inp.format(firstnum,secondnum)
                    userInput=input(qstring)
                elif numdig==3:
                    qstring=inp.format(firstnum,secondnum,thirdnumber)
                    userInput=input(qstring)
                try:
                    userInput=int(userInput) 
                    return userInput
                except: # If user input a text or left it empty
                    print("Enter a valid value")
                    askUser()# Reask again
                #return (qstring)
        userInput=askUser()
        
        if userInput==result: # Correct answer 
             score=score+1 
             if score>highscore: # If this score is the high score 
                 c.execute("UPDATE data SET highscore =  ? WHERE name = ?",(score,name)) # Change highscore in database
                 db.commit()
                 print("Correct ! , High score ! your score : {} \n".format(score)) # Show message
             else: # The score is not the highscore
                 print("Correct ! your score : {}\n".format(score))

        else: # Wrong answer
            score=0
            print("Oops ! Wrong Answer!\n")
            userAgain=input("Press y to play again!! (y,n) : ").lower()
            if userAgain=="n":
                print("Good bye !")
            
                db.close()
                lose=True
                main()
main()

