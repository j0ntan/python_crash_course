user_names = ['John', 'Isabella', 'Billy', 'Zoey', 'Valerie', 'admin']
for name in user_names:
    if name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {name.title()}, thank you for logging in again.")
