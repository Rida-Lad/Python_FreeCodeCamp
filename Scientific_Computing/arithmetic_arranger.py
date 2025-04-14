def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    top_lines = []
    bottom_lines = []
    dash_lines = []
    answer_lines = []
    
    for problem in problems:
        parts = problem.split()
        num1, operator, num2 = parts
        
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
            
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        width = max(len(num1), len(num2)) + 2
        top_line = num1.rjust(width)
        bottom_line = operator + ' ' + num2.rjust(width - 2)
        dash_line = '-' * width
        
        top_lines.append(top_line)
        bottom_lines.append(bottom_line)
        dash_lines.append(dash_line)
         
        if show_answers:
            if operator == '+':
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            answer_line = answer.rjust(width)
            answer_lines.append(answer_line)
    
    arranged_problems = "    ".join(top_lines) + "\n"
    arranged_problems += "    ".join(bottom_lines) + "\n"
    arranged_problems += "    ".join(dash_lines)
    
    if show_answers:
        arranged_problems += "\n" + "    ".join(answer_lines)
    
    return arranged_problems