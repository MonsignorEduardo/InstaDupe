from typing import Annotated

from fastapi import APIRouter, Depends
from instagrapi import Client

router = APIRouter()


async def get_client(session_id: str):
	print(session_id)
	cl = Client()
	result = cl.login_by_sessionid(session_id)

	if not result:
		raise Exception('Invalid session id')
	return cl


@router.get('/get_non_friends')
def get_non_friends(user_id: str, cl: Annotated[Client, Depends(get_client)]):
	# Get all followers
	followers = cl.user_followers(user_id)

	followers_name = {follower.username for follower in followers.values()}

	# Get all following
	following = cl.user_following(user_id)

	following_name = {follower.username for follower in following.values()}

	# Get followers that Im not following
	non_following = followers_name - following_name
	# Get following that don't follow me
	not_follower = following_name - followers_name

	return non_following.union(not_follower)
