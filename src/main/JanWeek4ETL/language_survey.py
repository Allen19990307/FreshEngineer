from survey import AnonymousServey

question = "what language did you firsy learn to speak?"
my_servey = AnonymousServey(question)
# 显示问题并且能够存储答案
my_servey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    s = input("Language:")
    if s == 'quit':
        break
    my_servey.store_response(s)
print("\n Thank you to everyone who participated in the survey!")
my_servey.show_results()
