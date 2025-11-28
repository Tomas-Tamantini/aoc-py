from src.solutions.y2015.d22.logic.state.character import Character
from src.solutions.y2015.d22.logic.state.effect_state import EffectState
from src.solutions.y2015.d22.logic.state.effects import HardModeEffect


def hard_mode_effect_state() -> EffectState:
    hard_mode_effect = HardModeEffect(target=Character.PLAYER, damage=1)
    return EffectState(runs_on_turn=Character.PLAYER, effect=hard_mode_effect)
