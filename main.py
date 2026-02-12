from modules.SetModule import SetModule
import Discrete_calculator

def main():
    setModuleObject = SetModule({1,2,3},{3,4,5})
    print(setModuleObject.get_union())


if __name__ == "__main__":
    main()