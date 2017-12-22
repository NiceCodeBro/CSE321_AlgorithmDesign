# base case'i arraylerin boş olup olmama durumunu göz önüne alarak size == 1 için ayarladım.
# iki arrayin de array size'ı nın yarısının toplamı metoda gönderilen size değerinden küçük ise, bu size değerilerinin 
# bulunduğu indexdeki verileri karşılaştırıp küçük olan tarafı egale edip metodu tekrar çağırdım.
# eğer midN + midM < size bu şart sağlanmaz ise iki arrayden de birer birer eleman azaltarak size değerinin 
# 1 e eşitlenip base case girmesini sağladım.

m = ["algotihm", "programminglanguages", "systemsprogramming"]
n = ["computergraphics", "cprogramming","oop"]
def find_kth_book_1(m,n,size):
  if(size == 1):
    if(m!=[] and n!=[]):
      return min(m[0],n[0])
    if(m==[]):
      return n[0]
    if(n==[]):
      return m[0]
  else:
    midM = len(m) // 2
    midN = len(n) // 2
    if(midM!= 0 and midN != 0 and midN + midM < size):
      if(m[midM-1] < n[midN-1]):
        return find_kth_book_1(m[midM:],n,size-midM)
      else:
        return find_kth_book_1(m,n[midN:],size-midN)
    else:
      if(m != [] and n!=[]):
        if(m[0] < n[0]):
          return find_kth_book_1(m[1:],n,size-1)
        else:
          return find_kth_book_1(m,n[1:],size-1)
      else:
        if(m!=[]):
          return find_kth_book_1(m[1:],n,size-1)
        else:
          return find_kth_book_1(m,n[1:],size-1)
          
    


book = find_kth_book_1(m,n,1)
print(book)

