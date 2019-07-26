def merge_list(list1, list2):
    merged_data=""
    #write your logic here
    resultant_data=[]
    for i in range(len(list1)):
        if(list1[i]==None):
            resultant_data.append(list2[len(list1)-1-i])
        elif(list2[len(list1)-i-1]==None):
            resultant_data.append(list1[i])
        else:
            resultant_data.append(list1[i]+list2[len(list1)-1-i])
    for j in range(len(resultant_data)):
        merged_data=merged_data+resultant_data[j]+" "
    return merged_data

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)
