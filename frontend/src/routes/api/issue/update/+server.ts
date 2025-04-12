import { BACKEND_API_URL } from '$env/static/private';
import { fetchWithAuth } from '$lib/util/api';

// class IssueUpdateView(APIView):
//     permission_classes = [IsAuthenticated]

//     def patch(self, request, owner, repo, id, state):
//         github = GithubAPI(request.user)
//         success = False
//         if state == 'open':
//              success = github.open_issue(owner, repo, id)
//         else:
//             success = github.close_issue(owner, repo, id)
//         return Response(status=200 if success else 500)

export const POST = async ({ request, cookies }) => {
	const { owner, repo, id, state } = await request.json();
	const token = cookies.get('token');

	const data = await fetchWithAuth({
		fetch: fetch,
		cookies: cookies,
		endpoint: `${BACKEND_API_URL}api/update_issue?format=json`,
		method: 'PATCH',
		body: {
			owner,
			repo,
			id,
			state
		},
		token
	});
	return new Response(data);
};
