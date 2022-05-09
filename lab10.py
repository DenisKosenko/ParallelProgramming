import multiprocessing

list=['A', 'B', 'C', 'D', 'E', 'F']

def do_stuff(element,sharedlist):
    element_dict={}
    element_dict['name']=element
    sharedlist.append(element_dict)
    print(sharedlist)

if __name__ == "__main__":
    pool=multiprocessing.Pool(processes=6)
    manager=multiprocessing.Manager()
    sharedlist=manager.list()
    tasks = [(x,sharedlist) for x in list]
    pool.starmap(do_stuff, tasks)
    pool.close()