import { BACKEND_API_URL } from '$env/static/private';
import { fetchWithAuth } from '$lib/util/api';

export const POST = async ({ request, cookies }) => {
    const token = cookies.get('token');
    const { owner, repo, title, body } = await request.json();

    const response = await fetchWithAuth({
        fetch,
        cookies,
        endpoint: `${BACKEND_API_URL}api/create_issue?format=json`,
        method: 'POST',
        token,
        body: {
            owner,
            repo,
            title,
            body
        }
    });

    return new Response(JSON.stringify(response), {
        status: response?.id ? 201 : 400,
        headers: { 'Content-Type': 'application/json' }
    });
};