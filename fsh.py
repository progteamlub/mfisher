import os, sys, time
print('█▒▒▒▒▒▒▒▒▒ 10% Подпишись на группу что бы было больше утилит!')
time.sleep(3)
os.system('clear')
print('███▒▒▒▒▒▒▒ 30%')
time.sleep(3)
os.system('clear')
print('█████▒▒▒▒▒ 50%')
time.sleep(3)
os.system('clear')
print('███████▒▒▒ 60%')
time.sleep(3)
os.system('clear')
print('100% ██████████')

 
time.sleep(2)
os.system('clear')

print("""\033\35m
 `'•.¸(¯`'•.¸*♥♥♥♥*¸.•'´¯)¸.•'´¯)
♥(¯`'•.¸(¯`' •.¸*♥♥*¸.•'´¯)¸.•'´¯)♥
♥♥(¯`'•.¸(¯`'•.¸**¸.•' ´¯)¸.•'´¯)♥♥
--==----------FishMaster----==-
(_¸. •'´(_¸.•'´* ♥♥♥♥*`'•.¸_)`'•.¸_)
     ×ProgTeam ° Termux SU×
""")
print("Starting.")
os.system('clear')
time.sleep(0.8)
print("""
 `'•.¸(¯`'•.¸*♥♥♥♥*¸.•'´¯)¸.•'´¯)
♥(¯`'•.¸(¯`' •.¸*♥♥*¸.•'´¯)¸.•'´¯)♥
♥♥(¯`'•.¸(¯`'•.¸**¸.•' ´¯)¸.•'´¯)♥♥
--==----------FishMaster----==-
(_¸. •'´(_¸.•'´* ♥♥♥♥*`'•.¸_)`'•.¸_)
     ×ProgTeam ° Termux SU×""")
print('Starting..')
os.system('clear')
time.sleep(0.8)
print("""
 `'•.¸(¯`'•.¸*♥♥♥♥*¸.•'´¯)¸.•'´¯)
♥(¯`'•.¸(¯`' •.¸*♥♥*¸.•'´¯)¸.•'´¯)♥
♥♥(¯`'•.¸(¯`'•.¸**¸.•' ´¯)¸.•'´¯)♥♥
--==----------FishMaster----==-
(_¸. •'´(_¸.•'´* ♥♥♥♥*`'•.¸_)`'•.¸_)
     ×ProgTeam ° Termux SU×""")
print('Starting...')
time.sleep(0.8)

ports = input("[PORT]: ")
if ports == "":
    ports=8080
os.system("php -S localhost:"+str(ports))
