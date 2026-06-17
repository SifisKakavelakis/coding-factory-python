# yield: converts a simple function into generator
# yeild: returns a generator object

# When a generator function is called, it returns a generator object BUT does not start execution immediately.
# When the next() function is called on the generator object, the generator function starts executing util it
# reached the yield statement. The value specified in the yield statement is returned to the caller, and the
# state of the generator function is saved. The next time next() function is called, the generator resumes execution
# right after the yield statement, preserving the local variables and execution state.

def simple_generator():
    print("The capital of", end=" ")
    yield 100
    print("Greece is", end=" ")
    yield 200
    print("Athens.")
    yield 300

def main():
    gen = simple_generator()
    a = next(gen)
    # print(f"\na={a}\n"")
    # print()
    b = next(gen)
    # print()
    c = next(gen)

    print("------------------")
    import time

    gen = simple_generator()
    for g in gen:
        time.sleep(3)
        print(g)
    # print()

if __name__ == "__main__":
    main()