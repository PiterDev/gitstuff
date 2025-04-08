import { dev } from '$app/environment';
import { BACKEND_API_URL } from '$env/static/private';
import { redirect } from '@sveltejs/kit';

export const GET = async ({ url, fetch, cookies }) => {
	const code = url.searchParams.get('code');

	if (!code) {
		throw new Response('No code provided', { status: 400 });
	}

	const res = await fetch(BACKEND_API_URL + 'auth/login?format=json', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			code: code
		})
	});
	const data = await res.json();

	cookies.set('token', data.key, {
		path: '/',
		secure: !dev,
		httpOnly: true,
		maxAge: 60 * 60 * 24 // A Github token is valid for 24 hours
	});

	throw redirect(301, '/');
};
