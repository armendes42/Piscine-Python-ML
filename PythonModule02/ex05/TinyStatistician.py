import math

class TinyStatistician:
    def __init__(self):
        pass

    def mean(self, x):
        if len(x) == 0:
            print("Param should be a non-empty list or array.")
            return None
        mean = sum(x) / len(x)
        return float(mean)
    
    def median(self, x):
        if len(x) == 0:
            print("Param should be a non-empty list or array.")
            return None
        x.sort()
        n = len(x)
        if len(x) % 2 != 0:
            median = x[n // 2]
            return float(median)
        else:
            median = (x[n // 2] + x[(n // 2) + 1]) / 2
            return float(median)
        
    def quartiles(self, x):
        if len(x) == 0:
            print("Param should be a non-empty list or array.")
            return None
        x.sort()
        n = len(x)
        quartile_one_index = int(0.25 * (n + 1))
        quartile_three_index = int(0.75 * (n + 1))
        quartile_one = x[quartile_one_index]
        quartile_three = x[quartile_three_index - 1]
        quartiles = [float(quartile_one), float(quartile_three)]
        return quartiles
    
    def var(self, x):
        if len(x) == 0:
            print("Param should be a non-empty list or array.")
            return None
        mean = self.mean(x)
        sum = 0
        for value in x:
            sum += (value - mean) ** 2
        var = sum / len(x)
        return float(var)
    
    def std(self, x):
        if len(x) == 0:
            print("Param should be a non-empty list or array.")
            return None
        var = self.var(x)
        std = math.sqrt(var)
        return float(std)
        
        