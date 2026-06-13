class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True
        if word.islower():
            return True
        if word[0].isupper() and word[1:].islower():
            return True
        return False
<<<<<<< HEAD
    
=======
>>>>>>> bd9b611965f8ec88a3b7a816d4e90586b6673690
