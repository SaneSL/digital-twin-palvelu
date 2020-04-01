# Example module 2. Does division

class Division:
    module_id = 2
    def __init__(self, upper_lower):
        self.upper = upper_lower[0]
        self.lower = upper_lower[1]

    # Make moduleArgException?
    def check_divider(self):
        if self.lower == 0:
            raise Exception    
    
    def divide(self):
        self.check_divider()
        results = sum(self.data)
        return results

    def run(self):
        return self.divide()
