### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    #Students do not have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
    if question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    if question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the MD5 hashing value to the following message: 'NYU Computer Networking'- Use MD5 hash generator and use the answer in your code":
        answer = "42b76fe51778764973077a5a94056724"
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question == "What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number":
        answer = "5"
    elif question == "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number":
        answer = "4"
    return (answer)
   

        ### you should understand why this else case should be included
        ### what happens if there is a typo in one of the questions?
        ### maybe put something here to flag an issue and catch errors
answer = "This is not my beautiful wife! This is not my beautiful car! How did I get here?"

# Complete all the questions.


if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))
    debug_question = "Is it possible to decrypt a message without a key? - Yes/No"
    print(welcome_assignment_answers(debug_question))
    debug_question = "Is it possible to decode a message without a key? - Yes/No"
    print(welcome_assignment_answers(debug_question))
    debug_question = "Is a hashed message supposed to be un-hashed? - Yes/No"
    print(welcome_assignment_answers(debug_question))
    debug_question = "What is the MD5 hashing value to the following message: 'NYU Computer Networking'- Use MD5 hash generator and use the answer in your code"
    print(welcome_assignment_answers(debug_question))
    debug_question = "Is MD5 a secured hashing algorithm? - Yes/No"
    print(welcome_assignment_answers(debug_question))
    debug_question = "What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number"
    print(welcome_assignment_answers(debug_question))
    debug_question = "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number"
    print(welcome_assignment_answers(debug_question))
    

#Questions:
#"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
#"Are encoding and encryption the same? - Yes/No":
#"Is it possible to decrypt a message without a key? - Yes/No":
#"Is it possible to decode a message without a key? - Yes/No":
#"Is a hashed message supposed to be un-hashed? - Yes/No":
#"What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
#"Is MD5 a secured hashing algorithm? - Yes/No":
#"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
#"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number": 
