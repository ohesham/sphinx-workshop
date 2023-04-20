from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Riddle:
    question: str
    answer: str

    def check_answer(self, answer: str) -> bool:
        """Evaluates the given answer to the riddle.

        Args:
            answer (str): The given answer to the riddle.

        Returns:
            str: The result of the evaluation of the answer.
        """
        return answer.lower() == self.answer.lower()

    def get_hint(self) -> Iterator[str]:
        yield from iter(self.answer)
