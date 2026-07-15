class ABTester:
    def __init__(self):
        self.samples = []
    
    def test(self, variant_a, variant_b):
        score_a = sum(self.samples) / len(self.samples) if self.samples else 0.5
        score_b = 0.5
        return "A" if score_a > score_b else "B"