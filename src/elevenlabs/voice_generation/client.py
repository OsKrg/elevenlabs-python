# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.voice_generation_parameter_response import VoiceGenerationParameterResponse
from ..core.unchecked_base_model import construct_type
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.gender import Gender
from ..types.age import Age
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.voice import Voice
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class VoiceGenerationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def generate_parameters(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceGenerationParameterResponse:
        """
        Get possible parameters for the /v1/voice-generation/generate-voice endpoint.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceGenerationParameterResponse
            Successful Response

        Examples
        --------
        from elevenlabs import ElevenLabs

        client = ElevenLabs(
            api_key="YOUR_API_KEY",
        )
        client.voice_generation.generate_parameters()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/voice-generation/generate-voice/parameters",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    VoiceGenerationParameterResponse,
                    construct_type(
                        type_=VoiceGenerationParameterResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def generate(
        self,
        *,
        gender: Gender,
        accent: str,
        age: Age,
        accent_strength: float,
        text: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Generate a random voice based on parameters. This method returns a generated_voice_id in the response header, and a sample of the voice in the body. If you like the generated voice call /v1/voice-generation/create-voice with the generated_voice_id to create the voice.

        Parameters
        ----------
        gender : Gender
            Category code corresponding to the gender of the generated voice. Possible values: female, male.

        accent : str
            Category code corresponding to the accent of the generated voice. Possible values: american, british, african, australian, indian.

        age : Age
            Category code corresponding to the age of the generated voice. Possible values: young, middle_aged, old.

        accent_strength : float
            The strength of the accent of the generated voice. Has to be between 0.3 and 2.0.

        text : str
            Text to generate, text length has to be between 100 and 1000.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Yields
        ------
        typing.Iterator[bytes]
            Successful Response

        Examples
        --------
        from elevenlabs import ElevenLabs

        client = ElevenLabs(
            api_key="YOUR_API_KEY",
        )
        client.voice_generation.generate(
            gender="female",
            accent="american",
            age="middle_aged",
            accent_strength=2.0,
            text="It sure does, Jackie… My mama always said: “In Carolina, the air's so thick you can wear it!”",
        )
        """
        with self._client_wrapper.httpx_client.stream(
            "v1/voice-generation/generate-voice",
            method="POST",
            json={
                "gender": gender,
                "accent": accent,
                "age": age,
                "accent_strength": accent_strength,
                "text": text,
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:
            try:
                if 200 <= _response.status_code < 300:
                    _chunk_size = request_options.get("chunk_size", 1024) if request_options is not None else 1024
                    for _chunk in _response.iter_bytes(chunk_size=_chunk_size):
                        yield _chunk
                    return
                _response.read()
                if _response.status_code == 422:
                    raise UnprocessableEntityError(
                        typing.cast(
                            HttpValidationError,
                            construct_type(
                                type_=HttpValidationError,  # type: ignore
                                object_=_response.json(),
                            ),
                        )
                    )
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_a_previously_generated_voice(
        self,
        *,
        voice_name: str,
        voice_description: str,
        generated_voice_id: str,
        played_not_selected_voice_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        labels: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Voice:
        """
        Create a previously generated voice. This endpoint should be called after you fetched a generated_voice_id using /v1/voice-generation/generate-voice.

        Parameters
        ----------
        voice_name : str
            Name to use for the created voice.

        voice_description : str
            Description to use for the created voice.

        generated_voice_id : str
            The generated_voice_id to create, call POST /v1/voice-generation/generate-voice and fetch the generated_voice_id from the response header if don't have one yet.

        played_not_selected_voice_ids : typing.Optional[typing.Sequence[str]]
            List of voice ids that the user has played but not selected. Used for RLHF.

        labels : typing.Optional[typing.Dict[str, str]]
            Optional, metadata to add to the created voice. Defaults to None.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Voice
            Successful Response

        Examples
        --------
        from elevenlabs import ElevenLabs

        client = ElevenLabs(
            api_key="YOUR_API_KEY",
        )
        client.voice_generation.create_a_previously_generated_voice(
            voice_name="Alex",
            voice_description="Middle-aged American woman",
            generated_voice_id="rbVJFu6SGRD1dbWpKnWl",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/voice-generation/create-voice",
            method="POST",
            json={
                "voice_name": voice_name,
                "voice_description": voice_description,
                "generated_voice_id": generated_voice_id,
                "played_not_selected_voice_ids": played_not_selected_voice_ids,
                "labels": labels,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Voice,
                    construct_type(
                        type_=Voice,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncVoiceGenerationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def generate_parameters(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceGenerationParameterResponse:
        """
        Get possible parameters for the /v1/voice-generation/generate-voice endpoint.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceGenerationParameterResponse
            Successful Response

        Examples
        --------
        import asyncio

        from elevenlabs import AsyncElevenLabs

        client = AsyncElevenLabs(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.voice_generation.generate_parameters()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/voice-generation/generate-voice/parameters",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    VoiceGenerationParameterResponse,
                    construct_type(
                        type_=VoiceGenerationParameterResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def generate(
        self,
        *,
        gender: Gender,
        accent: str,
        age: Age,
        accent_strength: float,
        text: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Generate a random voice based on parameters. This method returns a generated_voice_id in the response header, and a sample of the voice in the body. If you like the generated voice call /v1/voice-generation/create-voice with the generated_voice_id to create the voice.

        Parameters
        ----------
        gender : Gender
            Category code corresponding to the gender of the generated voice. Possible values: female, male.

        accent : str
            Category code corresponding to the accent of the generated voice. Possible values: american, british, african, australian, indian.

        age : Age
            Category code corresponding to the age of the generated voice. Possible values: young, middle_aged, old.

        accent_strength : float
            The strength of the accent of the generated voice. Has to be between 0.3 and 2.0.

        text : str
            Text to generate, text length has to be between 100 and 1000.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Yields
        ------
        typing.AsyncIterator[bytes]
            Successful Response

        Examples
        --------
        import asyncio

        from elevenlabs import AsyncElevenLabs

        client = AsyncElevenLabs(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.voice_generation.generate(
                gender="female",
                accent="american",
                age="middle_aged",
                accent_strength=2.0,
                text="It sure does, Jackie… My mama always said: “In Carolina, the air's so thick you can wear it!”",
            )


        asyncio.run(main())
        """
        async with self._client_wrapper.httpx_client.stream(
            "v1/voice-generation/generate-voice",
            method="POST",
            json={
                "gender": gender,
                "accent": accent,
                "age": age,
                "accent_strength": accent_strength,
                "text": text,
            },
            request_options=request_options,
            omit=OMIT,
        ) as _response:
            try:
                if 200 <= _response.status_code < 300:
                    _chunk_size = request_options.get("chunk_size", 1024) if request_options is not None else 1024
                    async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size):
                        yield _chunk
                    return
                await _response.aread()
                if _response.status_code == 422:
                    raise UnprocessableEntityError(
                        typing.cast(
                            HttpValidationError,
                            construct_type(
                                type_=HttpValidationError,  # type: ignore
                                object_=_response.json(),
                            ),
                        )
                    )
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_a_previously_generated_voice(
        self,
        *,
        voice_name: str,
        voice_description: str,
        generated_voice_id: str,
        played_not_selected_voice_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        labels: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Voice:
        """
        Create a previously generated voice. This endpoint should be called after you fetched a generated_voice_id using /v1/voice-generation/generate-voice.

        Parameters
        ----------
        voice_name : str
            Name to use for the created voice.

        voice_description : str
            Description to use for the created voice.

        generated_voice_id : str
            The generated_voice_id to create, call POST /v1/voice-generation/generate-voice and fetch the generated_voice_id from the response header if don't have one yet.

        played_not_selected_voice_ids : typing.Optional[typing.Sequence[str]]
            List of voice ids that the user has played but not selected. Used for RLHF.

        labels : typing.Optional[typing.Dict[str, str]]
            Optional, metadata to add to the created voice. Defaults to None.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Voice
            Successful Response

        Examples
        --------
        import asyncio

        from elevenlabs import AsyncElevenLabs

        client = AsyncElevenLabs(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.voice_generation.create_a_previously_generated_voice(
                voice_name="Alex",
                voice_description="Middle-aged American woman",
                generated_voice_id="rbVJFu6SGRD1dbWpKnWl",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/voice-generation/create-voice",
            method="POST",
            json={
                "voice_name": voice_name,
                "voice_description": voice_description,
                "generated_voice_id": generated_voice_id,
                "played_not_selected_voice_ids": played_not_selected_voice_ids,
                "labels": labels,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Voice,
                    construct_type(
                        type_=Voice,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(
                        HttpValidationError,
                        construct_type(
                            type_=HttpValidationError,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
