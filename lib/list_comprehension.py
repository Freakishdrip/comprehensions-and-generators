#!/usr/bin/env python3

def return_evens(num_list):
  arr = []
  for num in num_list:
    result = num % 2
    if result == 0:
      arr.append(num)
  print(arr)
  return arr
    
  
  # index = 0
  # while(index < len(num_list)):
  #   index += 1
  # for num in num_list:
  #   indicks = num % 2 
  # if(indicks == 0):
  #   print(indicks)
  # return
return_evens([0,1,2,3,4,5,6,7,8,9,10])

print(10%2)


def make_exclamation(sentence_list):
  arr = []
  # print(sentence_list)
  for sentence in sentence_list:
    # print(sentence)
    result = sentence + "!"
    # print(result)
    arr.append(result)
  # print(arr)
  return arr
  # sentence_list.append("!")
  # print(sentence_list)


make_exclamation([
            "I like computers",
            "I require coffee",
            "Live long and prosper",
        ])