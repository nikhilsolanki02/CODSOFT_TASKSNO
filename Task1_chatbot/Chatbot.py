# defining a function to handle chatbot responses
# using simple if-else statements to determine the response based on user input

def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! Kaise help kar sakta hoon?"
    elif "how are you" in user_input:
        return "Main theek hoon, aap batao!"
    elif "bye" in user_input:
        return "Bye! Milte hain phir."
    else:
        return "Mujhe samajh nahi aaya, phir se try karo."

# using a while loop to continuously take user input and provide responses until the user says "bye"

while True:
    user_input = input("Aap: ")
    if "bye" in user_input.lower():
        print("Bot:", chatbot_response(user_input))
        break
    print("Bot:", chatbot_response(user_input))

    # thankyou this is the end of the code for the chatbot.