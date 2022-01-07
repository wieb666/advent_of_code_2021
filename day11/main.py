import sys
import pandas as pd

def get_adjoining(pos, size=10):
    l = []
    ii = pos[0]
    jj = pos[1]
    for i in range(ii-1, ii+2):
        for j in range(jj-1, jj+2):
            if i >= 0 and i < size and j >= 0 and j < size:
                l.append((i,j))
    return l

def getIndexes(dfObj, value):
    # Empty list
    listOfPos = []
     
    # isin() method will return a dataframe with
    # boolean values, True at the positions   
    # where element exists
    result = dfObj.isin(value)
     
    # any() method will return
    # a boolean series
    seriesObj = result.any()
 
    # Get list of column names where
    # element exists
    columnNames = list(seriesObj[seriesObj == True].index)
    
    # Iterate over the list of columns and
    # extract the row index where element exists
    for col in columnNames:
        rows = list(result[col][result[col] == True].index)
 
        for row in rows:
            listOfPos.append((row, col))
             
    # This list contains a list tuples with
    # the index of element in the dataframe
    return listOfPos

def main(fname):
    lines = []
    with open(fname) as f:
        for line in f:
            lines.append([int(i) for i in line.strip()])

    df = pd.DataFrame(lines)
    flashes = 0
    positions = list(range(10,2500))

    for i in range(10000):
        df = df + 1
        flashing = True
        listOfPositions = getIndexes(df, positions)
        pos_done = []
        while flashing:
            pos_done = pos_done + listOfPositions
            flashes += len(listOfPositions)
            for j in listOfPositions:
                locations = get_adjoining(j)
                for loc in locations:
                    df.iloc[loc] += 1
            new_listOfPositions = getIndexes(df, positions)
            listOfPositions = list(set(new_listOfPositions) - set(pos_done))
            if not listOfPositions:
                flashing = False
        df[df > 9] = 0
        if df.to_numpy().sum() == 0:
            break
        
    print(df)
    print(flashes)
    print(i+1)
    
if __name__ == "__main__":
    main(sys.argv[1])


## TODO works but not correct yet
