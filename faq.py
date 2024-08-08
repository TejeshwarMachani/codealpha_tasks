faqs = {
    "What is your name?": "I am a simple chatbot.",
    "How can I help you?": "I can answer your questions based on the FAQ list.",
    "What is Python?": "Python is a high-level, interpreted programming language with dynamic semantics.",
    "What is AI?": "AI stands for Artificial Intelligence, which is the simulation of human intelligence in machines.",
    "How do I install Python?": "You can install Python from the official website https://www.python.org/ by downloading the installer for your operating system.",
    "Goodbye": "Goodbye! Have a great day!",
}

def get_response(question):
    # Convert the question to lowercase to make it case-insensitive
    question = question.strip().lower()

    # Check if the question is in the FAQs
    for faq, response in faqs.items():
        if faq.lower() == question:
            return response
    
    # Default response if the question is not recognized
    return "I'm sorry, I don't have an answer for that. Please try asking something else."

# Example usage
if __name__ == "__main__":
    print("Hello! I'm a chatbot. Ask me anything or type 'Goodbye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "goodbye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = get_response(user_input)
        print(f"Chatbot: {response}")
