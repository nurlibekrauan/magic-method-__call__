class AverageCalculator:
    list_of_nums = []
    def evarage(self):
        return sum(self.list_of_nums)/len(self.list_of_nums)
    def verify_data(self, data):
        if not isinstance(data, (int, float)):
            raise ValueError("Data must be a number")
    def __call__(self,data=None):
        if data is None: 
            return self.evarage()
        self.verify_data(data)
        self.list_of_nums.append(data)

        
avg_calc = AverageCalculator()
avg_calc(10)
avg_calc(20)
avg_calc(30)
print(avg_calc())  # Вернет среднее значение
