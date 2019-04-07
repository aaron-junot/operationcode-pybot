from aiohttp.web_response import Response

from . import slack, airtable, api


async def handle_health_check(request):
    return Response(status=200)
