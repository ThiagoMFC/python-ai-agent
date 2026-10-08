from functions.write_file import write_file

print(write_file("calculator", "lorem_ipsum.txt", "overwriting file"))
print(write_file("calculator", "pkg/more.txt", "what file is this"))
print(write_file("calculator", "tmp/temp.txt", "also don't exist"))
print(write_file("calculator", "pkg", "not even a file"))