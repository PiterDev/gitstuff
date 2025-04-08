import { BACKEND_API_URL } from '$env/static/private';
import { redirectIfUnauthorized } from '$lib/util/auth.js';
import { error, redirect } from '@sveltejs/kit';

export const load = async ({ parent, params, fetch, cookies }) => {
	const { isAuthorized } = await parent();
	redirectIfUnauthorized(isAuthorized);

	const token = cookies.get('token');

	const { repo } = params;
	const res = await fetch(BACKEND_API_URL + `api/repo_issues?repo_name=${repo}&format=json`, {
		method: 'GET',
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Token ${token}`
		}
	});

	const data = await res.json();

	if (data.status === '404') {
		error(404, 'Repo not found');
	}

	if (data.status === '401') {
		// Token expired
		cookies.delete('token', { path: '/' });
		throw redirect(302, '/auth/github/login?session_expired=true');
	}

	return {
		issues: data
	};
};
