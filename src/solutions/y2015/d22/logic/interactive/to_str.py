import re
from typing import Iterator

from src.solutions.y2015.d22.logic.actions.atomic import (
    AddTimedEffect,
    AtomicTransformation,
    DealDamage,
    DecrementEffectTimer,
    Heal,
    RechargeMana,
    RemoveEffect,
)
from src.solutions.y2015.d22.logic.actions.composite import CompositeAction
from src.solutions.y2015.d22.logic.actions.game_action import GameAction
from src.solutions.y2015.d22.logic.actions.moves import DirectDamage, GameMove
from src.solutions.y2015.d22.logic.state.attributes import (
    armor,
    current_effect_state,
    current_turn,
)
from src.solutions.y2015.d22.logic.state.character import (
    Character,
    CharacterState,
)
from src.solutions.y2015.d22.logic.state.game_state import GameState


def _character_to_str(character: Character) -> str:
    return str(character).split(".")[-1].capitalize()


def _character_attributes(
    character_state: CharacterState, game_state: GameState
) -> Iterator[str]:
    yield f"{character_state.hit_points} hit points"
    if armor_value := armor(game_state, character_state.id):
        yield f"{armor_value} armor"
    if character_state.mana_points:
        yield f"{character_state.mana_points} mana"


def _character_state_to_str(
    character_state: CharacterState, game_state: GameState
) -> str:
    return f"- {_character_to_str(character_state.id)} has " + ", ".join(
        _character_attributes(character_state, game_state)
    )


def _turn_header(character: Character) -> str:
    return f"\n-- {_character_to_str(character)} turn --"


def game_state_to_str(game_state: GameState) -> Iterator[str]:
    yield _turn_header(current_turn(game_state))
    for c in game_state.characters:
        yield _character_state_to_str(c, game_state)


def move_name(move: object) -> str:
    cls_name = move.__class__.__name__.replace("Effect", "")
    return re.sub(r"(?<!^)(?=[A-Z])", " ", cls_name)


def _describe_deal_damage(transformation, game_state) -> str:
    return (
        f"{_character_to_str(transformation.target)} "
        f"is dealt {transformation.actual_damage(game_state)} damage"
    )


def _describe_heal(transformation, _) -> str:
    return (
        f"{_character_to_str(transformation.target)} is "
        f"healed by {transformation.hit_points_increment} hit points"
    )


def _describe_recharge_mana(transformation, _) -> str:
    return (
        f"Recharge provides {transformation.recharge_amount} mana "
        f"to {_character_to_str(transformation.target)}"
    )


def _describe_add_timed_effect(transformation, _) -> str:
    return f"Its timer is {transformation.duration}"


def _describe_remove_effect(_, game_state) -> str:
    effect_state = current_effect_state(game_state)
    assert effect_state is not None
    effect_name = move_name(effect_state.effect)
    return f"{effect_name} wears off."


def _describe_decrement_timer(_, game_state) -> str:
    effect_state = current_effect_state(game_state)
    assert effect_state is not None
    assert effect_state.timer is not None
    timer = effect_state.timer - 1
    effect_name = move_name(effect_state.effect)
    return f"{effect_name} timer is now {timer}"


def _transformation_description(
    transformation: AtomicTransformation, game_state: GameState
) -> str:
    descriptions = {
        DealDamage: _describe_deal_damage,
        Heal: _describe_heal,
        RechargeMana: _describe_recharge_mana,
        AddTimedEffect: _describe_add_timed_effect,
        RemoveEffect: _describe_remove_effect,
        DecrementEffectTimer: _describe_decrement_timer,
    }
    if type(transformation) in descriptions:
        return descriptions[type(transformation)](transformation, game_state)
    else:
        return ""


def action_to_str(action: GameAction, game_state: GameState) -> Iterator[str]:
    if isinstance(action, CompositeAction):
        descriptions = [
            _transformation_description(t, game_state)
            for t in action.transformations
        ]
        for d in descriptions:
            if d:
                yield d


def _direct_damage_to_str(move: DirectDamage, game_state: GameState) -> str:
    armor_value = armor(game_state, move.target)
    if armor_value:
        actual_damage = move.damage - armor_value
        damage_str = f"{move.damage} - {armor_value} = {actual_damage}"
    else:
        damage_str = str(move.damage)
    caster = _character_to_str(current_turn(game_state))
    return f"{caster} attacks for {damage_str} damage!"


def move_to_str(move: GameMove, game_state: GameState) -> str:
    if isinstance(move, DirectDamage):
        return _direct_damage_to_str(move, game_state)
    else:
        caster = _character_to_str(current_turn(game_state))
        return f"{caster} casts {move_name(move)}"
