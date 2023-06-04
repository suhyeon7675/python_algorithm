def solution(participant, completion):
    participant = { i:p for i, p in enumerate(sorted(participant))}
    completion = { i:c for i, c in enumerate(sorted(completion))}
    for k in participant:
        if k not in completion:
            return participant[k]
        elif participant[k] != completion[k]:
            return participant[k]
