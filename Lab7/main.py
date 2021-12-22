from knuth_morris_pratt import kmp

if __name__ == '__main__':
    with open('kmp.in', 'r') as input_file:
        data = input_file.readlines()
    search_string = data[1]
    main_string = data[0]

    print('Result =>', kmp(search_string, main_string))