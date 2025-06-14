def func_to_do_notes():
    to_do_notes = []

    while True:
        note = input()

        if note == "End":
            break
        to_do_notes.append(note)

    sorted_notes = sorted(to_do_notes, key= lambda x: int(x.split("-")[0]))
    sorted_final_notes = [note.split("-")[1] for note in sorted_notes]
    return sorted_final_notes

result = func_to_do_notes()
print(result)