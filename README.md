# scilslab pyworld2px

This package contains the Python implementation for converting "world" coordinates (in um) from Bruker MALDI-(TIMS)-TOF 
instruments/SCiLS Lab to x-y coordinates (i.e. "pixel" coordinates) using a transformation matrix associated with each 
ROI in SCiLS Lab. The x-y coordinates can then be written back to a pandas DataFrame containing ROI and coordinate 
information.

## Example
```
import scilslab
from util.world2px import world2px
from util.coords import add_pixel_coords_to_region_spots


with scilslab.LocalSession(filename='data.slx) as session:
    dataset = session.dataset_proxy
    region_tree = dataset.get_region_tree()
    region_tree_df = add_pixel_coords_to_region_spots(dataset)

print(region_tree_df)
```
