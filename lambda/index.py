import json
import urllib.request

MODEL_API_URL = ""

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])

        prompt = body.get("message", "")

        request_payload = json.dumps({"prompt": prompt}).encode("utf-8")
        req = urllib.request.Request(
            MODEL_API_URL,
            data=request_payload,
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        with urllib.request.urlopen(req) as res:
            res_body = res.read()
        result = json.loads(res_body)

        assistant_response = result.get("generated_text")

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": json.dumps({
                "success": True,
                "response": assistant_response
            })
        }

    except Exception as error:
        print("Error:", str(error))
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            "body": json.dumps({"success": False, "error": str(error)})
        }
