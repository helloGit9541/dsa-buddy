/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './base/**/*.{html,js}',
    './accounts/**/*.{html,js}',
  ],
  theme: {
    extend: {
      fontFamily: {
        'inter': ["Inter", "Roboto", 'sans-serif']
      }
    },
  },
  plugins: [],
}
