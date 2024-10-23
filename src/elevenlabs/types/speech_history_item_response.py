# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .speech_history_item_response_model_voice_category import SpeechHistoryItemResponseModelVoiceCategory
from .feedback_item import FeedbackItem
from .speech_history_item_response_model_source import SpeechHistoryItemResponseModelSource
from .history_alignments_response_model import HistoryAlignmentsResponseModel
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class SpeechHistoryItemResponse(UncheckedBaseModel):
    history_item_id: str
    request_id: typing.Optional[str] = None
    voice_id: typing.Optional[str] = None
    model_id: typing.Optional[str] = None
    voice_name: typing.Optional[str] = None
    voice_category: typing.Optional[SpeechHistoryItemResponseModelVoiceCategory] = None
    text: typing.Optional[str] = None
    date_unix: typing.Optional[int] = None
    character_count_change_from: typing.Optional[int] = None
    character_count_change_to: typing.Optional[int] = None
    content_type: typing.Optional[str] = None
    state: typing.Optional[typing.Optional[typing.Any]] = None
    settings: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    feedback: typing.Optional[FeedbackItem] = None
    share_link_id: typing.Optional[str] = None
    source: typing.Optional[SpeechHistoryItemResponseModelSource] = None
    alignments: typing.Optional[HistoryAlignmentsResponseModel] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
