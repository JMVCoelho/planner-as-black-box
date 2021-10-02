import subprocess
import os


#########################
# READ INSTANCE FROM FILE
#########################

with open("in", "r") as handle:
    instance_n = handle.readline()

# i am used pre-generated hanoi inatances - should implement a generalizated script instead

instance = 'instances/hanoi-' + instance_n + '.pddl'


#########################
# RUN THE PLANNER
#########################

print("PLANNING FOR HANNOI WITH " + str(instance_n) + " PIECES")   

domain = 'domain/hanoi.pddl'

result = "result.txt"

subprocess.run(["singularity", "run", "../planner.img", domain, instance, result],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT)

removable = ["abstract-structure-graph.txt", "graph-gs-L-bolded-cs.png", "output", "output.sas", "plan_numbers_and_cost"]

for f in removable:
    os.remove(f)

with open(result, 'r') as handle:
    plan = handle.read()


#########################
# ADAPT THE OUTPUT
#########################

# here im just printting it - do whatever must be done
os.remove(result)
print(plan)








