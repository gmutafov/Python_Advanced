from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    INITIAL_STRENGTH_NEEDED: float = 200
    MIN_STRENGTH_NEEDED = 100

    def __init__(self, name):
        super().__init__(name, ArcticClimber.INITIAL_STRENGTH_NEEDED)

    def can_climb(self):
        return self.strength >= ArcticClimber.MIN_STRENGTH_NEEDED

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == 'Extreme':
            self.strength -= 20 * 2
        else:
            self.strength -= 20 * 1.5

        self.conquered_peaks.append(peak.name)
