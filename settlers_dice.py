from collections import Counter;
import random;

#settlers_weights = {
#    2: 1,
#    3: 2,
#    4: 3,
#    5: 4,
#    6: 5,
#    7: 6,
#    8: 5,
#    9: 4,
#    10: 3,
#    11: 2,
#    12: 1
#}

test_weights = {
        1: 1,
        2: 2,
        3: 3
}


class SettlersDice:
    def __init__(self, orig_weights):
        print ('hello world')
        
        self.history = []
        self.history_cycle = []
        self.orig_weights = orig_weights.copy()

        self.roll_count = 0
        self.curr_weights = self.orig_weights.copy()

        self.cycle = sum(self.orig_weights.values())

    def roll(self):
        if (self.roll_count == self.cycle):
            self._update_weights()
            self.roll_count = 0
        
        return self._roll(self.curr_weights)

    def show_history(self):
        print(self.history + self.history_cycle)

    def show_all_rolls(self):
        print ('todo')
        # think more about

    def verify_distribution(self):
        print ('todo')


    def _update_weights(self):
        self.history += self.history_cycle

        cnt = Counter()
        for val in self.history_cycle:
            cnt[val] += 1

        print (cnt)

        # minimum should never be 0
        for val, weight in self.curr_weights.items():
            self.curr_weights[val] = weight - (cnt[val] - self.orig_weights[val]);
            
        if 0 in self.curr_weights.values():
            self.curr_weights = self._adjust_for_zero(self.curr_weights)

        self.history_cycle = []


    def _adjust_for_zero(self, val_weights):
        while 0 in val_weights.values():
            print ('Adjusting for 0')

            max_weighted_val = max(val_weights, key=val_weights.get)
            min_weighted_val = min(val_weights, key=val_weights.get)

            val_weights[max_weighted_val] -= 1
            val_weights[min_weighted_val] += 1

        return val_weights


    def _roll(self, val_weights):
        weighted_val_list = []
        for val in val_weights.keys():
            weighted_val_list += [val] * val_weights[val]

        self.roll_count += 1

        rolled_val = random.choice(weighted_val_list)
        self.history_cycle += [rolled_val]

        return rolled_val


testDice = SettlersDice(test_weights)
for i in range(19):
    print(testDice.roll())
testDice.show_history()
