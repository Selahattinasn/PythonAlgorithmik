def group_list(group, users):
  members = ""
  for user in users:
    members+=user
    if user!=users[-1]:
      members+=", "
  message="{}: {}".format(group,members)
  return message

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"