#!/usr/bin/env python3
#sed -i '1i #!/usr/bin/env python3' iszero.py
#chmod +x iszero.py
#./iszero.py
number = float(input("Enter a number: "))

if number == 0:
    print("This number is equal to zero.")
else:
    print("This number is different from zero.")