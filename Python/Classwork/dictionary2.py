quiz = {
    1 :{
        "que" : "most popular programming languauge",
        "ans" : "python"
    },
    2 :{
        "que" : "prime minister of India",
        "ans" : "Narendra Modi"
    }
    
}

for i  in range(1,len(quiz)+1):
    print(quiz[i]['que'])
    ans = input("enter the answer : ")#.lower() for lower casing the answer but can be problemetic
    if ans == quiz[i]['ans']:
        print("right answer")
    else:
        print("wrong answer")