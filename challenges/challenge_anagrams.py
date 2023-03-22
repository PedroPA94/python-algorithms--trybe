# Merge sort adaptado do algortimo proposto no livro 'Estrutura de dados
# e algoritmos com JavaScript', 2ª ed.


def merge_sort(word: str) -> str:
    if len(word) > 1:
        mid = len(word) // 2
        left = merge_sort(word[:mid])
        right = merge_sort(word[mid:])
        word = merge(left, right)
    return word


def merge(left: str, right: str) -> str:
    merged_word = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_word.append(left[i])
            i += 1
        else:
            merged_word.append(right[j])
            j += 1

    merged_word += left[i:] if i < len(left) else right[j:]

    return "".join(merged_word)


def is_anagram(first_string: str, second_string: str) -> bool:
    sorted_first = merge_sort(first_string.lower())
    sorted_second = merge_sort(second_string.lower())

    if not sorted_first or not sorted_second:
        comparison = False
    else:
        comparison = sorted_first == sorted_second

    return (sorted_first, sorted_second, comparison)
