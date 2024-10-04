/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */
function withOpacity(variableName) {
    return ({opacityValue}) => {
        if (opacityValue !== undefined) {
            return `rgba(var(${variableName}), ${opacityValue})`
        }
        return `rgb(var(${variableName}))`
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
    theme: {
        extend: {
            minHeight: {
                'nav-offset': 'calc(100vh - 5rem)',
            },
            textColor: {
                skin: {
                    'base': withOpacity('var(--text-base)'),
                    'muted': withOpacity('var(--text-muted)'),
                    'primary': withOpacity('var(--text-primary)'),
                    'secondary': withOpacity('var(--text-secondary)'),
                    'accent': withOpacity('var(--text-accent)'),
                    'error': withOpacity('var(--text-error)'),
                    'success': withOpacity('var(--text-success)'),
                    'link': withOpacity('var(--text-link)'),
                }
            },
            backgroundColor: {
                skin: {
                    'base': withOpacity('var(--bg-base)'),
                    'muted': withOpacity('var(--bg-muted)'),
                    'primary': withOpacity('var(--bg-primary)'),
                    'secondary': withOpacity('var(--bg-secondary)'),
                    'accent': withOpacity('var(--bg-accent)'),
                    'inverted': withOpacity('var(--bg-inverted)'),
                    'overlay': withOpacity('var(--bg-overlay)'),
                }
            },
            border: {
                skin: {
                    'base': withOpacity('var(--border-base)'),
                    'muted': withOpacity('var(--border-muted)'),
                    'primary': withOpacity('var(--border-primary)'),
                    'secondary': withOpacity('var(--border-secondary)'),
                    'accent': withOpacity('var(--border-accent)'),
                    'inverted': withOpacity('var(--border-inverted)'),
                    'error': withOpacity('var(--border-error)'),
                    'success': withOpacity('var(--border-success)'),
                }
            },
            fill: {
                skin: {
                    'base': withOpacity('var(--fill-base)'),
                    'muted': withOpacity('var(--fill-muted)'),
                    'primary': withOpacity('var(--fill-primary)'),
                    'secondary': withOpacity('var(--fill-secondary)'),
                    'accent': withOpacity('var(--fill-accent)'),
                    'inverted': withOpacity('var(--fill-inverted)'),
                    'error': withOpacity('var(--fill-error)'),
                    'success': withOpacity('var(--fill-success)'),
                }
            }
        },
        transitionDuration: {
            '1500': '1500ms',
            '2000': '2000ms',
            '2500': '2500ms',
            '3000': '3000ms',
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
