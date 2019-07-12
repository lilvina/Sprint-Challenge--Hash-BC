#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    index = 0

    for w in weights:
        hash_table_insert(ht, w, index)
        index += 1

    for i in range(len(weights)):
        pair = limit - weights[i] #value we are looking for
        # check to see if pair exists
        answer_pair = hash_table_retrieve(ht, pair)
        if answer_pair is not None:
            print(answer_pair, i)
            return(answer_pair, i)

    return None


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

test_weights = [21, 0]
test_limit = 21

get_indices_of_item_weights(test_weights, len(test_weights), test_limit)
