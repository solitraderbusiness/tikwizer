from fastapi import HTTPException

from app.generator import mql_generator


def generate(data: dict) -> dict:
    """
    Wrap the MQL generator to produce code from the given input data.

    If *data* does not already contain a top-level ``"data"`` key the
    payload is wrapped automatically so the generator always receives
    the expected ``{"data": ...}`` structure.

    Returns
    -------
    dict
        ``{"code": <generated_mql>, "filename": "expert_output.mq4"}``

    Raises
    ------
    HTTPException (500)
        When the generator returns an error string (prefixed with
        ``"ERROR:"``).
    """
    if "data" not in data:
        data = {"data": data}

    result = mql_generator.generate_mql(data)

    if isinstance(result, str) and result.startswith("ERROR:"):
        raise HTTPException(status_code=500, detail=result)

    return {"code": result, "filename": "expert_output.mq4"}
