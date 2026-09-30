def build_context(
    results,
    max_chars: int = 6000
):
    context_parts = []
    total_chars = 0

    for result in results:

        text = result.payload.get("text", "").strip()

        if not text:
            continue

        if text in context_parts:
            continue

        if total_chars + len(text) > max_chars:
            break

        context_parts.append(text)
        total_chars += len(text)

    return "\n\n---\n\n".join(context_parts)