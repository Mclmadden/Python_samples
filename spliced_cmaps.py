# By Eric Koch

def half_table(table1_name, table2_name, 
               reverse1=False, reverse2=False,
               pivot=0.5):
    """
    Splice together two matplotlib color tables.
    """
    n_col = 256
    cmap1 = cm.get_cmap(table1_name, n_col)
    cmap2 = cm.get_cmap(table2_name, n_col)
    pivot_int = int(round(pivot*n_col))
    if pivot_int < 0:
        pivot_int = 0
    if pivot_int > 255:
        pivot_int = 255
    n_cmap1 = pivot_int
    n_cmap2 = n_col-pivot_int
    # initialize
    newcolors = cmap1(np.linspace(0,1,n_col))
    # now hack
    newcolors[:pivot_int,:] = cmap1(np.linspace(0, 1, n_cmap1))
    newcolors[pivot_int:,:] = cmap2(np.linspace(0, 1, n_cmap2))        
    newcmp = ListedColormap(newcolors)
    return(newcmp)


def noise_and_heat():
    return(half_table('Greys','hot', pivot=0.2)) 
#mess with pivot to set the fraction where the two cmaps are stitched together
