def arithmetic_arranger(problems, give_solutions = False):
    arranged_problems = ''
    try:
        err_key = error_handler(problems)
        if err_key:
            return get_err_msg(err_key)
          
        top_nums = ''
        bot_nums = ''
        bot_line = ''
        solutions = ''
        for problem in problems:
            p_split = problem.split()
            total_width = max([len(num) for num in p_split if num.isdigit()]) + 2
            justify = total_width + 4
            top_nums += p_split[0].rjust(total_width).ljust(justify)
            bot_nums += p_split[1] + p_split[2].rjust(total_width -1).ljust(justify - 1)
            bot_line += ('-' * total_width).ljust(justify)
            # future me: manual parsing is safer
            solutions += str(eval(problem)).rjust(total_width).ljust(justify)
        new_probs = [top_nums[:-4], bot_nums[:-4], bot_line[:-4]]
        if give_solutions:
            new_probs.append(solutions[:-4])
        arranged_problems += '\n'.join(new_probs)
        return arranged_problems
  
    except Exception as e:
        return handle_def_err() + "\nDetails: " + str(e)
        
def error_handler(problems):
    if len(problems) > 5:
        return 'too_many'
    for problem in problems:
        p_split = problem.split()
        if len(p_split) != 3:
            return 'format_err'
        if p_split[1] not in ['+', "-"]:
            return 'wrong_oper'
        if not (p_split[0].isdigit() and p_split[2].isdigit()):
            return 'not_num'
        if len(p_split[0]) > 4 or len(p_split[2]) > 4:
            return 'too_long'
    return None

def handle_too_many():
    return 'Error: Too many problems.'
def handle_wrong_oper():
    return 'Error: Operator must be ' + "'" + '+' + "'" + ' or ' + "'" + '-' + "'."
def handle_not_num():
    return 'Error: Numbers must only contain digits.'
def handle_too_long():
    return 'Error: Numbers cannot be more than four digits.'
def handle_format_err():
    return 'Error: Problems need 2 operands and 1 operator.'
def handle_def_err():
    return 'Error: Something went wrong!'

err_switch = {
  'too_many': handle_too_many,
  'wrong_oper': handle_wrong_oper,
  'not_num': handle_not_num,
  'too_long': handle_too_long,
  'format_err': handle_format_err
}

def get_err_msg(err_key):
    return err_switch.get(err_key, handle_def_err)()
