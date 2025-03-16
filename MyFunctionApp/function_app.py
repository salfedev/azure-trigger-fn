import azure.functions as func
import json

app = func.FunctionApp()  # ✅ Explicitly declare the function app

@app.function_name(name="HttpTriggerFunction")  # ✅ Register the function
@app.route(route="hello", auth_level=func.AuthLevel.ANONYMOUS)  # ✅ Define HTTP route
def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get("name")
    if not name:
        try:
            req_body = req.get_json()
            name = req_body.get("name")
        except ValueError:
            pass

    if name:
        return func.HttpResponse(
            json.dumps({"message": f"Hello, {name}!"}),
            mimetype="application/json",
            status_code=200
        )
    else:
        return func.HttpResponse(
            json.dumps({"error": "Please provide a name"}),
            mimetype="application/json",
            status_code=400
        )
