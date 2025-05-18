"""
1. Take subject marks as command line arguments

"""
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Take subject marks as command line arguments")   
    parser.add_argument("--physics", type=int, help="Enter the physics marks")
    parser.add_argument("--chemistry", type=int,help="Enter the chemistry marks")
    parser.add_argument("--maths",type=int,help="Enter the maths marks")
    args = parser.parse_args()

    physics_marks = args.physics
    chemistry_marks = args.chemistry
    maths_marks = args.maths
    average_marks = None

    print ("physics marks",physics_marks)
    print ("chemistry marks",chemistry_marks)
    print ("maths marks",maths_marks)

    # get the average of the marks using the formula
    average_marks = (physics_marks + chemistry_marks + maths_marks) / 3

    # get the average of the marks using the statistics module  
    import statistics
    marks = [physics_marks, chemistry_marks, maths_marks]
    average_marks_mean = statistics.mean(marks)
 
    print ("Average of marks: ",average_marks_mean,average_marks)

#    # To run this script, use the command line and provide the arguments as follows:
    #& C:/Users/SingRit1/AppData/Local/Programs/Python/Python313/python.exe c:/Ritesh/Work/R_AND_D/AI/Python/Coding/python/Basics/20_command_argument/exercise.py --physics 60 --chemistry 70 --maths 90

