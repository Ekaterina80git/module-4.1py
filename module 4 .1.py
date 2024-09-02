import fake_match as fm
import true_match as tm




fake_divide = fm.divide
true_divide = tm.divide

resalt1 = fake_divide(69,3)
resalt2 = fake_divide(3,0)
resalt3 = true_divide(49,7)
resalt4 = true_divide(15,0)

print(resalt1)
print(resalt2)
print(resalt3)
print(resalt4)







