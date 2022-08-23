/** @type {import('tailwindcss').Config} */
module.exports = {
	darkMode: 'class',

	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			aspectRatio: { '4/3': '4/3' }
		}
	},
	plugins: [require('@tailwindcss/typography')]
};
