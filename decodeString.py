class Solution:
    def decodeString(self, s: str) -> str:

        def digit_checker(s, count):
            if s[count].isdigit():
                num = ""
                while s[count].isdigit():
                    num += s[count]
                    count += 1
                multiplier_stack.append(int(num))
            return count

        multiplier_stack = []
        string_stack = []
        count = 0

        while s:
            if ']' in s[count:]:
                temp = ""
                while s[count] != ']':
                    count = digit_checker(s, count)
                    temp += s[count]
                    count += 1

                if temp:
                    string_stack.append(temp)
                else:
                    temp = string_stack[-1]

                temp_index = len(temp) - 1
                while temp[temp_index] != '[':
                    temp_index -= 1
                    if temp_index < 0:
                        string_stack.pop()
                        temp = string_stack[-1] + temp
                        temp_index = len(string_stack[-1]) - 1

                temp = temp[:temp_index] + temp[temp_index + 1:] * multiplier_stack.pop()
                string_stack.pop()
                string_stack.append(temp)
                count += 1
            else:
                if s[count:]:
                    string_stack.append(s[count:])
                s = ""
                break

        return ''.join(string_stack)