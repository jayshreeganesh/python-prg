# Solution 1 - Using | operator - bar

dict1 = {"John":89, "Lisa":99}
dict2 = {"Lisa":94, "Peter":78}

print(dict1 | dict2)

# Solution 2 - Using ** operator - quartz
dict3 = {"John":89, "Lisa":99}
dict4 = {"Lisa":94, "Peter":78}

print({**dict3,**dict4})

# Solution 3 - Using copy() and update() method
dict5 = {"John":89, "Lisa":99}
dict6 = {"Lisa":94, "Peter":78}

dict7 = dict6.copy()
dict7.update(dict5)

print(dict7)

dict8 = {"John":89, "Lisa":99}
dict9 = {"Lisa":94, "Peter":78}

dict10 = dict8.copy()
dict10.update(dict9)

print(dict10)