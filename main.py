from ur_dashboard import URDashboard

robot1 = URDashboard("172.31.0.101")

print(robot1.connect())

programName = "moveAToB"

print(robot1.load(programName))
