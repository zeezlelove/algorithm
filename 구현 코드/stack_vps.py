def vps(s): # 괄호가 올바른 괄호인지 체크한다.
    st = []
    #여는괄호면 stack에 push하고 닫는괄호면 stack에서 pop한다.
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
print(vps(input()))
