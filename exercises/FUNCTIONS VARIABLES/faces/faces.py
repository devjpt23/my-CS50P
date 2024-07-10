userinput = input("enter something: ")

# "🙂","🙁"
sadFace = ":("
happyFace = ":)"

if sadFace in userinput:
    userinput = userinput.replace(sadFace,"🙁")
if happyFace in userinput:
    userinput = userinput.replace(happyFace,"🙂")
print(userinput)
