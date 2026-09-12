import numpy as np
import matplotlib.pyplot as plt


def build_basic_plot(output_path: str = "basic_plot.png") -> None:
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label="sin(x)")
    plt.title("Basic Line Plot")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


if __name__ == "__main__":
    build_basic_plot()
