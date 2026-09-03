from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        result = []
        currentLine = []
        currentLength = 0

        for word in words:

            requiredLength = (
                currentLength
                + len(word)
                + len(currentLine)
            )

            if requiredLength <= maxWidth:
                currentLine.append(word)
                currentLength += len(word)

            else:
                # Current line ko justify karo
                spaces = maxWidth - currentLength
                gaps = len(currentLine) - 1

                if gaps == 0:
                    line = currentLine[0] + " " * spaces
                else:
                    spacePerGap = spaces // gaps
                    extraSpaces = spaces % gaps

                    line = ""

                    for i in range(gaps):
                        line += currentLine[i]
                        line += " " * (
                            spacePerGap + (1 if i < extraSpaces else 0)
                        )

                    line += currentLine[-1]

                result.append(line)

                # New line
                currentLine = [word]
                currentLength = len(word)

        # Last line → left aligned
        line = " ".join(currentLine)
        line += " " * (maxWidth - len(line))
        result.append(line)

        return result
