from collections import Counter;
from collections import defaultdict;
import random;

settlers_weights = {
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    7: 6,
    8: 5,
    9: 4,
    10: 3,
    11: 2,
    12: 1
}

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
        print ('Verifying Distribution')

        self.history += self.history_cycle
        dist = defaultdict(list)

        while (self.history != []):
            # print ('----------------------------')
            cnt = Counter()
            for r in self.history[0:self.cycle]:
                cnt[r] += 1

            #print 'range of history processing'
            #print (cnt)

            weights = {}

            for val in cnt.keys():
                weights[val] = cnt[val]

            #print 'weight according to cnt'
            #print (weights)

            for val in weights.keys():
                weights[val] = weights[val] - self.orig_weights[val]

            #print 'weight after math'
            #print (weights)

            self.history = self.history[self.cycle:]

            #print 'updated self.history'
            #print (self.history)

            for val in weights.keys():
                dist[val].append(weights[val])

            #print 'final distrbution look'
            #print (dist)

        print ('Distribution')
        print ('=======before======')
        print (dist)

        for k in dist.keys():
            dist[k] = sum(dist[k])
        print ('=======after======')
        print (dist)

        return dist


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

def test_and_verify(dice):
    for i in range (3000):
        print (dice.roll())
    dice.show_history()
    dice.verify_distribution()

# dice = SettlersDice(settlers_weights)
#test_and_verify(dice)

class SimpleSettlersDice:

    def __init__(self, orig_weights):
        print ('simple settlers dice')

        self.orig_weights = orig_weights.copy()
        self.all_rolls = []
        self.roll_cnt = 0

        self.cycle = sum(self.orig_weights.values())

    def create_cycle(self):
        cycle_list = []
        for v in self.orig_weights.keys():
            cycle_list += [v] * self.orig_weights[v]

        random.shuffle(cycle_list)

        return cycle_list

    def roll(self):
        if self.roll_cnt == len(self.all_rolls):
            self.all_rolls += self.create_cycle()

        rolled_val = self.all_rolls[self.roll_cnt]
        self.roll_cnt += 1
        return rolled_val

    def get_history(self):
        return self.all_rolls[0:self.roll_cnt]

    def verify_distribution(self):
        return self._verify_distribution(self.get_history())

    def _verify_distribution(self, orig_history):
        print ('Verifying Distribution')

        history = orig_history[:]
        dist = defaultdict(list)

        while (history != []):
            # print ('----------------------------')
            cnt = Counter()
            for r in history[0:self.cycle]:
                cnt[r] += 1

            #print 'range of history processing'
            #print (cnt)

            weights = {}

            for val in cnt.keys():
                weights[val] = cnt[val]

            #print 'weight according to cnt'
            #print (weights)

            for val in weights.keys():
                weights[val] = weights[val] - self.orig_weights[val]

            #print 'weight after math'
            #print (weights)

            history = history[self.cycle:]

            #print 'updated history'
            #print (history)

            for val in weights.keys():
                dist[val].append(weights[val])

            #print 'final distrbution look'
            #print (dist)

        print ('Distribution')
        #print ('=======before======')
        #print (dist)

        for k in dist.keys():
            dist[k] = sum(dist[k])
        #print ('=======after======')
        print (dist)

        return dist

class SettlersDiceFactory:
    settlers_weights = {
        2: 1,
        3: 2,
        4: 3,
        5: 4,
        6: 5,
        7: 6,
        8: 5,
        9: 4,
        10: 3,
        11: 2,
        12: 1
    }

    test_weights = {
            1: 1,
            2: 2,
            3: 3
    }

    def __int__(self):
        print ('Settlers Dice Factory!')

    def get_settlers_dice(self):
        return SimpleSettlersDice(settlers_weights)

    def get_test_dice(self):
        return SimpleSettlersDice(test_weights)



# testDice = SettlersDiceFactory().get_test_dice()
# for i in range (36000):
#     print(testDice.roll())
# testDice.verify_distribution()


