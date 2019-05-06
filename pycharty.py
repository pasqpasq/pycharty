def pycharty(df,
             size     = .5,
             stacked  = False,
             theme    = 'blue',
             title    = 'This is the title',
             legend   = True,
            ):
    # get groups
    group_labels = df['Group'].unique().tolist()
    group_count = len(df['Group'].unique().tolist())
    # get types
    type_labels = df['Type'].unique().tolist()
    type_count = len(df['Type'].unique().tolist())
    # x axis index
    index = np.arange(group_count)
    # ratios
    _width = .7 if stacked else .8/type_count
    x_ticks_loc = index if stacked else index + _width*(type_count-1)*.5
           
    figsize_x = 2*(group_count+(type_count*(not stacked)))*size
    figsize_y = 12 * size

    themes = {'blue' : ['#373F51','#01BAEF','#D9D9D9','#919191','#373F51'],
               'pink' :['#373F51','#F45B69','#D9D9D9','#919191','#373F51'],
              'yellow' :['#373F51','#F0C808','#D9D9D9','#919191','#373F51'],
                    }
    color_palette = themes[theme]
    fig, ax = plt.subplots(figsize=(figsize_x,figsize_y))
    bar_space = .00

    if not stacked:
        for (i, _type) in enumerate(type_labels):
            ax.bar(index + (_width * i) + (bar_space * i),
               df['Value'][df['Type'] == _type].values.tolist(),
               width = _width,
               color = color_palette[i],
               label = _type)

    bottom_temp = [0] * group_count

    if stacked:
            for (i, _type) in enumerate(type_labels):
                ax.bar(index,
                   df['Value'][df['Type'] == _type].values.tolist(),
                   width = _width,
                   color = color_palette[i],
                   label = _type,
                   bottom = bottom_temp
                      )  
                values_temp = df['Value'][df['Type'] == _type].values.tolist()
                bottom_temp = [values_temp[i]+bottom_temp[i] for i in range(group_count)]
    ax.grid(color='black', linestyle=':', linewidth=1.5*size, alpha = .3)
    ax.xaxis.grid(False)
    ax.set_axisbelow(True)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_edgecolor('#2B2D42')
    plt.xticks(x_ticks_loc, group_labels)
    ax.set_ylabel(list(df)[2])
    ttl = ax.set_title(title, color = '#2B2D42', fontsize = 18*size*1.6)
    for item in ([ax.xaxis.label, ax.yaxis.label] + #ax.title, 
                 ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(22*size)
        item.set_fontname('Helvetica')
    if legend:
        lg = ax.legend(ncol = type_count, loc = 'upper center', bbox_to_anchor=(0.5, -.06), frameon = False, fontsize = 22*size)
        plt.setp(lg.get_texts(), color='#2B2D42')
    plt.show()