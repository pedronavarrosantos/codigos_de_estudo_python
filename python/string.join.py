gym_problem = ["I'm", "struggling", "with", "this", "gym", "problem", "today!"]
gym_separator = " ; "
print(gym_separator.join(gym_problem))

coding_exp = ["I'm", "day!", "having", "learning", "fun", "Python", "all"]

def sentence_assembly(coding_exp):
   right_order = [0, 2, 4, 3, 5, 6, 1]
   separator = ' | '
   return separator.join(coding_exp[i] for i in right_order)

print (sentence_assembly(coding_exp))