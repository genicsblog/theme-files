module.exports = {
  darkMode: 'class',
  content: [
    './**/*.html',
  ],
  safelist: [
    '!bg-android',
    '!bg-jekyll',
    '!bg-web',
    '!bg-web3',
    '!bg-node-js',
    '!bg-backend',
    '!bg-api',
    'hover:border-android', 'dark:hover:!border-android',
    'hover:border-web', 'dark:hover:!border-web',
    'hover:border-web3', 'dark:hover:!border-web3',
    'hover:border-jekyll', 'dark:hover:!border-jekyll',
    'hover:border-node-js', 'dark:hover:!border-node-js',
    'hover:border-backend', 'dark:hover:!border-backend',
    'hover:border-api', 'dark:hover:!border-api',
    'mt-16'
  ],
  theme: {
    extend: {
      colors: {
        'background': '#16161f',
        'primary': '#2564eb',
        'web': '#F06529',
        'web3': '#6cdcc4',
        'android': '#3ddc84',
        'jekyll': '#c83c3c',
        'node-js': '#68a063',
        'backend': '#1494fc',
        'api': '#fceccc'
      }
    },
  },
  variants: {},
  plugins: [],
}
