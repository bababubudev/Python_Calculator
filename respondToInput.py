wants_to_rerun = False


def sort_input(input_value) -> object:
    operators = ["+", "-", "*", "/", "^", "%"]
    num_value_dictionary = {}

    operator_dictionary = {
        k: operator_values
        for k, operator_values in enumerate(input_value)
        if input_value[k] in operators
    }

    list_of_operators = list(operator_dictionary)

    range_iterator = 0
    for l in range(len(operator_dictionary) + 1):
        if l >= len(list_of_operators):
            num_value_dictionary[l] = float(
                input_value[range_iterator: len(input_value)])
        else:
            num_value_dictionary[l] = float(
                input_value[range_iterator: list_of_operators[l]])
            range_iterator = list_of_operators[l] + 1

    return operator_dictionary, num_value_dictionary


def respond_response(str):
    value, string = check_response(str)

    print("\n[ ", end='')
    if value == 1:
        if len(str) == len(string):
            print(
                f"Ok see you I guess. Fun fact! You could have just pressed the X up there to faster.", end='')
        else:
            print(
                f"{str.capitalize()}? You mean { string.upper()}? Alright, whatever you say man.", end='')
            wants_to_rerun = True
    elif value == -1:
        if len(str) == len(string):
            print(
                f"Stop wasting my goddamn time with that {string} ass response!", end='')
        else:
            print(
                f"{str.capitalize()}? You mean {string.upper()} ?", end='')
            wants_to_rerun = True
    else:
        print(
            f"Shit man! Is \"{str.upper()}\" all you had to say?! Tell me again clearly.", end='')
    print(" ] \n")


def check_response(player_input) -> object:
    response_p = ["yes", "sure", "okay", "alright", "aight", "go"]
    response_n = ["no", "nah", "sorry"]

    modified_input = player_input.split()[0].lower()
    amount_of_responses = max(len(response_p), len(response_n))
    amount_of_spaces = player_input.count(" ")
    amount_of_words = player_input.count(" ") + 1

    looper = 0 if amount_of_spaces == 0 else 1
    for _ in range(amount_of_words):
        for indexer in range(amount_of_responses):
            if len(modified_input) <= 1:
                first_char = " "
                second_char = " "
            else:
                first_char = modified_input[0]
                second_char = modified_input[1]

            if response_p[indexer].startswith(first_char):
                if response_p[indexer].find(second_char) == modified_input.find(second_char):
                    return 1, response_p[indexer]
            else:
                for item in response_n:
                    if item.startswith(first_char) and item.find(
                        second_char
                    ) == modified_input.find(second_char):
                        return -1, item

        if amount_of_spaces == 0:
            return 0, " "

        modified_input = player_input.split()[looper].lower() if (
            amount_of_spaces > 0) else modified_input.lower()
        looper += 1
        indexer = 0


def ask_response(input_calculation) -> int:
    new_player_input = str(
        input(f"\nAre you sure you want to {input_calculation}? : "))
    value, _ = check_response(new_player_input)
    respond_response(new_player_input)
    return value
