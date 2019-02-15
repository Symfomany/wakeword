#!/usr/bin/env python3


# Finally, you can write your program, passing the location of the precise binary like shown:



from precise_runner import PreciseEngine, PreciseRunner

engine = PreciseEngine('precise-engine/precise-engine', 'my_model_file.pb')
runner = PreciseRunner(engine, on_activation=lambda: print('hello'))
runner.start()