while True:
    DNA = input(["Enter a nucleotide sequence (Please use all capital letters)"])

    print(" ")
    print(" ")

    DNA_length = len(DNA)

    print(" ")

    C_number = DNA.count('C')
    G_number = DNA.count('G')

    print(" ")

    CG_number = C_number + G_number

    print(" ")

    print("Length of sequence: " + str(DNA_length))
    print("Number of Cs: " + str(C_number))
    print("Number of Gs: " + str(G_number))
    print("Number of Cs and Gs: " + str(CG_number))

    print(" ")

    print("Total CG percentage: " + str((CG_number/DNA_length)*100) + "%")

    print(" ")
    print(" ")

    DNA_complement = DNA.translate(str.maketrans('ATCG', 'TAGC'))

    print("Complement: " + DNA_complement)

    DNA_reversecomplement = DNA_complement[::-1]

    print("Reverse complement: " + DNA_reversecomplement)

    print(" ")

    print("Sequence:")

    print(" ")

    print(DNA)
    print("|"*len(DNA))
    print(DNA_complement)

    print(" ")

    print("Reverse sequence:")

    print(" ")

    print(DNA[::-1])
    print("|"*len(DNA))
    print(DNA_reversecomplement)

    print ('\n')

    while True:
        closeornah = str(input('Do you need any more help? (y/n): '))
        if closeornah in ('y','n'):
            break
        print('Invalid input.')
    if closeornah == 'y':
        continue
    else:
        print('I am glad to have been of service, goodbye!')
        break

    



    
