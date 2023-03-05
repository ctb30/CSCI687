   
SCRATCHPAPER:

if numSegments >= 3 : 
        secondSegment = thisLine[1]
        sequenceArrayPosition = int(secondSegment)
        print(" Change at position" + str(sequenceArrayPosition))

        thirdSegment = thisLine[2]
        flag = 0 
        match thirdSegment:
            case "DNA":
                  print("DNA!")
                  flag = 1
            case "RNA":
                  print("RNA!")
                  flag = 1 
        
        if flag == 0: 
             thirdSegment
        
            

    elif numSegments >= 2 : 
         secondSegment = thisLine[1]
         sequenceArrayPosition = int(secondSegment)
         print(" Change at position" + str(sequenceArrayPosition))
         