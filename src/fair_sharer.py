def fair_sharer(values, num_iterations, share=0.1):
    """
    Redistributes the highest value in the list to its neighbors over multiple iterations.

    Args:
        values: List of numeric values
        num_iterations: Number of redistribution iterations
        share: Fraction of the highest value to redistribute to neighbors

    Returns:
        List of redistributed values
    """
    import numpy as np

    values = np.array(values, dtype=float)
    n = len(values)

    for _ in range(num_iterations):
        max_idx = np.argmax(values)
        max_value = values[max_idx]
        to_share = max_value * share

        # Update values
        values[max_idx] -= 2 * to_share
        values[(max_idx - 1) % n] += to_share
        values[(max_idx + 1) % n] += to_share

    return values.tolist()
