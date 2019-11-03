def vps(s):
    st = []
    for i in s:
        if i == "(":
            st.append(i)
        elif i == ")":
            if "(" in st:
                st.pop()
            else:
                return "NO"
    if st:
        return "NO"
    return "YES"
for i in range(int(input())):
    print(vps(input()))
#백준 괄호
