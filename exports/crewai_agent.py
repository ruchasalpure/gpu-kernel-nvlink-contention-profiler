from crewai import Agent

gpu_kernel_nvlink_contention_profiler = Agent(
    role="Gpu Kernel Nvlink Contention Profiler",
    goal="Deliver high-precision autonomous Gpu Kernel Nvlink Contention Profiler operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
