"""Intersect Elements Command"""

# Shared
from src.modules.shared.application import Command, CommandResponse, AbstractUnitOfWork

# Build-ins
from dataclasses import dataclass


@dataclass
class IntersectElementsCommand(Command):
    name: str
    status: int


def intersect_elements(
    uow: AbstractUnitOfWork,
    command: IntersectElementsCommand,
) -> CommandResponse:
    with uow:
        elements = uow.element_repository.get_by_name(name=command.name)


    return CommandResponse(dto=command)
