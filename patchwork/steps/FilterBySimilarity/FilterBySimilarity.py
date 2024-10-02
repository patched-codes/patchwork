from __future__ import annotations

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from patchwork.logger import logger
from patchwork.step import Step, StepStatus
from patchwork.steps.FilterBySimilarity.typed import (
    FilterBySimilarityInputs,
    FilterBySimilarityOutputs,
)


class FilterBySimilarity(Step, input_class=FilterBySimilarityInputs, output_class=FilterBySimilarityOutputs):
    def __init__(self, inputs):
        super().__init__(inputs)

        self.list = inputs["list"]
        self.keywords = inputs["keywords"]
        self.keys = self.__parse_keys(inputs.get("keys", None))
        self.top_k = inputs.get("top_k", 10)

    @staticmethod
    def __parse_keys(keys: list[str] | str | None) -> list[str] | None:
        if keys is None:
            return None

        if isinstance(keys, str):
            delimiter = None
            if "," in keys:
                delimiter = ","
            return [key.strip() for key in keys.split(delimiter)]

        return keys

    def run(self):
        if len(self.list) == 0:
            self.set_status(StepStatus.SKIPPED, "List is empty")
            return dict()

        items_with_score = []
        for item in self.list:
            if self.keys is not None:
                texts = [str(item[key]) for key in self.keys if item.get(key) is not None]
            else:
                texts = [value for value in item.values() if value is not None and isinstance(value, str)]
            if len(texts) == 0:
                logger.warning(f"No text found in item: {item}")
                continue

            vectorizer = TfidfVectorizer()
            vectorizer.fit(texts)
            keyword_vectors = vectorizer.transform([self.keywords])

            similarity_scores = []
            for text in texts:
                text_vector = vectorizer.transform([text])
                similarity = cosine_similarity(text_vector, keyword_vectors)[0][0]
                similarity_scores.append(similarity)

            avg_similarity = sum(similarity_scores) / len(similarity_scores)
            items_with_score.append((item, avg_similarity))

        items_with_score.sort(key=lambda x: x[1], reverse=True)
        return dict(result_list=[item for item, _ in items_with_score[: self.top_k]])
