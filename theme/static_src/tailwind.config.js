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
                    'base-inverted': withOpacity('text-base-inverted'),
                    'muted': withOpacity('text-muted'),
                    'muted-inverted': withOpacity('text-muted-inverted'),
                    'primary': withOpacity('text-primary'),
                    'primary-inverted': withOpacity('text-primary-inverted'),
                    'secondary': withOpacity('text-secondary'),
                    'secondary-inverted': withOpacity('text-secondary-inverted'),
                    'accent': withOpacity('text-accent'),
                    'accent-inverted': withOpacity('text-accent-inverted'),
                    'error': withOpacity('text-error'),
                    'error-inverted': withOpacity('text-error-inverted'),
                    'success': withOpacity('text-success'),
                    'success-inverted': withOpacity('text-success-inverted'),
                    'link': withOpacity('text-link'),
                    'link-inverted': withOpacity('text-link-inverted'),
                },
            },
            backgroundColor: {
                skin: {
                    'base': withOpacity('bg-base'),
                    'base-inverted': withOpacity('bg-base-inverted'),
                    'muted': withOpacity('bg-muted'),
                    'muted-inverted': withOpacity('bg-muted-inverted'),
                    'primary': withOpacity('bg-primary'),
                    'primary-inverted': withOpacity('bg-primary-inverted'),
                    'secondary': withOpacity('bg-secondary'),
                    'secondary-inverted': withOpacity('bg-secondary-inverted'),
                    'accent': withOpacity('bg-accent'),
                    'accent-inverted': withOpacity('bg-accent-inverted'),
                    'inverted': withOpacity('bg-inverted'),
                    'overlay': withOpacity('bg-overlay'),
                    'overlay-inverted': withOpacity('bg-overlay-inverted'),
                    'fill-base': withOpacity('fill-base'),
                    'fill-base-inverted': withOpacity('fill-base-inverted'),
                    'fill-muted': withOpacity('fill-muted'),
                    'fill-muted-inverted': withOpacity('fill-muted-inverted'),
                    'fill-primary': withOpacity('fill-primary'),
                    'fill-primary-inverted': withOpacity('fill-primary-inverted'),
                    'fill-secondary': withOpacity('fill-secondary'),
                    'fill-secondary-inverted': withOpacity('fill-secondary-inverted'),
                    'fill-accent': withOpacity('fill-accent'),
                    'fill-accent-inverted': withOpacity('fill-accent-inverted'),
                    'fill-error': withOpacity('fill-error'),
                    'fill-error-inverted': withOpacity('fill-error-inverted'),
                    'fill-success': withOpacity('fill-success'),
                    'fill-success-inverted': withOpacity('fill-success-inverted'),
                },
            },
            borderColor: {
                skin: {
                    'base': withOpacity('border-base'),
                    'base-inverted': withOpacity('border-base-inverted'),
                    'muted': withOpacity('border-muted'),
                    'muted-inverted': withOpacity('border-muted-inverted'),
                    'primary': withOpacity('border-primary'),
                    'primary-inverted': withOpacity('border-primary-inverted'),
                    'secondary': withOpacity('border-secondary'),
                    'secondary-inverted': withOpacity('border-secondary-inverted'),
                    'accent': withOpacity('border-accent'),
                    'accent-inverted': withOpacity('border-accent-inverted'),
                    'inverted': withOpacity('border-inverted'),
                    'error': withOpacity('border-error'),
                    'error-inverted': withOpacity('border-error-inverted'),
                    'success': withOpacity('border-success'),
                    'success-inverted': withOpacity('border-success-inverted'),
                },
            },
            fill: {
                skin: {
                    'base': withOpacity('fill-base'),
                    'base-inverted': withOpacity('fill-base-inverted'),
                    'muted': withOpacity('fill-muted'),
                    'muted-inverted': withOpacity('fill-muted-inverted'),
                    'primary': withOpacity('fill-primary'),
                    'primary-inverted': withOpacity('fill-primary-inverted'),
                    'secondary': withOpacity('fill-secondary'),
                    'secondary-inverted': withOpacity('fill-secondary-inverted'),
                    'accent': withOpacity('fill-accent'),
                    'accent-inverted': withOpacity('fill-accent-inverted'),
                    'inverted': withOpacity('fill-inverted'),
                    'error': withOpacity('fill-error'),
                    'error-inverted': withOpacity('fill-error-inverted'),
                    'success': withOpacity('fill-success'),
                    'success-inverted': withOpacity('fill-success-inverted'),
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
