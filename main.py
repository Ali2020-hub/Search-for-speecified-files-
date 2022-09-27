
import os


def FindWithExtension(ex):

    all =""
    for root, dirs, files in os.walk(r"Z:\Al kharj"):
        for i in range(len(files)):
            if files[i].endswith(ex):
                paths = os.path.join(root, files[i])
                all = all + "\n" + paths
    print(all)


extension = input("==> : ")


if __name__ == '__main__':
    try:
        FindWithExtension(extension)
    finally:
        print("some thing Error")



