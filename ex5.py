import random
import timeit


class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class ListPriorityQueue:
    def __init__(self):
        self.head = None
        self.size = 0

    def enqueue(self, value):
        new_node = LinkedListNode(value)
        if self.head is None or value < self.head.value:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return
        current = self.head
        while current.next is not None and current.next.value <= value:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def dequeue(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value

    def is_empty(self):
        return self.head is None


class HeapPriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, value):
        self.heap.append(value)
        self._bubble_up(len(self.heap) - 1)

    def dequeue(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        minimum = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return minimum

    def is_empty(self):
        return len(self.heap) == 0

    def _bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def _bubble_down(self, index):
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            index = smallest


def generate_tasks(n=1000, seed=42):
    random.seed(seed)
    tasks = []
    for _ in range(n):
        if random.random() < 0.7:
            tasks.append(("enqueue", random.randint(1, 100000)))
        else:
            tasks.append(("dequeue", None))
    return tasks


def process_tasks(queue, tasks):
    for operation, value in tasks:
        if operation == "enqueue":
            queue.enqueue(value)
        else:
            queue.dequeue()


def benchmark(queue_class, tasks, repeats=10):
    total_time = timeit.timeit(lambda: process_tasks(queue_class(), tasks), number=repeats)
    total_tasks = len(tasks) * repeats
    average_time_per_task = total_time / total_tasks
    return total_time, average_time_per_task


if __name__ == "__main__":
    tasks = generate_tasks()

    list_total_time, list_average_time = benchmark(ListPriorityQueue, tasks)
    heap_total_time, heap_average_time = benchmark(HeapPriorityQueue, tasks)

    print("ListPriorityQueue")
    print(f"Overall time: {list_total_time:.8f} seconds")
    print(f"Average time per task: {list_average_time:.12f} seconds")

    print()

    print("HeapPriorityQueue")
    print(f"Overall time: {heap_total_time:.8f} seconds")
    print(f"Average time per task: {heap_average_time:.12f} seconds")

    print()

    if heap_total_time < list_total_time:
        print("discussion: HeapPriorityQueue is faster overall because heap operations are O(log n), while inserting into the linked-list priority queue requires O(n) time to keep the list sorted. Dequeue is O(1) for the list and O(log n) for the heap, but the workload has many more enqueue operations than dequeue operations, so the heap's better insertion efficiency usually wins.")
    elif list_total_time < heap_total_time:
        print("discussion: ListPriorityQueue is faster overall in this run, likely because the constants for this specific workload favored the linked-list approach. In general, however, heaps usually scale better because enqueue is O(log n) instead of O(n).")
    else:
        print("discussion: Both implementations performed the same in this run. In general, heaps are usually faster for larger workloads because enqueue is O(log n), while ordered linked-list insertion is O(n).")