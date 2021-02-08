import numpy as np

def calculate(list):
    if len(list) < 9:
      raise ValueError('List must contain nine numbers.') 


    new_arr = np.reshape(list, (3, 3))

    calculations = {}

    mean = []
    variance = [] 
    std = [] 
    maxi = []
    mini = []
    sums = [] 

    #mean
    mean_axis1 = []
    mean_axis1.append(np.mean(new_arr[:,0]))
    mean_axis1.append(np.mean(new_arr[:,1]))
    mean_axis1.append(np.mean(new_arr[:,2]))

    mean_axis2 = []
    mean_axis2.append(np.mean(new_arr[0,:]))
    mean_axis2.append(np.mean(new_arr[1,:]))
    mean_axis2.append(np.mean(new_arr[2,:]))

    mean_axis3 = np.mean(new_arr)

    mean.append(mean_axis1)  
    mean.append(mean_axis2)
    mean.append(mean_axis3)

    #variance
    variance_axis1 = []
    variance_axis1.append(np.var(new_arr[:,0]))
    variance_axis1.append(np.var(new_arr[:,1]))
    variance_axis1.append(np.var(new_arr[:,2]))

    variance_axis2 = []
    variance_axis2.append(np.var(new_arr[0,:]))
    variance_axis2.append(np.var(new_arr[1,:]))
    variance_axis2.append(np.var(new_arr[2,:]))

    variance_axis3 = np.var(new_arr)

    variance.append(variance_axis1)  
    variance.append(variance_axis2)
    variance.append(variance_axis3)

    #std
    std_axis1 = []
    std_axis1.append(np.std(new_arr[:,0]))
    std_axis1.append(np.std(new_arr[:,1]))
    std_axis1.append(np.std(new_arr[:,2]))

    std_axis2 = []
    std_axis2.append(np.std(new_arr[0,:]))
    std_axis2.append(np.std(new_arr[1,:]))
    std_axis2.append(np.std(new_arr[2,:]))

    std_axis3 = np.std(new_arr)

    std.append(std_axis1)  
    std.append(std_axis2)
    std.append(std_axis3)

    #max
    max_axis1 = []
    max_axis1.append(np.max(new_arr[:,0]))
    max_axis1.append(np.max(new_arr[:,1]))
    max_axis1.append(np.max(new_arr[:,2]))

    max_axis2 = []
    max_axis2.append(np.max(new_arr[0,:]))
    max_axis2.append(np.max(new_arr[1,:]))
    max_axis2.append(np.max(new_arr[2,:]))

    max_axis3 = np.max(new_arr)

    maxi.append(max_axis1)  
    maxi.append(max_axis2)
    maxi.append(max_axis3)

    #min
    min_axis1 = []
    min_axis1.append(np.min(new_arr[:,0]))
    min_axis1.append(np.min(new_arr[:,1]))
    min_axis1.append(np.min(new_arr[:,2]))

    min_axis2 = []
    min_axis2.append(np.min(new_arr[0,:]))
    min_axis2.append(np.min(new_arr[1,:]))
    min_axis2.append(np.min(new_arr[2,:]))
    
    min_axis3 = np.min(new_arr)

    mini.append(min_axis1)  
    mini.append(min_axis2)
    mini.append(min_axis3)

    #sum
    sum_axis1 = []
    sum_axis1.append(np.sum(new_arr[:,0]))
    sum_axis1.append(np.sum(new_arr[:,1]))
    sum_axis1.append(np.sum(new_arr[:,2]))

    sum_axis2 = []
    sum_axis2.append(np.sum(new_arr[0,:]))
    sum_axis2.append(np.sum(new_arr[1,:]))
    sum_axis2.append(np.sum(new_arr[2,:]))

    sum_axis3 = np.sum(new_arr)

    sums.append(sum_axis1)  
    sums.append(sum_axis2)
    sums.append(sum_axis3)

    calculations['mean'] = mean
    calculations['variance'] = variance
    calculations['standard deviation'] = std
    calculations['max'] = maxi
    calculations['min'] = mini
    calculations['sum'] = sums

    print(calculations)

    return calculations