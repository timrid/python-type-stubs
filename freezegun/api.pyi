import datetime
import numbers
import types
from typing import Any, Callable, Optional, Sequence, Tuple, Type, Union


class TickingDateTimeFactory(object):
    def __init__(self, time_to_freeze: datetime.datetime, start: datetime.datetime):
        self.time_to_freeze: datetime.datetime = ...
        self.start: datetime.datetime = ...

    def __call__(self) -> datetime.datetime:
        ...


class FrozenDateTimeFactory(object):
    def __init__(self, time_to_freeze: datetime.datetime):
        self.time_to_freeze: datetime.datetime = ...

    def __call__(self) -> datetime.datetime:
        ...

    def tick(self, delta: Union[float, numbers.Real, datetime.timedelta] = ...):
        ...

    def move_to(
        self,
        target_datetime: Optional[
            Union[str, datetime.datetime, datetime.date, datetime.timedelta]
        ],
    ):
        """Moves frozen datetime.date to the given ``target_datetime``"""
        ...


class StepTickTimeFactory(object):
    def __init__(self, time_to_freeze: datetime.datetime, step_width: float):
        self.time_to_freeze = ...
        self.step_width = ...

    def __call__(self) -> datetime.datetime:
        ...

    def tick(self, delta: Optional[datetime.timedelta] = ...):
        ...

    def update_step_width(self, step_width: float):
        self.step_width = ...

    def move_to(
        self,
        target_datetime: Optional[
            Union[str, datetime.datetime, datetime.date, datetime.timedelta]
        ],
    ):
        """Moves frozen datetime.date to the given ``target_datetime``"""
        ...


class _freeze_time:
    time_to_freeze: datetime.datetime = ...
    tz_offset: float = ...
    ignore: Sequence[str] = ...
    tick: bool = ...
    auto_tick_seconds: float = ...
    undo_changes: Sequence[Tuple[types.ModuleType, str, Any]] = ...
    modules_at_start: Sequence[str] = ...
    as_arg: bool = ...

    def __init__(
        self,
        time_to_freeze_str: Union[
            None, str, datetime.datetime, datetime.date, datetime.timedelta
        ],
        tz_offset: float,
        ignore: Sequence[str],
        tick: bool,
        as_arg: bool,
        auto_tick_seconds: float,
    ) -> None:
        ...

    def __call__(self, func: Union[type, types.CoroutineType, Callable]):
        ...

    def __enter__(self):
        ...

    def __exit__(self, *args: Any) -> None:
        ...

    def start(
        self,
    ) -> Union[StepTickTimeFactory, TickingDateTimeFactory, FrozenDateTimeFactory]:
        ...

    def stop(self) -> None:
        ...

    def decorate_class(self, klass):
        ...

    def decorate_coroutine(self, coroutine):
        ...

    def decorate_callable(self, func):
        ...


def freeze_time(
    time_to_freeze: Optional[
        Union[
            str,
            datetime.datetime,
            datetime.date,
            datetime.timedelta,
            types.FunctionType,
            types.GeneratorType,
        ]
    ] = ...,
    tz_offset: Optional[float] = ...,
    ignore: Optional[Sequence[str]] = ...,
    tick: Optional[bool] = ...,
    as_arg: Optional[bool] = ...,
    auto_tick_seconds: Optional[float] = ...,
) -> _freeze_time:
    ...
