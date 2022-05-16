# magic_square = [
# [8, 3, 4],
# [1, 5, 9],
# [6, 7, 2]]
# row1=0
# row2=0
# row3=0
# i=0
# while i<len(magic_square):
#     j=0
#     while j<len(magic_square[i]):
#         if i==0:
#            row1=(row1+magic_square[i][j]) 
#         elif i==1:
#             row2=(row2+magic_square[i][j])
#         elif i==2  :
#             row3=(row3+magic_square[i][j])   
#         j=j+1
#     i=i+1       
# colum1=0 
# colum2=0
# colum3=0
# k=0
# while k<len(magic_square):
#     l=0
#     while l<len(magic_square[k]):
#         if l==0:
#              colum1=colum1+magic_square[k][l]
#         elif l==1:
#             colum2=colum2+magic_square[k][l]
#         elif l==2:
#             colum3=colum3+magic_square[k][l]
#         l=l+1
#     k=k+1   
# diagonal1=0
# diagonal2=0
# m=0
# while m<len(magic_square):
#     n=0
#     while n<len(magic_square[m]):
#         if n-m==0:
#             diagonal1=diagonal1+magic_square[n][m]
#         if m+n==2:
#             diagonal2=diagonal2+magic_square[n][m]
#         n=n+1
#     m=m+1
# if row1==row2 and row1==row3 and row2==row3:
#     print([row1,row2,row3]) 
#     if colum1==colum2 and colum1==row3 and colum2==colum3:
#         print([colum1,colum2,colum3])
#         if diagonal1==diagonal2:
#             print([diagonal1,diagonal2])
#             if diagonal1==row1 and diagonal1==colum1 and row1==colum1 :
#                 print("yes")
#             else:
#                 print("no")
#         else:
#             print("NO Both diagonalare different")   
#     else:
#        print("NO Both the colum are different") 
# else:
#     print("NO Both rows are different")        
  




magic_square = [
[8, 3, 4],
[1, 5, 9],
[6, 7, 2]]
row1=0
row2=0
row3=0
colum1=0 
colum2=0
colum3=0
diagonal1=0
diagonal2=0
i=0
while i<len(magic_square):
    j=0
    while j<len(magic_square[i]):
        if i==0:
           row1=(row1+magic_square[i][j]) 
        elif i==1:
            row2=(row2+magic_square[i][j])
        elif i==2  :
            row3=(row3+magic_square[i][j])   
        if j==0:
             colum1=colum1+magic_square[i][j]
        elif j==1:
            colum2=colum2+magic_square[i][j]
        elif j==2:
            colum3=colum3+magic_square[i][j]
        if j-i==0:
            diagonal1=diagonal1+magic_square[j][i]
        if i+j==2:
            diagonal2=diagonal2+magic_square[j][i]
        j=j+1
    i+=1        
if row1==row2 and row1==row3 and row2==row3:
    print([row1,row2,row3]) 
    if colum1==colum2 and colum1==row3 and colum2==colum3:
        print([colum1,colum2,colum3])
        if diagonal1==diagonal2:
            print([diagonal1,diagonal2])
            if diagonal1==row1 and diagonal1==colum1 and row1==colum1 :
                print("yes")
            else:
                print("no")
        else:
            print("NO Both diagonalare different")   
    else:
       print("NO Both the colum are different") 
else:
    print("NO Both rows are different")        
  

















