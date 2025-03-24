from typing import List

def loss(
        preferences: List[int],
        allocations: List[int]
) -> int:
    """
    loss = 0
    for i in range(len(allocations)):
        loss += preferences[i].index(allocations[i])
    return loss"
    """""
    pass

def calculate_allocation(
        student_number: int,
        topic_number: int,
        preferences: List[int]
) -> List[int]:
    min_loss = float("inf")
    allocations = None

    def dfs(trace, prev_loss):
        nonlocal min_loss
        nonlocal allocations
        if len(trace) == student_number:
            if prev_loss < min_loss:
                min_loss = prev_loss
                allocations = trace
            return 
        
        cur = len(trace)
        for topic in range(topic_number):
            if topic not in trace:
                cur_loss = preferences[cur].index(topic) if topic in preferences[cur] else topic_number
                if prev_loss + cur_loss < min_loss: dfs(trace + [topic], prev_loss + cur_loss)
    dfs([], 0)
    return allocations


if __name__ == "__main__":
    student_number = 5
    topic_number = 5
    preferences = [[0, 1, 2, 4, 3], [0, 1, 3, 2, 4], [1, 2, 0, 3, 4], [3, 2, 0, 1, 4], [1, 3, 2, 4, 0]]
    allocations = calculate_allocation(student_number=student_number, topic_number=topic_number, preferences=preferences)
    print(allocations)
