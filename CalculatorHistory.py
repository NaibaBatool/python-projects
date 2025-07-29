# Calculator with history

calHistory="history.txt"

def showHistory():
    file=open(calHistory,'r')
    lines=file.readline()
    if len(lines) == 0:
        print("No history found\n")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clearHistory():
    file=open(calHistory,'w')
    file.close()
    print("History Cleared! \n")

def saveToHistory(equation, result):
    file=open(calHistory,'a')
    file.write(equation +"="+ str(result)+"\n")
    file.close()

def calculate(userInput):
    parts = userInput.split()
    if len(parts) !=3:
        print("Invalid operator! Use Format: number operator number (e.g: 7+3)")
        return
    
    num1= float(parts[0])
    op=parts[1]
    num2= float(parts[2])

    if op=='+':
        result=num1+num2
    elif op=='-':
        result=num1-num2
    elif op=='*':
        result=num1*num2
    elif op=='/':
        if(num2!=0):
            result=num1/num2
        else:
            print("DivideWithZero Error!\n")
    else:
        print("Invalid operator. use only(+,-,*,/) \n")

    if int(result) == result:
        result = int(result)
    print("Result:",result)
    saveToHistory(userInput,result)

def main():
    print('---SIMPLE CALCULATOR (type history,clear or exist)')
    while True:
        displayInput=input("Enter calculation (+, -, *, /) or command (history, clear,exist) :")
        if displayInput=='exist':
            print("Goodbye\n")
            break
        elif displayInput=="clear":
            clearHistory()
            break
        elif displayInput=="history":
            showHistory()
            break
        else:
            calculate(displayInput)

main()
