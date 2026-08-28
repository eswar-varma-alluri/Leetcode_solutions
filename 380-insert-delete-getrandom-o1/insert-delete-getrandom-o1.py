import random

class RandomizedSet:

    def __init__(self):
        self.val_list = []          # Stores the actual values
        self.val_to_index = {}      # Maps value -> index in val_list

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        
        # Add the new value to the end of the list and record its index
        self.val_to_index[val] = len(self.val_list)
        self.val_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        
        # Get the index of the element to remove and the last element in the list
        idx_to_remove = self.val_to_index[val]
        last_val = self.val_list[-1]
        
        # Move the last element to the position of the element being removed
        self.val_list[idx_to_remove] = last_val
        self.val_to_index[last_val] = idx_to_remove
        
        # Remove the target element from the list and dictionary
        self.val_list.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.val_list)