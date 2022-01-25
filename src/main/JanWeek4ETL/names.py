from name_function import get_formatted_name
print("Enter 'q' at any time to quit")
while True:
    s = input("\n Please give me a first name:")
    if s == 'q':
        break
    s1 = input("\n Please give me a last name:")
    if s1 == 'q':
        break
    formatted_name = get_formatted_name(s, s1)
    print(f"\tNeatly formatted name {formatted_name}")