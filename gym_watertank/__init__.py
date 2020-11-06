from gym.envs.registration import register

register(
    id='WaterTank-v0',
    entry_point='gym_watertank.envs:WaterTankEnv',
)
register(
    id='WaterTank-v1',
    entry_point='gym_watertank.envs:WaterTankEnv1',
)

# LQR
register(
    id='WaterTankLQR-v0',
    entry_point='gym_watertank.envs:WaterTankLQREnv',
)
register(
    id='WaterTankLQR-v1',
    entry_point='gym_watertank.envs:WaterTankLQREnv1',
)


register(
    id='WaterTankLQRZeroNoise-v0',
    entry_point='gym_watertank.envs:WaterTankLQRZeroNoiseEnv',
)
register(
    id='WaterTankLQRZeroNoise-v1',
    entry_point='gym_watertank.envs:WaterTankLQRZeroNoiseEnv1',
)

register(
    id='LQR-v0',
    entry_point='gym_watertank.envs:LQREnv',
)

# Integral
register(
    id='WaterTankIntegral-v0',
    entry_point='gym_watertank.envs:WaterTankIntegralEnv',
)
register(
    id='WaterTankIntegral-v1',
    entry_point='gym_watertank.envs:WaterTankIntegralEnv1',
)

# LQI
register(
    id='WaterTankLQI-v0',
    entry_point='gym_watertank.envs:WaterTankLQIEnv',
)
register(
    id='WaterTankLQI-v1',
    entry_point='gym_watertank.envs:WaterTankLQIEnv1',
)

register(
    id='WaterTankLQIZeroNoise-v0',
    entry_point='gym_watertank.envs:WaterTankLQIZeroNoiseEnv',
)

register(
    id='WaterTankLQIZeroNoise-v1',
    entry_point='gym_watertank.envs:WaterTankLQIZeroNoiseEnv1',
)

