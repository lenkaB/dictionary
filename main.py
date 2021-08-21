import csv

def parse_dict(path):
    output = {}
    file = open(path,'r')
    for line in file.read().split('\n'):
        if len(line.split(' '))<4:
            continue
        try:
            part1 = line.split('-')[0]
            if '-' in line:
                explanation = line.split('-')[1]

                lemma = part1.split(' ')[0] #TODO leme iz prethodnog reda
                if '/' in lemma:
                    l1 = lemma.split('/')[0]
                    l2 = lemma.split('/')[1]
                    if l1==l2:
                        lemma = l1

                pos = part1.split(' ')[1]

                txt = ''
                after_pos = part1.split(' ')[2:]
                for el in after_pos:
                    txt+=el+' '
                after_pos = txt.strip()

                if pos=='im.':
                    info = after_pos.split('(')[0]
                    #print(lemma, pos, gender)
                elif pos=='prid.':
                    info = after_pos.split('(')[0]
                    #print(lemma, pos, definite)
                elif pos == 'gl.':
                    if '(' in part1:
                        info = after_pos.split('(')[0]
                        #print(lemma, pos, aspect)
                    else:
                        info = after_pos.split('prez.')[0]
                        #print(lemma, pos, aspect)

                output[lemma] = {'pos':pos, 'info':info, 'explanation':explanation }


            else:
                print('bez povlake ',part1)
        except:
            print('problematican red ', line)

    a_file = open("rjecnik.csv", "w")
    writer = csv.writer(a_file)
    writer.writerow(['lemma', 'pos', 'grammar', 'explanation'])
    for key, value in output.items():
        row = [key]
        for val in value.values():
            row.append(val)
        writer.writerow(row)
    a_file.close()



if __name__ == '__main__':
    parse_dict('rjecnik.txt')

