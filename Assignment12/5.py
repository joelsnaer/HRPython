#game_of_eights() function goes here
def game_of_eights(a_list):
    for x, value in enumerate(a_list):
        if x+1 < len(a_list):
            if int(a_list[x]) == 8 and int(a_list[x+1]) == 8:
                return True
    return False

def main():
    a_list = input("Enter elements of list separated by commas: ").split(',')
    # remainder of main() goes here
    letterCheck = [letter for letter in a_list if letter.isalpha()]
    if len(letterCheck) > 0:
        print("Error. Please enter only integers.")
    else:
        print(game_of_eights(a_list))
main()