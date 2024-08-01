'''FLAMES is a popular game named after the acronym: friends, lovers, affectionate, marriage, enemies, and siblings. This game does not predict whether an individual is right for you. There are few steps in the game
1) Take two names on which you wanna perform flames.
2) Remove the common characters from both the names. 
3) Get the remaining characters and add them to a variable called count
4) Take a character array for F, L, A, M, E, S
5) Start removing letters from F, L, A, M, E, S using the count we got.  
6) the letter that will be left at last using the  count is the result 
input format 
there will be 2 players named player1& player2
output format
status = result
'''
def flames(player1, player2):
    # Convert names to lowercase and remove common characters
    name1 = set(player1.lower())
    name2 = set(player2.lower())
    common_chars = name1.intersection(name2)
    name1 = name1 - common_chars
    name2 = name2 - common_chars

    # Calculate count
    count = len(name1) + len(name2)

    # Define FLAMES array
    flames_array = ['F', 'L', 'A', 'M', 'E', 'S']

    # Remove letters from FLAMES array using count
    index = 0
    while len(flames_array) > 1:
        index = (index + count - 1) % len(flames_array)
        flames_array.pop(index)

    # Get result
    result = flames_array[0]

    # Map result to status
    status_map = {
        'F': 'Friends',
        'L': 'Lovers',
        'A': 'Affectionate',
        'M': 'Marriage',
        'E': 'Enemies',
        'S': 'Siblings'
    }
    status = status_map[result]

    return status

# Example usage:
player1 = input("Enter player 1's name: ")
player2 = input("Enter player 2's name: ")
status = flames(player1, player2)
print(f"Status = {status}")

# Add a feature to play again
play_again = input("Do you want to play again? (yes/no): ")
while play_again.lower() == "yes":
    player1 = input("Enter player 1's name: ")
    player2 = input("Enter player 2's name: ")
    status = flames(player1, player2)
    print(f"Status = {status}")
    play_again = input("Do you want to play again? (yes/no): ")