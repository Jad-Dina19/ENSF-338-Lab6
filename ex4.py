import random

class Heap:
    def __init__(self):
        self.data = []

    def heapify(self, arr):
        self.data = arr.copy()

        n = len(self.data)

        for i in range(n//2 - 1, -1, -1):
            self.bubble_down(i)
            

    def bubble_down(self, index):
        n = len(self.data)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            root = index
            
            if (left < n and self.data[left] < self.data[root]):
                root = left
            if (right < n and self.data[right] < self.data[root]):
                root = right
            
            if root == index:
                break

            self.data[index], self.data[root] = self.data[root], self.data[index]
            index = root

    def enqueue(self, value):
        self.data.append(value)
        index = len(self.data) - 1

        while index > 0:
            parent = (index - 1) // 2

            if self.data[parent] <= self.data[index]:
                break

            self.data[parent], self.data[index] = self.data[index], self.data[parent]
            index = parent
    
    def dequeue(self):
        if not self.data:
            return None

        root = self.data[0]
        last = self.data.pop()

        if (self.data):
            self.data[0] = last
            self.bubble_down(0)     

        return root


def sorted_array_test():
    heap = Heap()
    arr = [1,2,3,4,5,6]

    heap.heapify(arr)

    print(f"Sorted Array Test\nThe expected outcome is: {arr}\nWhile the heap result is: {heap.data}")
    if (heap.data == arr):
        print("The test passed the sorted array test!\n")
        return
    print("The test failed the sorted array test.\n")
        
    

def empty_case():
    heap = Heap()

    heap.heapify([])

    print(f"Empty Case Test\nThe expected outcome is: {[]}\nWhile the result is: {heap.data}")
    if (heap.data == []):
        print("The test passed the empty array test!\n")
        return
    print("The test failed the empty array test.\n")       


def random_long_array():
    heap = Heap()
    long_heap = Heap()

    longish_array = [7,2,9,4,1,6,8,3,5]
    long_array = list(range(100))
    shuffled = long_array.copy()
    random.shuffle(shuffled)
    

    heap.heapify(longish_array)
    long_heap.heapify(shuffled)

    print(f"Random Long Array Test\nThe expected min outcome for a longish array is: {min(longish_array)}\nWhile the min result is: {heap.data[0]}\n\
Really Long Array (100 Elements) The expected min outcome is: {min(long_array)}\nWhile the min result is: {long_heap.data[0]}")

    if (heap.data[0] == min(longish_array) and long_heap.data[0] == min(long_array)):
        print("The test passed the long shuffled array test!\n")
        return
    print("The test failed the long shuffled array test.\n")   



def main():
    sorted_array_test()
    empty_case()
    random_long_array()


if __name__ == '__main__':
    main()