#Programmer Sadiq
#By@Sadiqul Islam
#Identity Operator


#Variables
#is operator
x = 10
y = 10

result = x is y

print(result)

#id() function
#আইডি () ফাংশন প্রদত্ত বস্তুর জন্য একটি অনন্য আইডি প্রদান করে।

#পাইথনের প্রতিটি বস্তু(object) তৈরি হয়ে গেলে একটি অনন্য আইডি পায়।

#কোনও সামগ্রীর আইডি হ'ল একটি পূর্ণসংখ্যা মান যা স্মৃতিতে কোনও বস্তুর ঠিকানা উপস্থাপন করে।

#Variables
x = 10
y = 10

result = x is y


print("Result :", result, id(x), id(y))


#is not operator
#Variables

x = 10
y = "Super"

result = x is not y

print("Result :",result, id(x),id(y))

#Upespected result
x = 258
y = 258

result = x is y

print("Mad result :",result)

