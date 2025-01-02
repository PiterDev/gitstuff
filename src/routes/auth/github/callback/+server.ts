import { redirect } from '@sveltejs/kit'
import { dev } from '$app/environment'

export const GET = async ({ url, fetch, cookies }) => {
	const code = url.searchParams.get('code')

	if (!code) {
		return new Response('Missing code', { status: 400 })
	}
	const response = await fetch('http://127.0.0.1:8000/auth/github/', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ code })
	})

	if (!response.ok) {
		return new Response('Failed to authenticate', { status: response.status })
	}

	const data = await response.json()
	//  FIX: fix JWT on backend
	cookies.set('token', data.token, {
		path: '/',
		secure: !dev,
		httpOnly: true,
		maxAge: 60 * 60 * 24 * 14 // 2 weeks
	})
	throw redirect(302, '/')
}
