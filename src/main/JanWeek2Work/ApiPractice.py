# 周六的安排
life = ['friends:coffeeShare','expertise:practiceSkills','body:fitnessFoodPurchase','mood:stories','money:Make']
message =f'things I gotta do'
# 开始的三件事
print(life[:3])
print(message)
# 中间的三件事
print(life[1:4])
# 末尾的三件事
print(life[-3:])

# 4-11 创建副本实现列表的转换
goal = ['know','use','fluent practice']
friends_goal = goal[:]
goal.append('mission Complete')
friends_goal.append('pretend know')
print(goal)
print(friends_goal)

# 4-12 实现名称的输出
for i in goal:
    for j in friends_goal:
        print(j)

