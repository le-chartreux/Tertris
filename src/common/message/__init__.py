"""
File that contains the declaration of the Message class, that is used by the views to ask things to the model
"""
import common.message.message_subject as m_message_subject
import typing


class Message:
    def __init__(
            self,
            subject: m_message_subject.MessageSubject,
            content: typing.Any = None
    ):
        self._subject = subject
        self._content = content

    # GETTERS
    def get_subject(self) -> m_message_subject.MessageSubject:
        return self._subject

    def get_content(self) -> typing.Any:
        return self._content
