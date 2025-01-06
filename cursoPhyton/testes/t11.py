def convert_time_to_ascii(time_str):
    paterns = {
        '0': [" _ ", 
              "| |", 
              "|_|"],

        '1': ["   ", 
              "  |", 
              "  |"],

        '2': [" _ ", 
              " _|", 
              "|_ "],

        '3': [" _ ", 
              " _|", 
              " _|"],

        '4': ["   ", 
              "|_|", 
              "  |"],

        '5': [" _ ", 
              "|_ ", 
              " _|"],

        '6': [" _ ", 
              "|_ ", 
              "|_|"],

        '7': [" _ ", 
              "  |", 
              "  |"],

        '8': [" _ ", 
              "|_|", 
              "|_|"],

        '9': [" _ ", 
              "|_|", 
              " _|"]
    }
    
    lines = ["", "", ""]
    
    hours, minutes = time_str.split(":")
    
    for i, part in enumerate([hours, minutes]):
        for j, char in enumerate(part):
            digit_segments = paterns[char]
            lines[0] += digit_segments[0] + (" " if j < 1 else "")
            lines[1] += digit_segments[1] + (" " if j < 1 else "")
            lines[2] += digit_segments[2] + (" " if j < 1 else "")
        
        if i == 0:
            for k in range(3):
                if k != 0:
                    lines[k] += " . "
                else:
                    lines[k] += '   '
            
    lines = [line.rstrip() for line in lines]
    
    return "\n".join(lines)


print(convert_time_to_ascii("18:15"))