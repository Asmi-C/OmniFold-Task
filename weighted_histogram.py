import numpy as np
import matplotlib.pyplot as plt


def whist(obs, wts=None, bins=30, rng=None, density=False,plot=False, xlabel="Observable", ylabel=None,title="Weighted Histogram", show=False):
    obs=np.asarray(obs, dtype=float)

    if obs.ndim!=1:
        raise ValueError("obs must be a 1d array")

    if wts is None:
        wts=np.ones_like(obs, dtype=float)
    else:
        wts=np.asarray(wts, dtype=float)
        if wts.ndim!=1:
            raise ValueError("wts must be a 1d array")
        if len(wts)!=len(obs):
            raise ValueError("obs and wts must have the same length")

    # drop non-finite entries 
    mask=np.isfinite(obs)&np.isfinite(wts)
    x=obs[mask]
    w=wts[mask]
    nused=len(x)
    ndropped=len(obs)-nused

    if nused==0:
        raise ValueError("no finite obs/wts pairs remain after filtering")

    # default range when bins is a scalar and user has given no range
    if rng is None and np.isscalar(bins):
        rng=(x.min(),x.max())
        # avoiding zero-width range when all the values are identical
        if rng[0]==rng[1]:
            mid=rng[0]
            rng=(mid-0.5, mid+0.5)

    # main histogram
    h, edges=np.histogram(x,bins=bins,range=rng,weights=w,density=density)

    # per-bin sum of squared weights for uncertainty estimates
    sw2,_=np.histogram(x,bins=edges,weights=w**2,density=False)
    centers=0.5*(edges[:-1]+edges[1:])
    result={"hist": h,"edges": edges,"centers": centers,"sumw2": sw2,"nused": nused,"ndropped": ndropped}
    if plot:
        if ylabel is None:
            ylabel="Density" if density else "Weighted Counts"

        plt.figure(figsize=(7,5))
        plt.stairs(h, edges, label="Histogram")
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.grid(alpha=0.3)
        plt.legend()

        if show:
            plt.show()

    return result


def runtests():
    # test 1: unit weights should match raw counts
    x=np.array([0.1,0.2,0.8,0.9])
    out=whist(x,bins=2,rng=(0,1),plot=False)
    assert np.allclose(out["hist"],np.array([2.0, 2.0]))
    assert np.allclose(out["sumw2"],np.array([2.0, 2.0]))

    # test 2: weighted sums should be correct
    w=np.array([1.0,2.0,10.0,20.0])
    out=whist(x,wts=w,bins=2,rng=(0,1),plot=False)
    assert np.allclose(out["hist"],np.array([3.0,30.0]))
    assert np.allclose(out["sumw2"],np.array([1.0**2+2.0**2,10.0**2+20.0**2]))

    # test 3: nan/inf handling - only finite pairs should be used
    xbad=np.array([0.1,np.nan,0.8,np.inf,0.4])
    wbad=np.array([1.0,2.0,np.inf,3.0,4.0])
    out=whist(xbad,wts=wbad,bins=2,rng=(0,1),plot=False)
    #here the finite pairs are (0.1, 1.0) and (0.4, 4.0)
    assert out["nused"]==2
    assert out["ndropped"]==3
    assert np.allclose(out["hist"],np.array([5.0, 0.0]))

    # test 4: negative weights should be allowed
    xneg=np.array([0.1,0.2,0.8])
    wneg=np.array([1.0,-0.5,2.0])
    out=whist(xneg,wts=wneg,bins=2,rng=(0,1),plot=False)
    assert np.allclose(out["hist"],np.array([0.5,2.0]))
    assert np.allclose(out["sumw2"],np.array([1.0**2+(-0.5)**2,2.0**2]))

    # test 5: mismatched lengths should raise valueerror
    try:
        whist([1,2,3], wts=[1,2], plot=False)
        raise AssertionError("expected valueerror for mismatched lengths")
    except ValueError:
        pass

    # test 6: density histogram should integrate to 1
    rg=np.random.default_rng(0)
    xrand=rg.uniform(0,1,size=5000)
    out=whist(xrand,bins=20,rng=(0,1),density=True,plot=False)
    widths=np.diff(out["edges"])
    integral=np.sum(out["hist"]*widths)
    assert np.isclose(integral,1.0,atol=5e-2)
    print("All tests passed.")


if __name__=="__main__":
    runtests()
    rg=np.random.default_rng(42)
    x=rg.normal(loc=50,scale=10,size=1000)
    w=rg.uniform(0.8,1.2,size=1000)
    whist(x,wts=w,bins=25,plot=True,xlabel="Example Observable",title="Demo Weighted Histogram",show=True,)
