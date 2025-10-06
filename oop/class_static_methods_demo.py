

# ===============================================================================================
# here I have created a class called Calculator which i difine class attribute calculation_type
class Calculator:
    # ===========================================================================================
    # Class attribute shared by all instances
    calculation_type = "Arithmetic Operations"

    # ============================================================================================
    #  here I add method has been decorator with staticmethod  to add two numbers
    @staticmethod
    def add(a, b):
        return a + b

    # ===========================================================================================
    #  here I add method has been decorator with classmethod to multiply two numbers
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
# ===============================================================================================