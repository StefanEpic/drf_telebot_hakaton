from drf_spectacular.utils import extend_schema, extend_schema_view

video_summary = extend_schema_view(
    list=extend_schema(summary="Получение списка всех видео", description="Постраничный вывод списка всех видео"),
)

video_detail_summary = extend_schema_view(
    retrieve=extend_schema(
        summary="Получение информации о видео по ID",
        description="Получить подробную информацию о видео по его ID. Также выводится самая популярная эмоция и еда для этого видео",
    ),
)

video_emotion_summary = extend_schema(
    summary="Передача результата голосования. Какая эмоция ассоциируется с видео",
    description="Передать ID видео и ID эмоции. Переданные данные влияют на вес связи этого видео и эмоции",
)

video_food_summary = extend_schema(
    summary="Передача результата голосования. Какая закуска ассоциируется с видео",
    description="Передать ID видео и ID закуски. Переданные данные влияют на вес связи этого видео и закуски",
)

video_random_summary = extend_schema(
    summary="Получение информации о рандомном видео",
    description="Получение информации о рандомном видео для голосования",
)

emotion_summary = extend_schema_view(
    list=extend_schema(summary="Получение списка всех эмоций", description="Постраничный вывод списка всех эмоций")
)

emotion_detail_summary = extend_schema_view(
    retrieve=extend_schema(
        summary="Получение информации об эмоции по ID",
        description="Получить подробную информацию о эмоции по ее ID. Также выводится самое популярное видео для этой эмоции",
    ),
)

food_summary = extend_schema_view(
    list=extend_schema(summary="Получение списка всех закусок", description="Постраничный вывод списка всех закусок"),
)

food_detail_summary = extend_schema_view(
    retrieve=extend_schema(
        summary="Получение информации о закуске по ID",
        description="Получить подробную информацию о закуске по ее ID. Также выводится самое популярное видео для этой закуски",
    ),
)
