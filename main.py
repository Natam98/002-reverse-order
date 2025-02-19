def get_integer(prompt="Enter a integer: ") -> int|bool:
    try:
        integer=float(input(prompt))
        if integer.is_integer():
            return int(integer)
        else:
            return False
    except ValueError:
        print("invalid input!")
        return False

def integers_list() -> list:
    integers_list=[]
    is_valid_input=True
    while is_valid_input:
        integer=get_integer("Enter an integer (0 to quit): ")
        if integer is not False:
            if integer!=0:
                integers_list.append(integer)
            else:
                is_valid_input=False
    return integers_list


def main():
    list_of_integers=integers_list()
    print("The entered integers in reverse order:")
    for integer in sorted(list_of_integers, reverse=True):
        print(integer)

if __name__=="__main__":
    main()