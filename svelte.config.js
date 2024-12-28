import adapter from '@sveltejs/adapter-vercel'
import { sveltePreprocess } from 'svelte-preprocess'

// const filePath = dirname(fileURLToPath(import.meta.url))
// const varsPath = `${filePath}/src/vars.scss`

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://svelte.dev/docs/kit/integrations
	// for more information about preprocessors
	preprocess: sveltePreprocess({
		scss: {
			prependData: `@use 'src/vars.scss' as *;`
		}
	}),
	// @use 'src/vars' as *;
	kit: {
		// adapter-auto only supports some environments, see https://svelte.dev/docs/kit/adapter-auto for a list.
		// If your environment is not supported, or you settled on a specific environment, switch out the adapter.
		// See https://svelte.dev/docs/kit/adapters for more information about adapters.
		adapter: adapter()
	}
}

export default config
