def read_file(file_name):
    print("__CONTENT_START__")
    try:
        file = open(file_name, "r")
        content = file.read()
        print(content)
    except IOError:
        print("__NO_SUCH_FILE__")
    finally:
        print('__CONTENT_END__')


read_file(r"C:\Users\y8463\words.txt")
read_file('imaginaty')