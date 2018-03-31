#encoding=utf-8
import csv

if __name__ == '__main__':
    # You should not modify this part.
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--source',
                       default='source.csv',
                       help='input source data file name')
    parser.add_argument('--query',
                        default='query.txt',
                        help='query file name')
    parser.add_argument('--output',
                        default='output.txt',
                        help='output file name')
    args = parser.parse_args()
    
    #load source data, build search engine
    source_file = open(args.source, 'r')
    csvCursor = csv.reader(source_file)
    source_data = []
    for row in csvCursor:
        source_data.append(row)

    #compute query result and output result
    output_file = open(args.output, 'w')
    new_line = False
    with open(args.query, 'r') as query_file:
        for line in query_file:
            if new_line:
                output_file.write('\n')
            new_line = True
            line = line[0:len(line)-1]
            if line.find('and') > -1:
                query_content = line.split(' and ')
                result_set  = set()
                flag = True
                for content in query_content:
                    temp_set = set()
                    for row in source_data:
                        if row[1].find(content) > -1:
                            temp_set.add(int(row[0]))
                    if flag:
                        flag = False
                        result_set = temp_set
                    else :
                        result_set = result_set & temp_set
                if len(result_set) == 0:
                    output_file.write('0')
                else:
                    result = list(result_set)
                    result.sort()
                    flag = False
                    for index in result:
                        if flag:
                            output_file.write(',')
                        flag = True
                        result_set = temp_set
                        output_file.write(str(index))
                        

            if line.find('or') > -1:
                query_content = line.split(' or ')
                result_set  = set()
                flag = True
                for content in query_content:
                    temp_set = set()
                    for row in source_data:
                        if row[1].find(content) > -1:
                            temp_set.add(int(row[0]))
                    if flag:
                        flag = False
                        result_set = temp_set
                    else :
                        result_set = result_set | temp_set
                if len(result_set) == 0:
                    output_file.write('0')
                else:
                    result = list(result_set)
                    result.sort()
                    flag = False
                    for index in result:
                        if flag:
                            output_file.write(',')
                        flag = True
                        result_set = temp_set
                        output_file.write(str(index))

            if line.find('not') > -1:
                query_content = line.split(' not ')
                result_set  = set()
                flag = True
                for content in query_content:
                    temp_set = set()
                    for row in source_data:
                        if row[1].find(content) > -1:
                            temp_set.add(int(row[0]))
                    if flag:
                        flag = False
                        result_set = temp_set
                    else :
                        result_set = result_set - temp_set
                if len(result_set) == 0:
                    output_file.write('0')
                else:
                    result = list(result_set)
                    result.sort()
                    flag = False
                    for index in result:
                        if flag:
                            output_file.write(',')
                        flag = True
                        result_set = temp_set
                        output_file.write(str(index))
