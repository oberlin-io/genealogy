#### FUNCTIONS
def csv_to_matrix(csv_file):
    '''
    Reads CSV file, returns list of sub-lists (rows) (ie matrix),
    Counts commas in first row of CSV file to determine columns.
    Currently does not support items with commas.
    But could do so by: first, split strings/rows by ' " ', then split sections by ',',
    and append sections in same order
    '''

    with open(csv_file, 'r') as f:
        csv = f.read()

    row_list = csv.splitlines()

    matrix = []
    for row in row_list:

        sub_list = []
        r = row
        while ',' in r:

            comma_x = r.index(',')

            if comma_x != -1:
                sub_list.append(r[:comma_x])
                r = r[comma_x+1:]

            else:
                r = ''

        if len(r) > 0:
            sub_list.append(r)

        matrix.append(sub_list)

    return matrix


def getLocations(matrix):

    blatDx = matrix[0].index('BLat')
    blonDx = matrix[0].index('BLon')
    dlatDx = matrix[0].index('DLat')
    dlonDx = matrix[0].index('DLon')

    locations = ''

    for rec in matrix:
        if matrix.index(rec) != 0:
            if rec[blatDx] != '':
                locations += '[%s,%s],\n' % (rec[blatDx], rec[blonDx])
            else:
                pass
            if rec[dlatDx] != '':
                locations += '            [%s,%s],\n' % (rec[dlatDx], rec[dlonDx])
            else:
                pass
        else:
            pass

    locations += ']'

    with open('gen-locs.txt', 'w') as f:
        f.write(locations)


#### RUN IT

# Get all lat lng sets from births and deaths
# Outputs as text formatted as an array
getLocations(csv_to_matrix("genealogy - persons.csv"))



done = raw_input('Done')
