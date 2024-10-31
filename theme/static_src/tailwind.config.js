/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */
function withOpacity(variableName) {
    return ({opacityValue}) => {
        if (opacityValue !== undefined) {
            return `rgba(var(--${variableName}), ${opacityValue})`
        }
        return `rgb(var(--${variableName}))`
    }
}


module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        '../../**/*.py'
    ],
    safelist: [
        {
            pattern: /text-skin-(base|muted|primary|secondary|tertiary|accent|error|success|warning|info|link|link-hover|link-active)/,
            variants: ['hover', 'focus', 'active', 'disabled', 'group-hover']
        },
        // Background colors
        {
            pattern: /bg-skin-(base|muted|primary|secondary|tertiary|accent|error|success|warning|info|surface|surface-hover|overlay)/,
            variants: ['hover', 'focus', 'active', 'disabled', 'group-hover']
        },
        // Border colors
        {
            pattern: /border-skin-(base|muted|primary|secondary|tertiary|accent|error|success|warning|info)/,
            variants: ['hover', 'focus', 'active', 'disabled', 'group-hover']
        },
        // Ring colors
        {
            pattern: /ring-skin-(base|muted|primary|secondary|tertiary|accent|error|success|warning|info)/,
            variants: ['hover', 'focus', 'active', 'disabled', 'group-hover']
        },
        // Fill colors for SVGs
        {
            pattern: /fill-skin-(base|muted|primary|secondary|tertiary|accent|error|success|warning|info)/,
            variants: ['hover', 'focus', 'active', 'disabled', 'group-hover']
        },
        // Opacity variations for the withOpacity function
        {
            pattern: /opacity-\d+/,
        }
    ],
    theme: {
        extend: {

            screens: {
                '3xl': '1600px',
                '6xl': '1900px',
            },

            transitionDuration: {
                '1500': '1500ms',
                '2000': '2000ms',
                '2500': '2500ms',
                '3000': '3000ms',
            },

            writingMode: {
                'vertical-rl': 'vertical-rl',
                'vertical-lr': 'vertical-lr',
                'vertical-tb': 'vertical-up',
            },
            minHeight: {
                'nav-offset': 'calc(100vh - 5rem)',
                'screen-4': 'calc(100vh - 1rem)',
                'screen-8': 'calc(100vh - 2rem)',
                'screen-12': 'calc(100vh - 3rem)',
                'screen-16': 'calc(100vh - 4rem)',
                'screen-20': 'calc(100vh - 5rem)',
                'screen-24': 'calc(100vh - 6rem)',

            },

            gridTemplateColumns: {
                '13': 'repeat(13, minmax(0, 1fr))',
                '14': 'repeat(14, minmax(0, 1fr))',
                '15': 'repeat(15, minmax(0, 1fr))',
            },
            textColor: {
                skin: {
                    'base': withOpacity('text-base'),
                    'muted': withOpacity('text-muted'),
                    'primary': withOpacity('text-primary'),
                    'secondary': withOpacity('text-secondary'),
                    'tertiary': withOpacity('text-tertiary'),
                    'accent': withOpacity('text-accent'),
                    'error': withOpacity('text-error'),
                    'success': withOpacity('text-success'),
                    'warning': withOpacity('text-warning'),
                    'info': withOpacity('text-info'),
                    'link': withOpacity('text-link'),
                    'link-hover': withOpacity('text-link-hover'),
                    'link-active': withOpacity('text-link-active'),
                },
            },
            backgroundColor: {
                skin: {
                    'base': withOpacity('bg-base'),
                    'muted': withOpacity('bg-muted'),
                    'primary': withOpacity('bg-primary'),
                    'secondary': withOpacity('bg-secondary'),
                    'tertiary': withOpacity('bg-tertiary'),
                    'accent': withOpacity('bg-accent'),
                    'error': withOpacity('bg-error'),
                    'success': withOpacity('bg-success'),
                    'warning': withOpacity('bg-warning'),
                    'info': withOpacity('bg-info'),
                    'surface': withOpacity('bg-surface'),
                    'surface-hover': withOpacity('bg-surface-hover'),
                    'overlay': withOpacity('bg-overlay'),
                },
            },
            borderColor: {
                skin: {
                    'base': withOpacity('border-base'),
                    'muted': withOpacity('border-muted'),
                    'primary': withOpacity('border-primary'),
                    'secondary': withOpacity('border-secondary'),
                    'tertiary': withOpacity('border-tertiary'),
                    'accent': withOpacity('border-accent'),
                    'error': withOpacity('border-error'),
                    'success': withOpacity('border-success'),
                    'warning': withOpacity('border-warning'),
                    'info': withOpacity('border-info'),
                },
            },
            ringColor: {
                skin: {
                    'base': withOpacity('border-base'),
                    'muted': withOpacity('border-muted'),
                    'primary': withOpacity('border-primary'),
                    'secondary': withOpacity('border-secondary'),
                    'tertiary': withOpacity('border-tertiary'),
                    'accent': withOpacity('border-accent'),
                    'error': withOpacity('border-error'),
                    'success': withOpacity('border-success'),
                    'warning': withOpacity('border-warning'),
                    'info': withOpacity('border-info'),
                },
            },
            fill: {
                skin: {
                    'base': withOpacity('icon-base'),
                    'muted': withOpacity('icon-muted'),
                    'primary': withOpacity('icon-primary'),
                    'secondary': withOpacity('icon-secondary'),
                    'tertiary': withOpacity('icon-tertiary'),
                    'accent': withOpacity('icon-accent'),
                    'error': withOpacity('icon-error'),
                    'success': withOpacity('icon-success'),
                    'warning': withOpacity('icon-warning'),
                    'info': withOpacity('icon-info'),
                },
            },
            typography: ({theme}) => ({
                skin: {
                    css: {
                        '--tw-prose-body': `rgb(var(--text-base))`,
                        '--tw-prose-headings': `rgb(var(--text-base))`,
                        '--tw-prose-lead': `rgb(var(--text-muted))`,
                        '--tw-prose-links': `rgb(var(--text-link))`,
                        '--tw-prose-bold': `rgb(var(--text-accent))`,
                        '--tw-prose-counters': `rgb(var(--text-muted))`,
                        '--tw-prose-bullets': `rgb(var(--text-muted))`,
                        '--tw-prose-hr': `rgb(var(--border-base))`,
                        '--tw-prose-quotes': `rgb(var(--text-secondary))`,
                        '--tw-prose-quote-borders': `rgb(var(--border-base))`,
                        '--tw-prose-captions': `rgb(var(--text-muted))`,
                        '--tw-prose-code': `rgb(var(--text-secondary))`,
                        '--tw-prose-pre-code': `rgb(var(--text-base))`,
                        '--tw-prose-pre-bg': `rgb(var(--bg-surface))`,
                        '--tw-prose-th-borders': `rgb(var(--border-base))`,
                        '--tw-prose-td-borders': `rgb(var(--border-base))`,

                        // Invert colors
                        '--tw-prose-invert-body': `rgb(var(--text-muted))`,
                        '--tw-prose-invert-headings': `rgb(var(--text-base))`,
                        '--tw-prose-invert-lead': `rgb(var(--text-muted))`,
                        '--tw-prose-invert-links': `rgb(var(--text-link))`,
                        '--tw-prose-invert-bold': `rgb(var(--text-accent))`,
                        '--tw-prose-invert-counters': `rgb(var(--text-muted))`,
                        '--tw-prose-invert-bullets': `rgb(var(--text-muted))`,
                        '--tw-prose-invert-hr': `rgb(var(--border-muted))`,
                        '--tw-prose-invert-quotes': `rgb(var(--text-base))`,
                        '--tw-prose-invert-quote-borders': `rgb(var(--border-muted))`,
                        '--tw-prose-invert-captions': `rgb(var(--text-muted))`,
                        '--tw-prose-invert-code': `rgb(var(--text-secondary))`,
                        '--tw-prose-invert-pre-code': `rgb(var(--text-muted))`,
                        '--tw-prose-invert-pre-bg': 'rgba(0, 0, 0, 0.5)',
                        '--tw-prose-invert-th-borders': `rgb(var(--border-muted))`,
                        '--tw-prose-invert-td-borders': `rgb(var(--border-muted))`,
                    },
                },
            }),

        },
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
        function ({addUtilities}) {
            addUtilities({
                '.writing-mode-vertical-rl': {
                    'writing-mode': 'vertical-rl',
                    'text-orientation': 'mixed',
                },
                '.writing-mode-vertical-lr': {
                    'writing-mode': 'vertical-lr',
                    'text-orientation': 'mixed',
                    'transform': 'rotate(180deg)',
                },
                '.writing-mode-vertical-up': {
                    'writing-mode': 'vertical-rl',
                    'transform': 'rotate(180deg)',
                    'text-orientation': 'upright',
                },
            });
        },

    ],
}
