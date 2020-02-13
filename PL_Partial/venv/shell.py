import mamba

while True:
    text = input('out: ')
    result, error = mamba.run('<stdin>',text)

    if error: print(error.as_string())
    else: print(result)