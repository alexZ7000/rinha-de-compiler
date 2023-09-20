import main

while True:
    text = input('basic > ')
    text = text.strip()
    result, error = main.run(text)

    if error:
        print(error.as_string())
    else:
        print(result)
