 
def inner_product(state_1, state_2):
    """Compute the inner product between two states.

    Args:
        state_1 (array[complex]): A normalized quantum state vector
        state_2 (array[complex]): A second normalized quantum state vector

    Returns:
        complex: The value of the inner product <state_1 | state_2>.
    """

    ##################
    # YOUR CODE HERE #
    ##################

    ## utilizado o produto internos explicitamente
    # Ex. :
    # state_1 = [ alpha|0> + beta|1>]
    # state_2 = [ gama|0> + sigma|1>]
    # retorna   gama*.alpha + sigma*.beta

    return state_1[0].conjugate()* state_2[0] + state_1[1].conjugate()*state_2[1]
    # COMPUTE AND RETURN THE INNER PRODUCT

    #pass


# Test your results with this code
ket_0 = np.array([1, 0])
ket_1 = np.array([0, 1])

print(f"<0|0> = {inner_product(ket_0, ket_0)}")
print(f"<0|1> = {inner_product(ket_0, ket_1)}")
print(f"<1|0> = {inner_product(ket_1, ket_0)}")
print(f"<1|1> = {inner_product(ket_1, ket_1)}")
