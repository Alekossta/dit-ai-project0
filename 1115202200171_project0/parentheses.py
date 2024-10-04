# We assume our lists will not have any character that is a space
# We assume we want our expressions to have parentheses with two numbers inside

def complete_parentheses(numberExpressionList):
    newList = numberExpressionList.copy()
    parenthesesNum = 0
    sequenceCounter = 0
    # we start the iteration from the end
    for i in range(len(newList) - 1, -1, -1):
        element = newList[i]
        if(element == ")"):
            parenthesesNum += 1
            sequenceCounter = 0
        else:
            sequenceCounter +=1

        if(sequenceCounter == 3 and parenthesesNum > 0):
            newList.insert(i,"(")
            parenthesesNum-=1
            sequenceCounter=1 # set it to 1 because the new complete parentheses counts as new "sequence"


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
exampleExpression4 = ["1", "+", "2", "+", "3", ")"]
hardExpression = ["1", "*", "1", "+", "2", "+", "3", ")", ")"]

print_expression(exampleExpression1)
print_expression(exampleExpression2)
print_expression(exampleExpression3)
print_expression(exampleExpression4)
print_expression(hardExpression)