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

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    safelist: [
        {
            pattern: /.*/,  // Match every class pattern to include all styles
        },
    ],
    theme: {
        extend: {

            screens: {
                '3xl': '1600px',
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
            textColor: {
                skin: {
                    'base': withOpacity('text-base'),
                    'muted': withOpacity('text-muted'),
                    'primary': withOpacity('text-primary'),
                    'secondary': withOpacity('text-secondary'),
                    'accent': withOpacity('text-accent'),
                    'error': withOpacity('text-error'),
                    'success': withOpacity('text-success'),
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
                    'accent': withOpacity('bg-accent'),
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
                    'accent': withOpacity('border-accent'),
                    'error': withOpacity('border-error'),
                    'success': withOpacity('border-success'),
                },
            },
            fill: {
                skin: {
                    'base': withOpacity('icon-base'),
                    'muted': withOpacity('icon-muted'),
                    'primary': withOpacity('icon-primary'),
                    'secondary': withOpacity('icon-secondary'),
                    'accent': withOpacity('icon-accent'),
                    'error': withOpacity('icon-error'),
                    'success': withOpacity('icon-success'),
                },
            },
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
