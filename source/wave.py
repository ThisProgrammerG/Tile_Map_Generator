from dataclasses import dataclass


@dataclass(slots=True)
class Wave:
    seed: float
    frequency: float
    amplitude: float


height_waves = [Wave(seed=56, frequency=0.05, amplitude=1.0), Wave(seed=199.36, frequency=0.1, amplitude=0.5)]
moisture_waves = [Wave(seed=621, frequency=0.03, amplitude=1.0)]
heat_waves = [Wave(seed=318.6, frequency=0.04, amplitude=1.0), Wave(seed=329.7, frequency=0.02, amplitude=0.5)]
