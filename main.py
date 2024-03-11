from dictmake import occur_dict, suited_parses


min_key = ''
min_val = 10000000

for i in occur_dict:
   if len(occur_dict[i]) < min_val:
      min_val = len(occur_dict[i])
      min_key = i
      
print(min_key)
print(*occur_dict[min_key], sep='\n')

