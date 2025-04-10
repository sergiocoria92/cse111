def main():
  # Create and print a list named fruit.
  fruit_list = ["pear", "banana", "apple", "mango"]
  print(f"original: {fruit_list}")
  fruit_list.reverse()
  print(f"sorted: {fruit_list}")
  fruit_list.append("orange")
  print (f"added: {fruit_list}")
  fruit_list.insert((fruit_list.index("apple")),"cherry")
  print (f"inserted: {fruit_list}")
  fruit_list.remove("banana")
  print (f"removed: {fruit_list}")
  fruit_list.pop(-1)
  print (f"removed first: {fruit_list}")
  fruit_list.sort()
  print (f"sorted: {fruit_list}")
  
  
main ()