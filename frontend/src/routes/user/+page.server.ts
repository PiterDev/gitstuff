// +page.server.ts
import { BACKEND_API_URL } from '$env/static/private';
import { fetchWithAuth } from '$lib/util/api.js';

export const load = async ({ fetch, cookies }) => {
	const token = cookies.get('token');

	const data = await fetchWithAuth({
		fetch,
		cookies,
		endpoint: `${BACKEND_API_URL}api/user?format=json`,
		method: 'GET',
		token,
		body: null
	});

	return {
		data
	};
};
