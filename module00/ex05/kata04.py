# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)

print("module_{0}, ex_{1} : {2:.2f}, {3:.2e}, {4:.2e}".format(
    str(kata[0]).zfill(2),
    str(kata[1]).zfill(2),
    kata[2],
    kata[3],
    kata[4]
))
