# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)


def disp_2_digits(n): return str(n).zfill(2)
def disp_4_digits(n): return str(n).zfill(4)


print("{0}/{1}/{2} {3}:{4}".format(
    disp_2_digits(kata[1]),
    disp_2_digits(kata[2]),
    disp_4_digits(kata[0]),
    disp_2_digits(kata[3]),
    disp_2_digits(kata[4])
))
