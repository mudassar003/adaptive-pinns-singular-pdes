import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Fix randomness for reproducibility
np.random.seed(42)
tf.random.set_seed(42)

# Small parameter for singular perturbation
epsilon = 0.01

# Define the neural network model
def build_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(1,)),
        tf.keras.layers.Dense(50, activation='tanh'),
        tf.keras.layers.Dense(50, activation='tanh'),
        tf.keras.layers.Dense(1)
    ])
    return model

# Compute the residual of the PDE: ε u''(x) - u(x)
def compute_pde_residual(model, x):
    with tf.GradientTape(persistent=True) as tape2:
        tape2.watch(x)
        with tf.GradientTape() as tape1:
            tape1.watch(x)
            u = model(x)
        u_x = tape1.gradient(u, x)
    u_xx = tape2.gradient(u_x, x)
    return epsilon * u_xx - u

# Generate training data
def generate_training_data(N_f=1000, N_b=100):
    x_f = tf.random.uniform((N_f, 1), 0, 1)        # Collocation points
    x_b0 = tf.zeros((N_b, 1))                      # Left boundary x = 0
    x_b1 = tf.ones((N_b, 1))                       # Right boundary x = 1
    return x_f, x_b0, x_b1

# Training function
def train(model, optimizer, epochs, data):
    x_f, x_b0, x_b1 = data
    for epoch in range(epochs):
        with tf.GradientTape() as tape:
            # Physics loss from PDE residual
            f_res = compute_pde_residual(model, x_f)
            loss_pde = tf.reduce_mean(tf.square(f_res))

            # Boundary losses
            u_b0 = model(x_b0)
            u_b1 = model(x_b1)
            loss_bc = tf.reduce_mean(tf.square(u_b0)) + tf.reduce_mean(tf.square(u_b1 - 1.0))

            total_loss = loss_pde + loss_bc

        grads = tape.gradient(total_loss, model.trainable_variables)
        optimizer.apply_gradients(zip(grads, model.trainable_variables))

        if epoch % 500 == 0:
            print(f"Epoch {epoch}: Loss = {total_loss.numpy():.5e}")

# Evaluate PINN vs. exact solution
def evaluate_model(model):
    x = np.linspace(0, 1, 200).reshape(-1, 1)
    x_tf = tf.convert_to_tensor(x, dtype=tf.float32)
    u_pred = model(x_tf).numpy().flatten()

    # Exact analytical solution
    denom = np.exp(1 / np.sqrt(epsilon)) - 1
    u_exact = (np.exp(x / np.sqrt(epsilon)) - 1) / denom
    return x.flatten(), u_pred, u_exact

# Plot results
def plot_results(x, u_pred, u_exact):
    plt.figure(figsize=(8, 5))
    plt.plot(x, u_exact, label='Exact Solution', linewidth=2)
    plt.plot(x, u_pred, '--', label='PINN Prediction', linewidth=2)
    plt.xlabel('x')
    plt.ylabel('u(x)')
    plt.title('PINN vs Exact: Singularly Perturbed Reaction–Diffusion')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Main execution
model = build_model()
optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
data = generate_training_data()
train(model, optimizer, epochs=5000, data=data)
x, u_pred, u_exact = evaluate_model(model)
plot_results(x, u_pred, u_exact)
