def calculate_tax(wages):
    
    if wages <= 14000:
        wage_tax = .105
    elif wages <= 48000:
        wage_tax = .175
    elif wages <= 70000:
        wage_tax = .30
    else:
        wage_tax = .33

    return wages * wage_tax

print(calculate_tax(48000))














