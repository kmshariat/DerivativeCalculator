import diff 
import numpy as np

x = np.linspace(-2, 2, 100)
diff.plot_f(x)
diff.plot_df(x)
diff.plot_ddf(x)
diff.plot_dddf(x)