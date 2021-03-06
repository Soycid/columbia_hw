import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
    """
      Softmax loss function, naive implementation (with loops)
      This adjusts the weights to minimize loss.

      Inputs have dimension D, there are C classes, and we operate on minibatches
      of N examples.

      Inputs:
      - W: a numpy array of shape (D, C) containing weights.
      - X: a numpy array of shape (N, D) containing a minibatch of data.
      - y: a numpy array of shape (N,) containing training labels; y[i] = c means
        that X[i] has label c, where 0 <= c < C.
      - reg: (float) regularization strength. For regularization, we use L2 norm.

      Returns a tuple of:
      - loss: (float) the mean value of loss functions over N examples in minibatch.
      - gradient: gradient wrt W, an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    #############################################################################
    #                     START OF YOUR CODE                                    #
    #############################################################################
    N = X.shape[0]

    # loss
    e = np.exp(np.dot(X, W))
    h = e/np.sum(e, axis=1).reshape(len(e),1)
    for n in range(N):
      loss += -np.log(h[n][y[n]])/N
    loss += 0.5 * reg*np.linalg.norm(W)

    # dW
    for n in range(N):
      h[n][y[n]] -= 1
    dW = np.dot(X.T, h)/N
    #dW += reg * W

    #############################################################################
    #                     END OF YOUR CODE                                      #
    #############################################################################


    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.
    This adjusts the weights to minimize loss.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    #############################################################################
    #                     START OF YOUR CODE                                    #
    #############################################################################
    
    #h = (np.exp(X)/np.sum(np.exp(X)))
    #print("h shape",h.shape)
    #loss = (-np.log(h[y])).mean() + reg*np.linalg.norm(W)
    #dW = np.dot(X.T, (h - y)) / y.shape[0]
    #rewrite

    N = X.shape[0]

    # loss
    e = np.exp(np.dot(X, W))
    h = e/np.sum(e, axis=1).reshape(len(e),1)
    
    loss = -np.log(h[range(N), y]).mean()
    loss += 0.5 * reg*np.linalg.norm(W)

    # dW
    h[range(N), y] -= 1
    dW = np.dot(X.T, h)/N
    #dW += reg * W


    #############################################################################
    #                     END OF YOUR CODE                                      #
    #############################################################################
    

    return loss, dW
