import json

# Get the Raw Rows value from Zapier
rows = input_data["ResponseRows"]

# Zapier may send the data as text.
# Convert it into a real Python list.
if isinstance(rows, str):
    rows = json.loads(rows)

# The first row contains the questions / column headers
headers = rows[0]

# All remaining rows contain participant answers
answer_rows = rows[1:]

responses = []

# Go through each participant's row
for row in answer_rows:

    participant = {}

    # Match each answer with the question in the same position
    for index, question in enumerate(headers):

        # Use an empty value if the row is missing an answer
        answer = row[index] if index < len(row) else ""

        # Remove extra spaces around questions and answers
        question = str(question).strip()

        if isinstance(answer, str):
            answer = answer.strip()

        participant[question] = answer

    responses.append(participant)


print (responses)

# Send clean JSON to the next Zapier step
return {
    "responses_json": json.dumps(responses, ensure_ascii=False, indent=2),
    "response_count": len(responses)
}
