# We assume our lists will not have any character that is a space
# We assume we want our expressions to have parentheses with two numbers inside

allowedOperators = ["*", "+", "-", "^", "/"]

def complete_parentheses(numberExpressionList):
    newList = numberExpressionList.copy()
    parenthesesNum = 0
    operatorCounter = 0
    operandCounter = 0
    # we start the iteration from the end
    for i in range(len(newList) - 1, -1, -1):
        element = newList[i]
        if(element in allowedOperators):
            operatorCounter+=1
        elif(element == ")"):
            parenthesesNum+=1
        else: #will be a number
            operandCounter+=1

        if(operandCounter == 2 and operatorCounter >= 1):
            newList.insert(i, "(")
            operandCounter-=2
            parenthesesNum-=1
            operatorCounter-=1
            if(operatorCounter > parenthesesNum - 2):
                newList.insert(i,"(")
                parenthesesNum-=1


    for i in range(1,parenthesesNum+1):
        newList.insert(0,"(")

    return newList
        

def print_expression(expression):
    print("---Old Expression---")
    print(expression)
    print("---Complete Expression---")
    newExpression = complete_parentheses(expression)
    print(newExpression)

exampleExpression1 = ["1","+","2",")","*","3","-","4",")","*","5","-","6",")",")",")"]
exampleExpression2 = [")"]
exampleExpression3 = ["0",")"]

print_expression(exampleExpression1)
print_expression(exampleExpression2)
print_expression(exampleExpression3)