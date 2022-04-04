import operator
import time
from os import system, name

import operatorList
import respondToInput as response_man

calculation = ""
history = []
ops = operatorList.ops
wants_response = response_man.wants_to_rerun


def clear():
    cleared = True
    _ = system('cls') if name == 'nt' else system('clear')


def store_history(str):
    for _ in range(1):
        history.append(str)


def show_results(_calculation, _result, _missing_operator=False, _is_eval=False):
    if _missing_operator:
        output = f"[ {_calculation} = {_calculation} ]"
    else:
        output = f"[ {_calculation} = {_result} ]"

    store_history(output)
    print(f"\n {output} \n")


command_dic = {
    "Close program.": "end",
    "Clear screen.": "clear",
    "Check calculation history.": "history",
    "Clear calculation history.": "clh",
    "List all the commands.": "cmdl",
    "Force end the program.": "fend",
}

print(f"\nType \"cmdl\" to see the list of commands.")
commands = list(command_dic)


def main():
    while True:
        try:
            calculation = input("Input: ").lower()
            better_result = eval(calculation)

            result = 0
            operator_dic, value_dic = response_man.sort_input(calculation)
            operator_list = list(operator_dic)
            value_list = list(value_dic)

            if not operator_list:
                show_results(calculation, result, True)
                continue

            print()
            for i in range(len(operator_list)):
                if i == 0:
                    result = ops[operator_dic[operator_list[i]]](
                        value_dic[value_list[i]], value_dic[value_list[i + 1]])
                else:
                    result = ops[operator_dic[operator_list[i]]](
                        result, value_dic[value_list[i + 1]])

            result = int(result) if result - int(result) == 0 else result
            show_results(calculation, result)
        except:
            value = 0
            want_to_break = False
            want_to_pass = False

            #Close program#
            if calculation == command_dic[commands[0]].lower():
                while (value == 0):
                    value = response_man.ask_response(calculation)
                    if value == -1:
                        want_to_pass = True
                    elif value == 1:
                        for timing in range(5):
                            b = "Shutting down in: " + (f" {5 - timing}")
                            print(b, end="\r")
                            time.sleep(1)
                        want_to_break = True
                if want_to_break:
                    break
            #Clear screen#
            elif calculation == command_dic[commands[1]].lower():
                clear()
            #Check calculation history#
            elif calculation == command_dic[commands[2]].lower():
                if history:
                    print("\n")
                    for element in history:
                        print(element)
                    print("\n")
                else:
                    print("Nothing to show in the history!\n")
            #Clear calculation history#
            elif calculation == command_dic[commands[3]].lower():
                history.clear()
                print("History cleared.\n")
            #List all the commands#
            elif calculation == command_dic[commands[4]].lower():
                for cmd in commands:
                    print("[", command_dic[cmd], "] = ", cmd)
                print("\n")
            #Force end the program#
            elif calculation == command_dic[commands[5]].lower():
                print("\n[ FORCE ENDING! ]\n")
                break
            else:
                print(
                    f"\nInvalid input operation: [ {calculation} ]. \nType \"cmdl\" to check the command list \n")


if __name__ == "__main__":
    main()
