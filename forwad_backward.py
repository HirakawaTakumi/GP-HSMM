import time
import GPSegmentation
from multiprocessing import Pool


def _foward_backward( args ):
    gpsegm, d = args

    start = time.time()
    print( "forward...", end="")
    a = gpsegm.forward_filtering( d )

    print( "backward...", end="" )
    segm, segm_class = gpsegm.backward_sampling( a, d )
    print( time.time()-start, "sec" )

    return segm, segm_class


def forward_backward_mp(gpsegm, data, num_threads):
    pool = Pool( num_threads )
    args = [ (gpsegm, d) for d in data ]
    ret = pool.map(_foward_backward, args )
    return zip(*ret)

def forward_backward_single(gpsegm, data ):
    segm, segm_class = _foward_backward( (gpsegm, data) )
    return (segm,), (segm_class,)
