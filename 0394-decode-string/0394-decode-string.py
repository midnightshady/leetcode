class Solution(object):
    def decodeString(self, s):
        num_stack = []
        str_stack = []

        curr_num = 0
        curr_str = ""

        for ch in s:

            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)

            elif ch == "[":
                num_stack.append(curr_num)
                str_stack.append(curr_str)

                curr_num = 0
                curr_str = ""

            elif ch == "]":
                repeat = num_stack.pop()
                prev = str_stack.pop()

                curr_str = prev + curr_str * repeat

            else:
                curr_str += ch

        return curr_str
            
