while True:
    DNA = input(["Enter your sgRNA sequence (Please use all capital letters)"])

    print("\n \n")
    
    DNA_complement = DNA.translate(str.maketrans('ATCG', 'TAGC'))

    oligo1 = 'CACCG' + str(DNA)

    oligo2 = '    C' + str(DNA_complement) + 'CAAA'

    print('These are the oligos you will need to order:\n')
    print('Oligo 1-> ' + oligo1 + '\n' + '          ' + oligo2 + ' <-Oligo 2')
    print('\n\n')
    print("Oligo 1: 5'-" + oligo1 + "-3'")
    print("Oligo 2: 5'-" + oligo2.strip()[::-1] + "-3'")

    while True:
        closeornah = str(input('\n Do you need any more help? (y/n): '))
        if closeornah in ('y','n'):
            break
        print('Invalid input.')
    if closeornah == 'y':
        continue
    else:
        print('I am glad to have been of service, goodbye!')
        break



    
