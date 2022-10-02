e=float(input("Enter your euros amount: "))
e_500 = e // 500
e = e - e_500*500
e_200 = e // 200
e = e - e_200*200
e_100 = e // 100
e = e - e_100*100
e_50 = e // 50
e = e - e_50*50
e_20 = e // 20
e = e - e_20*20
e_10 = e // 10
e = e - e_10*10
e_5 = e // 5
e = e - e_5*5

print(f"You have 500e bill: {round(e_500)}, 200e bill: {round(e_200)}, 100e bill: {round(e_100)}, 50e bill: {round(e_50)}, 20e bill: {round(e_20)}, 10e bill: {round(e_10)}, 5e bill: {round(e_5)}.")
	

