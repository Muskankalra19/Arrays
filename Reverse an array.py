def reverselist(A):
  print (A[::-1])
  
  
  OR
  
 def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
