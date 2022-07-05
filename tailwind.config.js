const extendedColors = {
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

const safelist = [];

Object.keys(extendedColors).filter(
  item => item !== 'background' || item !== 'primary'
).forEach((item) => {
  safelist.push(`!bg-${item}`);
  safelist.push(`hover:border-${item}`);
  safelist.push(`dark:hover:!border-${item}`);
});

safelist.push("mt-16");

module.exports = {
  darkMode: 'class',
  content: [
    './**/*.html',
  ],
  safelist: safelist,
  theme: {
    extend: {
      colors: extendedColors
    },
  },
  variants: {},
  plugins: [
    require('@tailwindcss/line-clamp'),
  ],
}
