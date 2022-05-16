import jax.numpy as np
from jax.numpy.linalg import norm
from jax.random import normal


def d_fold_tensor_product(x, order=4) -> np.DeviceArray:
    """
    Compute d-fold tensor product of a vector.

    Args:
        x (np.ndarray): Vector
        d (int): Order of tensor product
    Returns:
        np.ndarray: d-fold tensor product of x.
    """
    assert order > 1, "Error: Tensor order must be bigger than 1."

    xd = np.tensordot(x, x, axes=0)
    for _ in range(1, order - 1):
        xd = np.tensordot(xd, x, axes=0)

    return xd


def sample_sphere(key, n) -> np.DeviceArray:
    """
    Get a sample drawn uniformly from the (n-1)-sphere.
    Args:
        n (int): Dimension.
    Returns:
        np.ndarray: Sample.
    """
    x = normal(key, shape=(n,))

    return x / norm(x)


def get_normal_proposal(key, x_old, scaling_parameter=1) -> np.DeviceArray:
    """
    Sample a vector from a normal distribution centered at the
    current position of the Markov chain.

    Args:
        x_old (np.ndarray): Current vector.

    Returns:
        np.ndarray: Sample.
    """
    n = len(x_old)
    x = x_old + (1 / n) ** scaling_parameter * normal(key, x_old.shape)

    return x / norm(x)
