import os
class Config:
    
    S0 = 100.0          # Initial stock price
    K = 100.0          # Strike price
    T = 1.0            # Time to maturity (years)
    r = 0.05           # Risk-free rate
    sigma = 0.2        # Volatility
    n_steps = 252      # Number of time steps (trading days)
    n_simulations = 1000  # Number of simulations

    
    results_dir = "results"
    plots_dir = "results/plots"
    data_dir = "results/data"


def create_directories():
    """Create necessary directories if they don't exist"""
    directories = [Config.results_dir, Config.plots_dir, Config.data_dir]
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
