#this is a rule_based chatbot ;
import random
greeting={"hello","hi","hey","good morning", "greeting","bonjour"}
greeting_response={"Hello! How can I help you today?","Hi there! ","what's up "}
exit={"bye","quit","exit","au revoir","goodbye","see you later","later"}
exit_msg={"Goodbye! Have a great day!", "See you later!","bye"}



print ("welcome to the chatbot py\n")
print("type 'exit' to end the conversation")
while True:
    user_msg=input("BOT: how can i help you ? \nYou: ")
    user_msg=user_msg.lower()
    if user_msg in greeting :
        print("BOT: "+random.choice(list(greeting_response)))   
    elif user_msg=="how are you ?":
        print ("BOT: I am fine how are you ?")
    elif user_msg=="what's your name ?":
        print ("BOT: my name is rule_based chatbot")
    elif "weather" in user_msg:
        if "tomorrow" in user_msg:
            print("BOT: its will be rainy tomorrow")
        elif "today" in user_msg :
            print ("BOT: it's sunny today")
        else :
            print("BOT: sorry , i can't predict the weather for now")
    
    elif user_msg in exit:
        print("BOT:"+random.choice(list(exit_msg)))
        break
    else :
        print("BOT: i can't understand you for the moment . try 'hi'or 'hello ")