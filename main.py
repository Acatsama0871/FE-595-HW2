# main.py
# extract the companies' name and companies' purpose


# modules
from scraper import extract_name_purpose


def main():
    # initialize
    extract_results = []
    error_times = 0

    # extract
    for i in range(50):
        cur_status, cur_result = extract_name_purpose(url='http://3.95.249.159:8000/random_company')

        if cur_status:  # if extract successfully
            extract_results.append(cur_result)
        else:  # if not
            error_times += 1

    # output result
    # convert result to single a string
    output_string = ''
    for item in extract_results:
        output_string += 'Name: ' + item['Name'] + '---' + 'Purpose: ' + item['Purpose'] + '\n'

    # write to disk once
    with open('result.txt', 'w') as file:
        file.write(output_string)

    return



if __name__ == '__main__':
    main()
