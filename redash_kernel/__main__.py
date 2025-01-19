from ipykernel.kernelapp import IPKernelApp
from .kernel import RedashKernel

if __name__ == "__main__":
    IPKernelApp.launch_instance(kernel_class=RedashKernel)
