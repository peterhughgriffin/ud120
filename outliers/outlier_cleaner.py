#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    import numpy as np
    
    cleaned_data = []

    ### your code goes here
    errors = abs(np.subtract(net_worths,predictions))
    maxErr = np.percentile(errors,90)
    
    for error,age,net_worth in zip(errors,ages,net_worths):
        if error<=maxErr:
            cleaned_data.append((age,net_worth,error))
    print (len(cleaned_data))
    
    return cleaned_data

