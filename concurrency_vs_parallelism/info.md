# Concurrency vs Parallelism

## Concurrency

- Definition: Concurrency is about dealing with multiple tasks at the same time but not necessarily executing them simultaneously. It is a way to structure your code so that it can handle multiple tasks that overlap in time.

- How it Works: In a concurrent program, tasks can start, run, and complete in overlapping time periods. This can be achieved even on a single-core processor. Concurrency is mainly concerned with managing access to shared resources and ensuring that tasks are not stepping on each other's toes.

- Example in Python: Using threading (which can lead to concurrency because Python's Global Interpreter Lock (GIL) allows only one thread to execute Python bytecodes at a time), or asyncio (which provides asynchronous concurrency using event loops).

- Use Case: Concurrency is useful when tasks involve waiting (e.g., I/O operations, network requests). Instead of waiting for one task to complete before starting another, a concurrent program can switch between tasks, improving efficiency and responsiveness.

## Parallelism

- Definition: Parallelism is about executing multiple tasks simultaneously. It involves multiple processors or cores working at the same time, so tasks are literally running in parallel.

- How it Works: In a parallel program, different tasks or parts of a task are executed on different processors or cores simultaneously. This is achieved using multiple processes or using a multiprocessing approach.

- Example in Python: Using the multiprocessing module, which spawns multiple processes each with its own Python interpreter and memory space, allowing true parallel execution.

- Use Case: Parallelism is useful for CPU-bound tasks where the task can be split into independent units that can be processed simultaneously to improve performance. Examples include image processing, scientific computations, etc.

> Python Specific Considerations:

- **Concurrency** is often managed using threads or asynchronous programming (asyncio), but due to the Global Interpreter Lock (GIL) in CPython, true parallel execution of threads is limited.

- **Parallelism** can be achieved using the multiprocessing module, which sidesteps the GIL by using separate memory spaces for each process.
