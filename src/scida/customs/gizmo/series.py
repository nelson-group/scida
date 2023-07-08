import os

from scida.customs.gadgetstyle.series import GadgetStyleSimulation
from scida.discovertypes import CandidateStatus


class GizmoSimulation(GadgetStyleSimulation):
    """A series representing a gizmo simulation."""

    def __init__(self, path, lazy=True, async_caching=False, **interface_kwargs):
        prefix_dict = dict(paths="snapdir")
        super().__init__(
            path,
            prefix_dict=prefix_dict,
            lazy=lazy,
            async_caching=async_caching,
            **interface_kwargs
        )

    @classmethod
    def validate_path(cls, path, *args, **kwargs) -> CandidateStatus:
        if not os.path.isdir(path):
            return CandidateStatus.NO
        if "gizmo_parameters.txt" in os.listdir(path):
            return CandidateStatus.YES
        return CandidateStatus.NO
