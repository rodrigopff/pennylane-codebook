# Here are the vector representations of |0> and |1>, for convenience
ket_0 = np.array([1, 0])
ket_1 = np.array([0, 1])

def normalize_state(alpha, beta):
    """Compute a normalized quantum state given arbitrary amplitudes.

    Args:
        alpha (complex): The amplitude associated with the |0> state.
        beta (complex): The amplitude associated with the |1> state.

    Returns:
        array[complex]: A vector (numpy array) with 2 elements that represents
        a normalized quantum state.
    """

    ##################
    # YOUR CODE HERE #
    ##################
    aq = alpha**2
    bq = beta**2
    print(aq)
    print(bq)
    soma = aq + bq
    print(soma)

    normaVetor = np.sqrt(soma)
    print(normaVetor)

    alphaNormalizado = alpha/normaVetor
    print(alphaNormalizado)

    betaNormalizado = beta/normaVetor
    print(betaNormalizado)

    #print(alphaNormalizado**2+betaNormalizado**2)

    # CREATE A VECTOR [a', b'] BASED ON alpha AND beta SUCH THAT |a'|^2 + |b'|^2 = 1
    return np.array([alphaNormalizado,betaNormalizado])
    # RETURN A VECTOR
    #pass
#alpha = 1
#beta = 3
#print (normalize_state(alpha, beta))
