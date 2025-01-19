from ipykernel.kernels import IPythonKernel
from redash_python import Redash
import json
import os
from typing import Dict, Any


class RedashKernel(IPythonKernel):
    implementation = "Redash"
    implementation_version = "0.1.0"
    language = "sql"
    language_version = "0.1.0"
    language_info = {
        "name": "sql",
        "mimetype": "text/x-sql",
        "file_extension": ".sql",
    }
    banner = "Redash Kernel - Execute Redash queries directly from Jupyter"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.redash_url = os.environ.get("REDASH_URL")
        self.redash_api_key = os.environ.get("REDASH_API_KEY")

        if not self.redash_url or not self.redash_api_key:
            raise ValueError(
                "Please set REDASH_URL and REDASH_API_KEY environment variables"
            )

        self.redash_client = Redash(self.redash_url, self.redash_api_key)

    def do_execute(
        self,
        code: str,
        silent: bool,
        store_history: bool = True,
        user_expressions: Dict[str, Any] = None,
        allow_stdin: bool = False,
    ) -> Dict[str, Any]:
        try:
            # Execute the query
            query_id = None
            if code.strip().isdigit():
                # If the input is just a number, treat it as a query ID
                query_id = int(code.strip())
                result = self.redash_client.get_query_results(query_id)
            else:
                # Otherwise, create a new query and execute it
                query = self.redash_client.create_query(
                    name="Jupyter Query",
                    query_text=code,
                    data_source_id=1,  # Default data source ID
                )
                result = self.redash_client.get_query_results(query["id"])

            # Format the results
            if not silent:
                stream_content = {
                    "name": "stdout",
                    "text": json.dumps(result, indent=2),
                }
                self.send_response(self.iopub_socket, "stream", stream_content)

            return {
                "status": "ok",
                "execution_count": self.execution_count,
                "payload": [],
                "user_expressions": {},
            }

        except Exception as e:
            return {
                "status": "error",
                "ename": type(e).__name__,
                "evalue": str(e),
                "traceback": [],
            }
