#only needs to be ran once using "python ./createFileOnce.py"
#creates a empty dictionary file which we will load in location input
import numpy as np

def main():
  new_dict = dict()
  np.save("Dictionary.npy", new_dict)
    
if __name__ == '__main__':
  main()
